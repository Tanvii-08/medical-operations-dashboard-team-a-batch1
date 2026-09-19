# Development of a Healthcare Operations Intelligence Dashboard with Decision Analytics Group 1

**Live App:** https://medical-operations-dashboard-team-a-h6ai.onrender.com/

## Project Overview
The **Development of a Healthcare Operations Intelligence Dashboard with Decision Analytics Group 1** is a healthcare analytics project developed as part of the **Infosys Springboard Internship**. The project focuses on collecting, preprocessing, integrating, and analyzing healthcare datasets to generate meaningful insights and support dashboard development.

### Objectives
* Collect healthcare datasets.
* Clean and preprocess the datasets.
* Integrate multiple datasets into a unified dataset.
* Generate Key Performance Indicators (KPIs).
* Perform trend analysis.
* Build a dashboard for healthcare insights.
* Maintain the project using GitHub.

### Technologies Used
* Python
* Pandas
* NumPy
* Jupyter Notebook
* Git
* Plotly Dash (dashboard framework)
* Gunicorn (production server)
* Render (deployment)

---

## Project Structure
```
medical-operations-dashboard-team-a-batch1
|
-- data/
|   -- raw/
-- notebooks/
-- src/
-- README.md
```

---

## Datasets Used
* admissions.csv
* billing.csv
* departments.csv
* doctors.csv
* lab_results.csv
* medications.csv
* patients.csv
* raw_surgeries.csv

---

## Project Workflow
1. Data Collection
2. Data Preprocessing
3. Data Integration
4. KPI Generation
5. Trend Analysis
6. Documentation & GitHub
7. Dashboard Development

---

## Team Members
| Team Member | Responsibility |
|-------------|----------------|
| Sowmitha | Data Collection, Documentation & GitHub |
| Tanvi Bhosale | Data Preprocessing (Patients Dataset) |
| Sarthak | Data Preprocessing (Lab & Billing Datasets) |
| Sirivalli Reddyvari | Data Preprocessing (Doctors Dataset) |
| Nafisa | Data Preprocessing (Departments & Admissions Datasets) |
| Divya Kumari | Data Integration |
| Rushikesh | Data Preprocessing (Surgery Dataset) |
| Indhumathi K | Data Preprocessing (Medications Dataset) |
| Deepika J | KPI Generation |
| Abhi | Trend Analysis |

---

## Team Milestone 1 Completed
* Data Collection
* Data Preprocessing
* Data Integration
* KPI Generation
* Trend Analysis
* GitHub Collaboration
* Documentation

### Future Work
* Develop an interactive Power BI Dashboard.
* Create advanced healthcare visualizations.
* Enhance KPI reporting.
* Improve operational insights.

### License
This project was developed for educational purposes as part of the Infosys Springboard Internship.

---

## Milestone 2 - Patient Flow & Service Demand Intelligence

### 1. Project Overview
Milestone 2 focuses on transforming the cleaned healthcare datasets prepared during Milestone 1 into meaningful operational insights. The team performs Exploratory Data Analysis (EDA), KPI generation, trend analysis, visualization, and dashboard development to support healthcare operational decision-making.

### 2. Milestone 2 Objective
The main objective of Milestone 2 is to analyze patient flow and healthcare service demand and convert the results into interactive dashboard insights.

#### Objectives
* Analyze admission and discharge patterns.
* Analyze department-wise patient workload.
* Monitor treatment and service demand.
* Identify operational bottlenecks and capacity strain.
* Analyze surgery workload.
* Generate KPIs and trends.
* Develop visualizations for dashboard integration.

### 3. Business Questions
Milestone 2 is organized around six core business questions:
1. Admission Trends
2. Department-wise Patient Load
3. Patient Discharge & Flow
4. Treatment & Service Demand
5. Bottlenecks & Capacity Strain
6. Surgery Workload

Each business question is handled by one Type A and one Type B team member.

---

### 4. Task Division

| Business Question | Type A - Analysis | Type B - Visualization |
|---|---|---|
| Admission Trends | Divya | Nafisa |
| Department-wise Patient Load | Srivalli | Tanvi |
| Patient Discharge & Flow | Sowmitha | Keerthi |
| Treatment & Service Demand | Abhinay | Sarthak |
| Bottlenecks & Capacity Strain | Sarthak | Sarthak |
| Surgery Workload | Deepika | Divya |
| Dashboard Integration | Nafisa | - |
| Documentation | Sowmitha | - |

Type A members perform EDA and KPI analysis, while Type B members convert the findings into visualizations and dashboard components.

---

### 5. Datasets Used

* **Admission Trends:** admissions_clean.csv
* **Department-wise Patient Load:** admissions_clean.csv, departments_clean.csv
* **Patient Discharge & Flow:** admissions_clean.csv
* **Treatment & Service Demand:** lab_results_clean.csv, billing_clean.csv
* **Bottlenecks & Capacity Strain:** admissions_clean.csv, doctors_preprocessed.csv, departments_clean.csv
* **Surgery Workload:** surgeries_clean_fixed.csv

---

### 6. Analysis Methodology
The Milestone 2 workflow follows:
Data Loading -> Data Validation -> Exploratory Data Analysis -> KPI Generation -> Trend Analysis -> Findings -> Visualization -> Dashboard Integration

Python and Pandas are used for data analysis and KPI generation.

---

### 7. Patient Discharge & Flow Analysis
For the Patient Discharge & Flow business question, the analysis uses:
* Discharge_Date
* Status
* Length_of_Stay_Days

The analysis focuses on the admission-to-discharge timeline and patient status transitions. Since no movement or transfer log is available, ward-to-ward patient movement is not analyzed.

#### KPIs Generated
* Total Patients
* Average Length of Stay
* Discharge Rate
* Patient Status Distribution
* Monthly Admissions
* Monthly Discharges
* Department-wise Admissions
* Department-wise Discharges
* Department-wise Discharge Rate

#### Key Results
* Total Patients: 5,000
* Average Length of Stay: 5.52 days
* Discharge Rate: 24.28%
* Critical Patients: 1,279
* Under Treatment: 1,272
* Recovered Patients: 1,235
* Discharged Patients: 1,214
* Highest Monthly Admissions: July - 524
* Highest Monthly Discharges: March - 584
* Highest Department Admissions: D015 - 335
* Highest Department Discharge Rate: D004 - 30.32%

---

### 8. Visualization
The Type B members use the KPI outputs and findings from Type A analysis to create dashboard visualizations. Planned visualizations include:
* Admission trend charts
* Department-wise workload charts
* Patient status distribution
* Monthly admission and discharge trends
* Length of Stay analysis
* Treatment and service demand charts
* Bottleneck and capacity indicators
* Surgery workload visualizations

---

### 9. Tools & Technologies
* Python
* Pandas
* NumPy
* Matplotlib
* Plotly / Dash or Power BI
* Google Colab
* Git & GitHub

---

### 10. GitHub Workflow
The team uses GitHub for collaborative development and documentation:
Clone Repository -> Create/Use Working Branch -> Perform Analysis -> Commit Changes -> Push Changes -> Review/Integrate -> Dashboard Assembly

Work is pushed regularly so that dashboard integration can happen smoothly.

---

### 11. Challenges & Solutions
* **Challenge 1: Different Business Questions**
  * Solution: Tasks were divided into six business questions with dedicated Type A and Type B members.
* **Challenge 2: Missing Patient Movement Data**
  * Solution: Patient flow was analyzed using admission-to-discharge timelines and status transitions since no transfer logs existed.
* **Challenge 3: Multiple Dataset Requirements**
  * Solution: Relevant datasets were mapped to each business question and joined where required.
* **Challenge 4: Dashboard Integration**
  * Solution: Type A members provide KPI numbers and findings to Type B members for visualization and dashboard integration.

---

### 12. Milestone 2 Deliverables
* EDA and KPI analysis notebooks
* Business-question-specific findings
* KPI summary tables
* Visualization outputs
* Dashboard components
* GitHub updates
* README documentation
* Final integrated dashboard

#### How to Run the Dashboard
1. Clone the repo and navigate to the project root
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   source venv/bin/activate # Mac/Linux
   ```
3. Install dependencies:
   ```bash
   pip install dash plotly pandas
   ```
4. Run the app:
   ```bash
   python dashboard/app.py
   ```
5. Open http://localhost:8050 in your browser
6. Use the nav links at the top (Page 1, 2, 3) to view each business question's visualizations

#### Status
* Page 1: Admission Trends + Department-wise Patient Load (Complete)
* Page 2: Patient Discharge & Flow + Treatment & Service Demand (Complete)
* Page 3: Bottlenecks & Capacity Strain (Complete), Surgery Workload (Pending)

---

### 13. Future Work
* Complete dashboard integration.
* Improve interactive visualizations.
* Add advanced operational indicators.
* Validate all KPI outputs.
* Finalize documentation and presentation.
* Integrate all business-question outputs into the final dashboard.

---

### 14. Conclusion
Milestone 2 transforms the cleaned healthcare datasets from Milestone 1 into actionable operational intelligence. Through EDA, KPI generation, trend analysis, visualization, and dashboard integration, the project provides insights into patient flow, service demand, workload, operational bottlenecks, and surgery workload. The completed outputs serve as the foundation for the final Medical Operations Intelligence Dashboard.

---

## Milestone 3 - Resource Utilization & Capacity Intelligence Module

### 1. Milestone 3 Overview & Objective
**Weeks 5-6 | Team of 10**

Milestone 3 focuses on **Resource Utilization & Capacity Intelligence** - developing healthcare resource intelligence dashboards and capacity monitoring capabilities covering bed utilization, workforce efficiency, department-wise resource distribution, and benchmark/capacity gap analysis.

---

### 2. Data Notes - Benchmark Gap Datasets (Resolved)

**Bed Capacity Gap (data/raw/bed_capacity.csv):**
* **Contents:** department_id, department_name, Total_Beds (one row per department)
* **Purpose:** Benchmark bed counts defined by the team to allow Bed Utilization (BQ 1) calculation.
* **Usage:** Joined against admissions_clean.csv on department_id to compute occupancy and available beds.

**Staff Capacity Gap (data/raw/staff_capacity.csv):**
* **Contents:** department_id, department_name, Total_Staff (one row per department)
* **Purpose:** Benchmark staff counts representing full healthcare staffing in proportion to bed capacity.
* **Usage:** Joined against doctors_preprocessed.csv and admissions_clean.csv on department_id for Workforce & Staffing Efficiency (BQ 2) analysis.

---

### 3. Team Assignments & Role Model (Milestone 3)
The team operates using a two-role model (**Type A: Data Analysis / EDA + KPIs** and **Type B: Visualization & Dashboard Build**):

| # | Team Member | Type | Task | Business Question |
|---|-------------|------|------|-------------------|
| 1 | **Sirivalli Reddyvari** | Type A | Analyze Bed Utilization & Occupancy | Bed Utilization & Occupancy |
| 2 | **Tanvi Ajit Bhosale** | Type B | Visualize Bed Utilization & Occupancy | Bed Utilization & Occupancy |
| 3 | **Sowmitha A** | Type A | Analyze Workforce & Staffing Efficiency | Workforce & Staffing Efficiency |
| 4 | **Sarthak Jejurkar** | Type B | Visualize Workforce & Staffing Efficiency | Workforce & Staffing Efficiency |
| 5 | **Abhi** | Type A | Analyze Department-wise Resource Utilization | Department-wise Resource Utilization |
| 6 | **Rushikesh** | Type B | Visualize Department-wise Resource Utilization | Department-wise Resource Utilization |
| 7 | **Divya Kumari** | Type A | Analyze Benchmark & Capacity Gaps | Benchmark & Capacity Gap Analysis |
| 8 | **Deepika J** | Type B | Visualize Benchmark & Capacity Gaps | Benchmark & Capacity Gap Analysis |
| 9 | **Nafisa** | Type B | **Dashboard Integration Lead** | Assembles & integrates all pages (Pages 4 & 5) |
| 10 | **Keerthi Machanooru** | Lead | **Documentation & GitHub Lead** | GitHub README, PR merges, repository folder structure |

---

### 4. Business Question Pairings & Datasets

| Business Question | Type A (Analyst) | Type B (Visualizer) | Datasets Needed |
|-------------------|------------------|---------------------|-----------------|
| **1. Bed Utilization & Occupancy** | **Sirivalli Reddyvari** | **Tanvi Ajit Bhosale** | admissions_clean.csv, departments_clean.csv, bed_capacity.csv |
| **2. Workforce & Staffing Efficiency** | **Sowmitha A** | **Sarthak Jejurkar** | admissions_clean.csv, doctors_preprocessed.csv, staff_capacity.csv |
| **3. Department-wise Resource Utilization** | **Abhi** | **Rushikesh** | admissions_clean.csv, departments_clean.csv, doctors_preprocessed.csv |
| **4. Benchmark & Capacity Gap Analysis** | **Divya Kumari** | **Deepika J** | admissions_clean.csv, bed_capacity.csv, doctors_preprocessed.csv |
| **Dashboard Integration & Docs** | - | **Nafisa & Keerthi Machanooru** | All assembled datasets, notebooks, and dashboard scripts |

---

### 5. Detailed Task Breakdown & KPIs

#### 1. Bed Utilization & Occupancy (Sirivalli Reddyvari -> Tanvi Ajit Bhosale)
* Bed Occupancy Rate per department: (Patient-days / Available bed-days) * 100
* Available Beds per department: Total_Beds - Occupied Beds
* Identify overloaded departments vs. underutilized departments
* **Visualizations:** Department-wise occupancy rate chart, available-beds chart, KPI summary cards

#### 2. Workforce & Staffing Efficiency (Sowmitha A -> Sarthak Jejurkar)
* Patients-per-Doctor Ratio: Overall and department-wise
* Patients-per-Staff Ratio: Overall and department-wise using staff_capacity.csv
* Department Workload: Admissions relative to available doctors + support staff
* **Visualizations:** Patients-per-doctor & patients-per-staff bar charts, interactive department filter

#### 3. Department-wise Resource Utilization (Abhi -> Rushikesh)
* Combine bed capacity and doctor workforce data to classify departments
* Overall Resource Utilization Score combining bed occupancy and doctor workload
* Identify departments showing the clearest operational and resource strain
* **Visualizations:** Combined resource-utilization heatmap or ranked cross-department bar chart

#### 4. Benchmark & Capacity Gap Analysis (Divya Kumari -> Deepika J)
* Compare actual operational utilization against bed_capacity.csv benchmarks
* Quantify the operational gap between actual and target utilization per department
* Flag departments exhibiting critical capacity shortfalls
* **Visualizations:** Benchmark vs. Actual comparison chart, capacity scorecard

#### 5. Dashboard Integration (Nafisa - Data Integration Lead)
* Assemble all Type B visualization outputs into unified multi-page Plotly Dash application
* Deliver **Page 4** (Bed Utilization & Workforce Efficiency) and **Page 5** (Resource Utilization & Capacity Benchmarks)

#### 6. GitHub Management & Documentation (Keerthi Machanooru - PR & GitHub Lead)
* Maintain GitHub folder hierarchy including milestone3/ directory
* Review, resolve merge conflicts, and merge pull requests
* Update repository documentation and compile the presentation

---

### 6. Repository milestone3/ Structure
```
milestone3/
|-- README.md
|-- data/
|   |-- processed/
|   `-- raw/
|-- notebook/
|   |-- Bed_Utilization_Occupancy_EDA.ipynb
|   |-- Bed_Utilization_Occupancy_Visualization.ipynb
|   |-- Department wise resource_utilization.ipynb
|   |-- Department_wise_resource_utilization_visualization.ipynb
|   |-- workforce_staffing_efficiency.ipynb
|   `-- workforce_staffing_efficiency_visualization.ipynb
|-- report/
|   |-- bed_utilization.html
|   |-- bed_utilization_occupancy_dashboard.html
|   |-- benchmark_capacity_gap.html
|   `-- department_resource_utilization.html
`-- outputs/
    `-- .gitkeep
```

---

### 7. How to Run the Complete Dashboard
```bash
git clone https://github.com/springboardmentor647/medical-operations-dashboard-team-a-batch1.git
cd medical-operations-dashboard-team-a-batch1
pip install dash plotly pandas numpy
python dashboard/app.py
```
Open http://localhost:8050 in your web browser to interact with all 5 dashboard pages.

---

### 8. Milestone 3 PR & Merge Workflow (Managed by @Keerthi Machanooru)
* **Sirivalli Reddyvari** (Sirivalli-Milestone-3 / PR #30) -> Bed Utilization Analysis [Merged]
* **Rushikesh** (feature/department-resource-utilization / PR #31) -> Department Resource Utilization [Merged]
* **Nafisa** (nafisa-milestone3-dashboard-integration / PR #32) -> Multi-Page Dashboard Integration Lead (Pages 4 & 5) [Merged]
* **Tanvi Ajit Bhosale** (Tanvii-08-milestone3 / PR #29 & PR #33) -> Bed Utilization Visualizations [Merged]
* **Sarthak Jejurkar** (Visualize-workforce-staffing-sarthak-jejurkar / PR #27) -> Workforce Staffing Visualizations [Merged]
* **Sowmitha A** (sowmitha-analyze-workforce-staffing-m3) -> Workforce Staffing Analysis
* **Abhi** (abhi-resource-utilization-analysis-m3) -> Resource Utilization Analysis
* **Divya Kumari** (divya-benchmark-capacity-analysis-m3) -> Benchmark & Capacity Gap Analysis
* **Keerthi Machanooru** -> Merge all PRs into main, maintain directory structure integrity, and update README.

---

### 9. Future Work
* Real-time Data Ingestion: Connect the dashboard to live Electronic Health Record (EHR) pipelines for continuous capacity tracking.
* Predictive Bed Forecasting: Implement machine learning models to forecast patient admissions and bed demand 7 to 14 days in advance.
* Automated Staffing Recommendations: Build dynamic nurse-to-patient and doctor scheduling optimization algorithms based on predicted admission surges.
* Early Warning Alert System: Configure automated email and SMS threshold alerts whenever department bed occupancy exceeds 85%.
* Cloud Deployment: Containerize the full 5-page Dash application using Docker and deploy to cloud services (AWS / Azure) for hospital-wide access.

---

### 10. Conclusion
Milestone 3 successfully delivers the Resource Utilization & Capacity Intelligence Module, completing the analytical foundation of the Healthcare Operations Intelligence Dashboard. By integrating hospital bed capacity benchmarks, doctor staffing records, and admissions data across departments, this module enables operational decision-makers to:
* Identify departments operating near or above critical capacity thresholds.
* Highlight staffing and workforce imbalances across specialized hospital departments.
* Measure and close operational capacity gaps against established healthcare benchmarks.
* Provide an interactive, unified 5-page decision analytics platform supporting data-driven clinical and operational management.

## Milestone 4 - Geographic Healthcare Intelligence & Executive Dashboard

### 1. Milestone 4 Overview & Objective

**Weeks 7-8 | Team of 10**

Milestone 4 focuses on Geographic Healthcare Intelligence & the Executive Dashboard - developing patient distribution mapping and healthcare service coverage mapping, integrating all prior modules (Data Integration, Patient Flow, Resource Utilization), and deploying the complete healthcare operations intelligence platform.

### 2. Data Notes - Geolocation Data Gap

**Facility Geocode Benchmark (`data/raw/facility_geocodes.csv`):**

- **Contents:** `department_id, department_name, latitude, longitude` (one row per facility/department)
- **Purpose:** Milestone 1's cleaned datasets do not include patient or facility latitude/longitude data. This benchmark geocoding lookup file makes the geographic visualizations analyzable.
- **Usage:** Joined against `admissions_clean.csv` on `department_id` to plot patient volume by location for Patient Distribution Mapping (BQ 1).

> **Important:** If patient-level addresses are not available, department/facility-level coordinates are an acceptable benchmark for mapping purposes - not measured patient-location data. This assumption is documented in `data/raw/GEOCODE_README.md`, the same way the bed- and staff-capacity gaps were documented in Milestone 3.

This file was pushed to the repo before Type B work began - **pull the latest main before starting.**

### 3. Team Assignments & Role Model (Milestone 4)

The team operates using the same two-role model as Milestones 2-3 (**Type A:** Data Analysis / Geo-EDA Prep and **Type B:** Visualization & Dashboard Build), plus three dedicated support roles - Dashboard Integration Lead, Deployment Lead, and Documentation & GitHub Lead:

| # | Team Member | Type | Task | Business Question / Area |
|---|---|---|---|---|
| 1 | Sowmitha A| Type A | Prepare & Analyze Patient Distribution Data | Patient Distribution Mapping |
| 2 | Tanvi Ajit Bhosale | Type B | Visualize Patient Distribution Map | Patient Distribution Mapping |
| 3 | Sirivalli Reddyvari | Type A | Analyze Healthcare Service Coverage | Healthcare Service Coverage Mapping |
| 4 | Keerthi Machanooru | Type B | Visualize Service Coverage Map + Filters | Healthcare Service Coverage Mapping |
| 5 | Deepika J | Type A | Design Executive Dashboard Layout | Executive Dashboard Design |
| 6 | Nafisa | Type B | Integrate Module 1 (Data Integration) Outputs | Centralized Dashboard Integration |
| 7 | Abhi | Type B | Integrate Module 2 & 3 (Patient Flow, Resource Utilization) Outputs | Centralized Dashboard Integration |
| 8 | Sarthak Jejurkar | Type B | Dashboard Integration Lead | All pages + QA/Testing |
| 9 | Rushikesh | Lead | Deployment Lead | Platform hosting/publishing |
| 10 | Divya Kumari | Lead | Documentation & GitHub Lead | README, PR merges, conflict resolution |

### 4. Business Question Pairings & Datasets

| Business Question | Type A (Analyst) | Type B (Visualizer) | Datasets Needed |
|---|---|---|---|
| Patient Distribution Mapping | Sowmitha | Tanu | admissions_clean.csv, departments_clean.csv, facility_geocodes.csv |
| Healthcare Service Coverage Mapping | Sirivalli Reddyvari | Keerthi Machanooru | departments_clean.csv, facility_geocodes.csv, doctors_preprocessed.csv |
| Executive Dashboard Design | Deepika J | - | Outputs from Milestones 1-3 (summary KPIs) |
| Module 1 Integration | - | Nafisa | Milestone 1 Data Integration outputs |
| Module 2 & 3 Integration | - | Abhi | Milestone 2 (Patient Flow) + Milestone 3 (Resource Utilization) outputs |
| Dashboard Integration & QA | - | Sarthak Jejurkar | All of the above (assembled) |
| Deployment | - | Rushikesh | Final assembled dashboard |
| Documentation & Repo Maintenance | - | Divya Kumari | All of the above (assembled) |

### 5. Detailed Task Breakdown

**1. Patient Distribution Mapping (Sowmitha A -> Tanvi Ajit Bhosale )**
- Join `facility_geocodes.csv` against `admissions_clean.csv` on `department_id`
- Calculate patient volume/density by location and by department
- Identify geographic clusters of high patient origin
- Visualization: patient distribution map (Folium/GeoPandas heatmap or density map)

**2. Healthcare Service Coverage Mapping (Sirivalli Reddyvari -> Keerthi Machanooru)**
- Determine facility catchment areas / service radius per department
- Identify areas that are over- or under-served relative to facility locations
- Visualization: service coverage map with interactive filters (by department, time period, service type)

**3. Executive Dashboard Design (Deepika J)**
- Design the executive dashboard layout/wireframe (Power BI or Plotly/Dash executive view)
- Define the KPI card format, color scheme, and navigation structure for the final platform

**4. Module Integration (Nafisa, Abhi)**
- Nafisa: Integrate Module 1 (Data Integration) outputs into the centralized dashboard
- Abhi: Integrate Module 2 (Patient Flow) and Module 3 (Resource Utilization) visualizations into the centralized dashboard

**5. Dashboard Integration & QA (Sarthak Jejurkar)**
- Integrate the geographic intelligence maps (from Tanu and Keerthi Machanooru) into the unified dashboard interface
- Assemble all Type B outputs into unified dashboard pages, ensuring consistent styling across pages
- Conduct end-to-end testing, performance/QA checks, and bug fixes across the integrated platform

**6. Deployment (Rushikesh)**
- Take the fully integrated dashboard from Sarthak Jejurkar and deploy/publish the complete healthcare operations intelligence platform
- Verify the live/deployed version matches the tested build - no broken links, missing assets, or config issues
- Hand off deployment details (URL, hosting notes) to the Documentation Lead

**7. Documentation & GitHub Management (Divya Kumari)**
- Update GitHub README with Milestone 4 structure, run instructions, and data-gap notes (geocoding)
- Maintain repository folder hierarchy, review open pull requests, resolve merge conflicts, and merge all outstanding branches into main

### 6. How to Run the Complete Dashboard

```bash
git clone https://github.com/springboardmentor647/medical-operations-dashboard-team-a-batch1.git
cd medical-operations-dashboard-team-a-batch1
git checkout main && git pull origin main
pip install dash plotly pandas numpy folium geopandas
python dashboard/app.py
```

Open `http://localhost:8050` in your web browser to interact with all dashboard pages, including the new Patient Distribution and Service Coverage maps.

### 7. Milestone 4 PR & Merge Workflow (Managed by @Divya Kumari)

As of September 11, 2026, all Milestone pull requests have been reviewed, conflicts resolved, and merged into main by Divya Kumari:

- **Sirivalli Reddyvari:** (Sirivalli-Milestone-4 / PR #34) -> Healthcare Service Coverage Analysis [Merged]
- **Nafisa:** (nafisa-milestone4-module1-integration / PR #35) -> Module 1 (Data Integration) Dashboard Integration [Merged]
- **Tanvi Ajit Bhosale:** (Tanvii-08--milestone4-Patient-Distribution-Map / PR #36) -> Patient Distribution Map Visualization [Merged]
- **Sarthak Jejurkar:** (milestone4-dashboard-integration-sarthak-jejurkar / PR #37) -> Dashboard Integration Lead (All Pages + QA) [Merged]
- **Abhi:** (abhimilestone_4 / PR #38) -> Module 2 & 3 Dashboard Integration [Merged]
- **Rushikesh:** (milestone4-deployment-rushikesh / PR #39) -> Deployment [Merged]
- **Keerthi Machanooru:** (visualize-service-coverage-map-filters / PR #40) -> Service Coverage Map Visualization + Filters [Merged]
- **Tanvi Ajit Bhosale:** (Tanvi / PR #41) -> Patient Distribution Map, follow-up fix [Merged]
- **Divya Kumari:** Reviewed and resolved merge conflicts across all branches, merged PRs #34-#41 into main, fixed the milestone4/ directory structure (fix milestone4 directory commit), added Dash server variables/attributes for deployment support, and maintained the README.

### 8. Future Work

- **Patient-level Geocoding:** Replace department-level benchmark coordinates with actual patient address geocoding once privacy-compliant location data is available.
- **Real-time Data Ingestion:** Connect the dashboard to live Electronic Health Record (EHR) pipelines for continuous geographic and capacity tracking.
- **Predictive Coverage Modeling:** Use predictive analytics to forecast underserved areas as patient demand shifts over time.
- **Role-based Access Control:** Add authentication so executives, department heads, and analysts see tailored dashboard views.
- **Cloud Deployment Hardening:** Move the deployed platform to a managed cloud service (AWS / Azure) with CI/CD and monitoring.

### 9. Conclusion

Milestone 4 delivers the Geographic Healthcare Intelligence & Executive Dashboard module, completing the full Healthcare Operations Intelligence Dashboard. By mapping patient distribution and healthcare service coverage against facility geocode benchmarks, and integrating every prior module (Data Integration, Patient Flow, Resource Utilization) into a single deployed platform, this milestone enables hospital management to:

- Visualize where patients are coming from and identify high-density geographic clusters.
- Identify over- and under-served areas relative to existing facility locations.
- Navigate a single, unified executive dashboard covering data integration, patient flow, resource utilization, and geographic coverage.
- Access the fully deployed, end-to-end healthcare operations intelligence platform.

## Quick Start

1. Open the live app: https://medical-operations-dashboard-team-a-h6ai.onrender.com/
2. Use the sidebar to navigate between pages — Executive Overview, Patient Flow, Discharge & Treatment, Bottlenecks & Surgery, Bed & Workforce, Resources & Benchmarks, Patient Distribution, Service Coverage, and Data Integration
3. No setup or file upload needed — all datasets are pre-loaded and the dashboard computes live from them
