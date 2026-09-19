# Milestone 3 - Resource Utilization & Capacity Intelligence Module

Weeks 5-6 | Team of 10

## Business Questions & Team Roles

| # | Business Question | Analyst (Type A) | Visualizer (Type B) | Datasets Needed |
|---|---|---|---|---|
| 1 | Bed Utilization & Occupancy | Sirivalli Reddyvari | Tanvi Ajit Bhosale | admissions_clean.csv, departments_clean.csv, bed_capacity.csv |
| 2 | Workforce & Staffing Efficiency | Sowmitha A | Sarthak Jejurkar | admissions_clean.csv, doctors_preprocessed.csv, staff_capacity.csv |
| 3 | Department Resource Utilization | Abhi | Rushikesh | admissions_clean.csv, departments_clean.csv, doctors_preprocessed.csv |
| 4 | Benchmark & Capacity Gap Analysis | Divya Kumari | Deepika J | admissions_clean.csv, bed_capacity.csv, doctors_preprocessed.csv |

## Leadership

* **Nafisa** - Data Integration Lead (Dashboard Pages 4 & 5)
* * **Keerthi Machanooru** - Documentation & GitHub Lead (PR Merges & Structure)
 
  * ## Directory Structure
 
  * ```
    milestone3/
    |-- README.md
    |-- analysis/
    |   |-- sowmitha_workforce_staffing_analysis.ipynb
    |   |-- sirivalli_bed_utilization_analysis.ipynb
    |   |-- abhi_resource_utilization_analysis.ipynb
    |   `-- divya_benchmark_capacity_analysis.ipynb
    |-- visualizations/
    |   |-- tanvi_bed_utilization_visualization.ipynb
    |   |-- sarthak_workforce_staffing_visualization.ipynb
    |   |-- rushikesh_resource_utilization_visualization.ipynb
    |   `-- deepika_benchmark_capacity_visualization.ipynb
    |-- data_integration/
    |   `-- nafisa_milestone3_data_integration.ipynb
    `-- outputs/
        `-- .gitkeep
    ```

    ## How to Run Dashboard

    ```bash
    python dashboard/app.py
    ```

    Visit http://localhost:8050 to access all 5 pages.
    
