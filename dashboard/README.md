# Milestone 2 — Dashboard Integration

**Owner:** Nafisa (Member 13 — Dashboard Integration Lead)
**Business Question Covered on This Page:** Admission Trends (Member 2 — Nafisa)
**Module:** Patient Flow & Service Demand Intelligence

This folder contains the fully integrated Milestone 2 dashboard — a multi-page Dash application that brings together the visualization work from all six Type B members into one running app.

---

## 📁 Structure

```
dashboard/
├── app.py                              # Main entry point — starts the Dash server
├── README.md                           # This file
├── assets/
│   └── reports/                        # Static Plotly HTML exports (auto-served by Dash)
│       ├── dept_load.html              # Tanvi — Department-wise Patient Load
│       ├── discharge_flow.html         # Keerthi — Patient Discharge & Flow
│       ├── treatment_demand.html       # Sarthak — Treatment & Service Demand
│       ├── bottleneck_capacity.html    # Sarthak — Bottlenecks & Capacity Strain
│       └── surgery_workload.html       # Divya — Surgery Workload
└── pages/
    ├── page1_admissions_component.py   # Nafisa — Admission Trends (live Dash component)
    ├── page1_patient_flow.py           # Page 1: Admissions + Dept Load
    ├── page2_discharge_treatment.py    # Page 2: Discharge & Flow + Treatment Demand
    └── page3_bottleneck_surgery.py     # Page 3: Bottlenecks + Surgery Workload
```

---

## 🚀 How to Run

**1. Clone the repo and navigate to the project root** (not into `dashboard/`):
```bash
git clone https://github.com/springboardmentor647/medical-operations-dashboard-team-a-batch1.git
cd medical-operations-dashboard-team-a-batch1
```

**2. Create and activate a virtual environment:**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

**3. Install dependencies:**
```bash
pip install dash plotly pandas
```

**4. Run the app — from the repo root:**
```bash
python dashboard/app.py
```

**5. Open your browser:**
```
http://localhost:8050
```

**6. Navigate** using the links at the top of the page — Page 1, Page 2, Page 3.

> ⚠️ The app must be run from the **repo root**, not from inside `dashboard/`. The scripts use relative paths (e.g. `data/processed/admissions_clean.csv`) that assume the repo root as the working directory.

---

## 📊 What's on Each Page

| Page | Business Question | Owner (Analysis → Viz) | Type |
|---|---|---|---|
| Page 1 | Admission Trends | Divya → Nafisa | Live Dash (interactive slider + KPI cards) |
| Page 1 | Department-wise Patient Load | Srivalli → Tanvi | Embedded static Plotly export |
| Page 2 | Patient Discharge & Flow | Sowmitha → Keerthi | Embedded static Plotly export |
| Page 2 | Treatment & Service Demand | Abhinay → Sarthak | Embedded static Plotly export |
| Page 3 | Bottlenecks & Capacity Strain | Sarthak → Sarthak | Embedded static Plotly export |
| Page 3 | Surgery Workload | Deepika → Divya (covered for Aarthi) | Embedded static Plotly export |

---

## 🔧 Integration Approach

Four of the six visualization contributions (Tanvi, Keerthi, Sarthak ×2) were built as **standalone, self-contained Plotly HTML exports** (generated via `plotly.io.to_html()` in each member's notebook) rather than live Dash apps with callbacks.

Rather than rewriting each person's already-finished, tested work into Dash callback components — which would have meant reverse-engineering their figures and risking breaking something that already worked — each static HTML file is:

1. Copied into `dashboard/assets/reports/` (Dash auto-serves anything in `assets/`)
2. Embedded into the relevant page via `html.Iframe(src="/assets/reports/<file>.html")`

This keeps every member's original output fully intact and isolated (no shared component IDs, no risk of one person's code breaking another's), while still presenting everything inside one unified, navigable dashboard.

Only the Admission Trends chart (Nafisa/Member 2) is a genuinely live, interactive Dash component — it uses `dash.register_page()` with a real callback so the date-range slider filters the chart in real time.

---

## ✅ Status

- [x] Page 1 — Admission Trends (live/interactive)
- [x] Page 1 — Department-wise Patient Load
- [x] Page 2 — Patient Discharge & Flow
- [x] Page 2 — Treatment & Service Demand
- [x] Page 3 — Bottlenecks & Capacity Strain
- [x] Page 3 — Surgery Workload *(completed by Divya, covering for Aarthi)*

---

## 🐞 Known Issues / Notes for Reviewers

- `Sarthak`'s original `Treatment_and_service_demand_visualization.ipynb` notebook file was found empty (0 bytes) in the submitted work — his final exported dashboard HTML is intact and used here, but the source notebook behind it may need to be recovered/rebuilt separately.
- Surgery Workload (Page 3) was originally assigned to Aarthi; Divya completed this analysis and visualization on her behalf. The dashboard's KPI numbers (Total Surgeries: 3,505; Success Rate: 33.07%; Avg Duration: 195.31 min) come directly from her `Surgery_Workload.xlsx` output.
