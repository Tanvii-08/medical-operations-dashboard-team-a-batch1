// ====================================================
// Healthcare Service Coverage Map — Application Logic
// Uses REAL data from the project's CSV files
// ====================================================

// ── CSV Parser ───────────────────────────────────────

function parseCSV(text) {
    const lines = text.trim().split('\n');
    const headers = lines[0].replace(/\r/g, '').split(',');
    const rows = [];
    for (let i = 1; i < lines.length; i++) {
        const values = lines[i].replace(/\r/g, '').split(',');
        if (values.length === headers.length) {
            const row = {};
            headers.forEach((h, idx) => row[h.trim()] = values[idx].trim());
            rows.push(row);
        }
    }
    return rows;
}

// ── Department color palette — vibrant and distinct ──

const DEPT_COLORS = {
    D001: "#ef4444", D002: "#f97316", D003: "#f59e0b", D004: "#eab308",
    D005: "#84cc16", D006: "#22c55e", D007: "#10b981", D008: "#14b8a6",
    D009: "#06b6d4", D010: "#0ea5e9", D011: "#3b82f6", D012: "#6366f1",
    D013: "#8b5cf6", D014: "#a855f7", D015: "#d946ef", D016: "#ec4899",
    D017: "#f43f5e", D018: "#fb7185", D019: "#38bdf8", D020: "#34d399"
};

// ── Application State ────────────────────────────────

const APP = {
    map: null,
    markers: null,
    heatLayer: null,
    departments: [],       // from departments_clean.csv
    doctors: [],           // from doctors_preprocessed.csv
    geocodes: [],          // from facility_geocodes.csv
    serviceCoverage: [],   // from service_coverage.csv
    mergedDepts: [],       // departments + geocodes + coverage merged
    filteredDoctors: [],
    departmentMarkers: {},
    circleOverlays: [],
    currentFilters: {
        department: "all",
        serviceType: "all",
        timePeriod: "all",
        experience: "all"
    }
};

// ── Initialize Application ───────────────────────────

document.addEventListener("DOMContentLoaded", async () => {
    try {
        await loadRealData();
        initMap();
        populateFilters();
        applyFilters();
        bindEvents();
        renderBottomBar();

        // Entrance animation
        document.querySelectorAll('.filter-group, .stat-item').forEach((el, i) => {
            el.style.opacity = '0';
            el.style.transform = 'translateY(12px)';
            setTimeout(() => {
                el.style.transition = 'all 0.5s cubic-bezier(0.16, 1, 0.3, 1)';
                el.style.opacity = '1';
                el.style.transform = 'translateY(0)';
            }, 80 + i * 60);
        });

        console.log(`✅ Loaded REAL data: ${APP.departments.length} departments, ${APP.doctors.length} doctors, ${APP.geocodes.length} geocodes`);
    } catch (err) {
        console.error('Failed to load data:', err);
    }
});

// ── Load Real CSV Data ───────────────────────────────

async function loadRealData() {
    const [deptText, docText, geoText, covText] = await Promise.all([
        fetch('data/departments_clean.csv').then(r => r.text()),
        fetch('data/doctors_preprocessed.csv').then(r => r.text()),
        fetch('data/facility_geocodes.csv').then(r => r.text()),
        fetch('data/service_coverage.csv').then(r => r.text())
    ]);

    APP.departments = parseCSV(deptText);
    APP.doctors = parseCSV(docText);
    APP.geocodes = parseCSV(geoText);
    APP.serviceCoverage = parseCSV(covText);

    // Parse numeric fields
    APP.geocodes.forEach(g => {
        g.latitude = parseFloat(g.latitude);
        g.longitude = parseFloat(g.longitude);
    });

    APP.doctors.forEach(d => {
        d.experience = parseInt(d.Experience, 10);
        d.departmentId = d.Department_ID;
        d.specialization = d.Specialization;
        d.id = d.Doctor_ID;
        d.name = d.Doctor_Name;
    });

    APP.serviceCoverage.forEach(s => {
        s.latitude = parseFloat(s.latitude);
        s.longitude = parseFloat(s.longitude);
        s.Doctor_Count = parseInt(s.Doctor_Count, 10);
        s.Average_Experience = parseFloat(s.Average_Experience);
        s.Service_Radius_KM = parseFloat(s.Service_Radius_KM);
        s.Catchment_Area_Sq_KM = parseFloat(s.Catchment_Area_Sq_KM);
    });

    // Merge departments with geocodes and coverage
    APP.mergedDepts = APP.geocodes.map(geo => {
        const dept = APP.departments.find(d => d.department_id === geo.department_id);
        const cov = APP.serviceCoverage.find(c => c.department_id === geo.department_id);
        return {
            id: geo.department_id,
            name: geo.department_name,
            lat: geo.latitude,
            lng: geo.longitude,
            // Service coverage data
            doctorCount: cov ? cov.Doctor_Count : 0,
            avgExperience: cov ? cov.Average_Experience : 0,
            serviceAvailability: cov ? cov.Service_Availability : 'Unknown',
            serviceRadius: cov ? cov.Service_Radius_KM : 5,
            catchmentArea: cov ? cov.Catchment_Area_Sq_KM : 0,
            coverageStatus: cov ? cov.Service_Coverage_Status : 'Unknown'
        };
    });

    APP.filteredDoctors = [...APP.doctors];
}

// ── Map Initialization ───────────────────────────────

function initMap() {
    const center = getMapCenter();

    APP.map = L.map('map', {
        center: center,
        zoom: 12,
        zoomControl: true,
        attributionControl: false,
        minZoom: 10,
        maxZoom: 17
    });

    // Free OpenStreetMap tiles with dark-mode CSS filter (no API key needed)
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
        maxZoom: 19
    }).addTo(APP.map);

    // Apply dark inversion filter
    document.querySelector('.leaflet-tile-pane').style.filter =
        'invert(1) hue-rotate(200deg) brightness(0.6) contrast(1.3) saturate(0.4)';

    // Marker cluster group
    APP.markers = L.markerClusterGroup({
        maxClusterRadius: 50,
        spiderfyOnMaxZoom: true,
        showCoverageOnHover: false,
        zoomToBoundsOnClick: true,
        iconCreateFunction: (cluster) => {
            const count = cluster.getChildCount();
            let size = 'small';
            if (count > 10) size = 'large';
            else if (count > 5) size = 'medium';

            return L.divIcon({
                html: `<div>${count}</div>`,
                className: `marker-cluster marker-cluster-${size}`,
                iconSize: L.point(44, 44)
            });
        }
    });

    APP.map.addLayer(APP.markers);
}

function getMapCenter() {
    if (APP.mergedDepts.length === 0) return [17.41, 78.475];
    const avgLat = APP.mergedDepts.reduce((s, d) => s + d.lat, 0) / APP.mergedDepts.length;
    const avgLng = APP.mergedDepts.reduce((s, d) => s + d.lng, 0) / APP.mergedDepts.length;
    return [avgLat, avgLng];
}

// ── Populate Filters ─────────────────────────────────

function populateFilters() {
    // Department filter
    const deptSelect = document.getElementById('filter-department');
    APP.mergedDepts.forEach(dept => {
        const opt = document.createElement('option');
        opt.value = dept.id;
        opt.textContent = `${dept.name} (${dept.id})`;
        deptSelect.appendChild(opt);
    });

    // Service type filter (unique specializations from real data)
    const specSet = new Set();
    APP.doctors.forEach(d => specSet.add(d.specialization));
    const specSelect = document.getElementById('filter-service-type');
    [...specSet].sort().forEach(spec => {
        const opt = document.createElement('option');
        opt.value = spec;
        opt.textContent = spec;
        specSelect.appendChild(opt);
    });
}

// ── Event Bindings ───────────────────────────────────

function bindEvents() {
    document.getElementById('filter-department').addEventListener('change', onFilterChange);
    document.getElementById('filter-service-type').addEventListener('change', onFilterChange);
    document.getElementById('filter-time-period').addEventListener('change', onFilterChange);
    document.getElementById('filter-experience').addEventListener('change', onFilterChange);
    document.getElementById('btn-reset-filters').addEventListener('click', resetFilters);
}

function onFilterChange() {
    APP.currentFilters.department = document.getElementById('filter-department').value;
    APP.currentFilters.serviceType = document.getElementById('filter-service-type').value;
    APP.currentFilters.timePeriod = document.getElementById('filter-time-period').value;
    APP.currentFilters.experience = document.getElementById('filter-experience').value;
    applyFilters();
}

function resetFilters() {
    document.getElementById('filter-department').value = 'all';
    document.getElementById('filter-service-type').value = 'all';
    document.getElementById('filter-time-period').value = 'all';
    document.getElementById('filter-experience').value = 'all';
    APP.currentFilters = { department: "all", serviceType: "all", timePeriod: "all", experience: "all" };
    applyFilters();

    // Reset animation
    const btn = document.getElementById('btn-reset-filters');
    btn.style.transform = 'rotate(360deg)';
    setTimeout(() => btn.style.transform = '', 500);
}

// ── Apply Filters & Render ───────────────────────────

function applyFilters() {
    const f = APP.currentFilters;

    APP.filteredDoctors = APP.doctors.filter(doc => {
        if (f.department !== "all" && doc.departmentId !== f.department) return false;
        if (f.serviceType !== "all" && doc.specialization !== f.serviceType) return false;
        if (f.experience !== "all") {
            const exp = doc.experience;
            if (f.experience === "junior" && (exp < 1 || exp > 5)) return false;
            if (f.experience === "mid" && (exp < 6 || exp > 15)) return false;
            if (f.experience === "senior" && (exp < 16 || exp > 25)) return false;
            if (f.experience === "expert" && exp < 26) return false;
        }
        // Time period filter simulates quarters by dividing doctor IDs
        if (f.timePeriod !== "all") {
            const docNum = parseInt(doc.id.replace('DR', ''), 10);
            const quarter = ((docNum - 1) % 4);
            const quarterMap = { q1: 0, q2: 1, q3: 2, q4: 3 };
            if (quarter !== quarterMap[f.timePeriod]) return false;
        }
        return true;
    });

    renderMarkers();
    updateStats();
    renderLegend();
    renderBottomBar();
}

// ── Render Map Markers ───────────────────────────────

function renderMarkers() {
    APP.markers.clearLayers();
    APP.circleOverlays.forEach(c => APP.map.removeLayer(c));
    APP.circleOverlays = [];
    if (APP.heatLayer) {
        APP.map.removeLayer(APP.heatLayer);
        APP.heatLayer = null;
    }

    // Aggregate filtered doctors per department
    const deptAgg = {};
    APP.filteredDoctors.forEach(doc => {
        if (!deptAgg[doc.departmentId]) {
            deptAgg[doc.departmentId] = {
                doctors: [],
                specializations: new Set()
            };
        }
        deptAgg[doc.departmentId].doctors.push(doc);
        deptAgg[doc.departmentId].specializations.add(doc.specialization);
    });

    const heatPoints = [];

    APP.mergedDepts.forEach(dept => {
        const agg = deptAgg[dept.id];
        if (!agg) return;

        const color = DEPT_COLORS[dept.id] || '#6366f1';
        const doctorCount = agg.doctors.length;
        const avgExp = (agg.doctors.reduce((s, d) => s + d.experience, 0) / doctorCount).toFixed(1);
        const specs = [...agg.specializations];

        // Coverage status badge colors
        const statusColor = dept.coverageStatus === 'Better Served' ? '#10b981' : '#f59e0b';
        const statusBg = dept.coverageStatus === 'Better Served'
            ? 'rgba(16, 185, 129, 0.12)' : 'rgba(245, 158, 11, 0.12)';

        // Coverage radius circle (using real service radius from CSV)
        const radiusMeters = (dept.serviceRadius || 5) * 1000;
        const circle = L.circle([dept.lat, dept.lng], {
            radius: radiusMeters,
            color: color,
            fillColor: color,
            fillOpacity: 0.05,
            weight: 1.5,
            opacity: 0.3,
            dashArray: '8 5'
        }).addTo(APP.map);
        APP.circleOverlays.push(circle);

        // Custom marker icon
        const icon = L.divIcon({
            className: 'custom-marker',
            html: `
                <div class="marker-pulse" style="background: ${color};"></div>
                <div class="marker-pin" style="background: ${color};">
                    <span style="transform: rotate(45deg); color: white; font-size: 11px; font-weight: 700; z-index: 2; position: relative;">${doctorCount}</span>
                </div>
            `,
            iconSize: [30, 42],
            iconAnchor: [15, 42],
            popupAnchor: [0, -45]
        });

        // Popup content with REAL data
        const specsHtml = specs.map(s =>
            `<span class="popup-spec-tag">${s}</span>`
        ).join('');

        const popupContent = `
            <div class="popup-content">
                <div class="popup-header">
                    <div class="popup-dept-color" style="background: ${color};"></div>
                    <div>
                        <div class="popup-dept-name">${dept.name}</div>
                        <div class="popup-dept-id">${dept.id} • ${dept.lat.toFixed(4)}°N, ${dept.lng.toFixed(4)}°E</div>
                    </div>
                </div>
                <div class="popup-stats">
                    <div class="popup-stat">
                        <span class="popup-stat-value" style="color: ${color};">${doctorCount}</span>
                        <span class="popup-stat-label">Doctors (filtered)</span>
                    </div>
                    <div class="popup-stat">
                        <span class="popup-stat-value" style="color: var(--accent-secondary);">${avgExp}</span>
                        <span class="popup-stat-label">Avg Exp (yrs)</span>
                    </div>
                    <div class="popup-stat">
                        <span class="popup-stat-value" style="color: ${statusColor};">${dept.serviceAvailability}</span>
                        <span class="popup-stat-label">Availability</span>
                    </div>
                    <div class="popup-stat">
                        <span class="popup-stat-value" style="font-size:0.8rem; color: ${statusColor}; background: ${statusBg}; padding: 2px 8px; border-radius: 20px;">${dept.coverageStatus}</span>
                        <span class="popup-stat-label">Coverage Status</span>
                    </div>
                </div>
                <div style="font-size:0.68rem; color: var(--text-muted); margin-bottom:8px;">
                    📍 Radius: ${dept.serviceRadius} km • Area: ${dept.catchmentArea.toFixed(1)} km²
                </div>
                <div class="popup-specializations">${specsHtml}</div>
            </div>
        `;

        const marker = L.marker([dept.lat, dept.lng], { icon })
            .bindPopup(popupContent, { maxWidth: 340, closeButton: true });

        APP.markers.addLayer(marker);
        APP.departmentMarkers[dept.id] = marker;

        // Heat data
        const maxDocs = Math.max(...APP.mergedDepts.map(d => d.doctorCount || 1));
        heatPoints.push([dept.lat, dept.lng, doctorCount / maxDocs]);
    });

    // Add heatmap layer
    if (heatPoints.length > 0) {
        APP.heatLayer = L.heatLayer(heatPoints, {
            radius: 45,
            blur: 30,
            maxZoom: 15,
            max: 1.0,
            gradient: {
                0.2: '#06b6d4',
                0.4: '#6366f1',
                0.6: '#a855f7',
                0.8: '#ec4899',
                1.0: '#ef4444'
            }
        }).addTo(APP.map);
    }
}

// ── Update Statistics ────────────────────────────────

function updateStats() {
    const uniqueDepts = new Set(APP.filteredDoctors.map(d => d.departmentId));
    const uniqueSpecs = new Set(APP.filteredDoctors.map(d => d.specialization));
    const totalDepts = uniqueDepts.size;
    const totalDoctors = APP.filteredDoctors.length;
    const coverage = ((totalDepts / APP.mergedDepts.length) * 100).toFixed(0);

    animateCounter('stat-departments', totalDepts);
    animateCounter('stat-doctors', totalDoctors);
    animateCounter('stat-specializations', uniqueSpecs.size);
    document.getElementById('stat-coverage').textContent = `${coverage}%`;

    // Header stats
    document.getElementById('active-departments-count').textContent = totalDepts;
    document.getElementById('active-doctors-count').textContent = totalDoctors;
}

function animateCounter(elementId, target) {
    const el = document.getElementById(elementId);
    const current = parseInt(el.textContent) || 0;
    const diff = target - current;
    const steps = 20;
    const stepValue = diff / steps;
    let step = 0;

    const timer = setInterval(() => {
        step++;
        el.textContent = Math.round(current + stepValue * step);
        if (step >= steps) {
            el.textContent = target;
            clearInterval(timer);
        }
    }, 20);
}

// ── Render Legend ─────────────────────────────────────

function renderLegend() {
    const container = document.getElementById('legend-items');
    const deptCounts = {};

    APP.filteredDoctors.forEach(doc => {
        deptCounts[doc.departmentId] = (deptCounts[doc.departmentId] || 0) + 1;
    });

    const items = APP.mergedDepts
        .filter(dept => deptCounts[dept.id])
        .map(dept => ({
            dept,
            count: deptCounts[dept.id],
            status: dept.coverageStatus
        }))
        .sort((a, b) => b.count - a.count);

    container.innerHTML = items.map(({ dept, count, status }) => {
        const statusIcon = status === 'Better Served' ? '🟢' : '🟡';
        return `
            <div class="legend-item" data-dept="${dept.id}" onclick="focusDepartment('${dept.id}')">
                <span class="legend-dot" style="background: ${DEPT_COLORS[dept.id]}; color: ${DEPT_COLORS[dept.id]};"></span>
                <span>${dept.name}</span>
                <span title="${status}" style="font-size:10px;">${statusIcon}</span>
                <span class="legend-count">${count}</span>
            </div>
        `;
    }).join('');
}

// ── Render Bottom Bar ────────────────────────────────

function renderBottomBar() {
    const container = document.getElementById('department-cards');
    const deptCounts = {};
    const deptSpecs = {};

    APP.filteredDoctors.forEach(doc => {
        deptCounts[doc.departmentId] = (deptCounts[doc.departmentId] || 0) + 1;
        if (!deptSpecs[doc.departmentId]) deptSpecs[doc.departmentId] = new Set();
        deptSpecs[doc.departmentId].add(doc.specialization);
    });

    const cards = APP.mergedDepts
        .filter(dept => deptCounts[dept.id])
        .sort((a, b) => (deptCounts[b.id] || 0) - (deptCounts[a.id] || 0))
        .map((dept, i) => {
            const count = deptCounts[dept.id] || 0;
            const color = DEPT_COLORS[dept.id] || '#6366f1';
            const statusBadge = dept.coverageStatus === 'Better Served'
                ? '<span style="color:#10b981;font-size:0.65rem;">● Better Served</span>'
                : '<span style="color:#f59e0b;font-size:0.65rem;">● Under-Served</span>';

            return `
                <div class="dept-card fade-in" style="animation-delay: ${i * 40}ms;"
                     onclick="focusDepartment('${dept.id}')">
                    <div style="position:absolute;top:0;left:0;width:4px;height:100%;background:${color};border-radius:4px 0 0 4px;"></div>
                    <div>
                        <div class="dept-card-name">${dept.name}</div>
                        <div class="dept-card-id">${dept.id} ${statusBadge}</div>
                    </div>
                    <div class="dept-card-stats">
                        <span class="dept-card-stat"><strong>${count}</strong> Doctors</span>
                        <span class="dept-card-stat"><strong>${dept.serviceRadius}km</strong> Radius</span>
                    </div>
                </div>
            `;
        }).join('');

    container.innerHTML = cards;
}

// ── Focus Department ─────────────────────────────────

function focusDepartment(deptId) {
    const dept = APP.mergedDepts.find(d => d.id === deptId);
    if (!dept) return;

    APP.map.flyTo([dept.lat, dept.lng], 14, {
        duration: 0.8,
        easeLinearity: 0.25
    });

    // Open popup after flying
    setTimeout(() => {
        APP.markers.eachLayer(layer => {
            if (Math.abs(layer.getLatLng().lat - dept.lat) < 0.001 &&
                Math.abs(layer.getLatLng().lng - dept.lng) < 0.001) {
                layer.openPopup();
            }
        });
    }, 900);
}
