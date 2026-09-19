# Bed Capacity Dataset — Data Source Note

## What this is
`bed_capacity.csv` provides a **defined benchmark** of total bed capacity per department, used
to enable Milestone 3's Bed Utilization & Occupancy analysis.

## Why it exists
Milestone 1's cleaned datasets (`departments_clean.csv`, `admissions_clean.csv`, etc.) do not
include any bed-count or facility-capacity data. Without a capacity figure, no occupancy rate,
utilization percentage, or capacity-gap analysis is possible. This file fills that gap.

## Important: this is an assumed benchmark, not extracted hospital data
Bed counts were **defined by the team** based on typical relative sizing patterns across hospital
departments (e.g., Emergency and ICU carry more beds than Dermatology or Dental), to enable
realistic KPI calculations for Milestone 3. These are **not** real bed-count figures pulled from
the original dataset, since no such data was collected in Milestone 1.

## How it should be used
- Join on `department_id` against `admissions_clean.csv` to calculate admissions per department
  relative to `Total_Beds`, giving an occupancy/utilization rate.
- Treat `Total_Beds` as the **target/benchmark capacity** for gap analysis (Business Question 4),
  not as ground truth.
- If your mentor or evaluator asks about this dataset, be upfront: it was defined by the team to
  make the Bed Utilization business question analyzable, since the source data didn't include it.

## Columns
| Column | Description |
|---|---|
| `department_id` | Matches `departments_clean.csv` |
| `department_name` | Matches `departments_clean.csv` |
| `Total_Beds` | Assumed/benchmark bed capacity for the department |
