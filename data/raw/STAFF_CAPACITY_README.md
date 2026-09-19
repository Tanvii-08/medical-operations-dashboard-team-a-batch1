# Staff Capacity Dataset — Data Source Note

## What this is
`staff_capacity.csv` provides a **defined benchmark** of total nursing/support staff per
department, used to enable full Workforce & Staffing Efficiency analysis in Milestone 3.

## Why it exists
Your mentor's notes list **beds, doctors, staff, and departments** as the four resource
categories to analyze. Milestone 1's cleaned datasets only include `doctors_preprocessed.csv`
— there is no separate nursing/support-staff dataset. Without a staff-count figure, workforce
analysis would be limited to doctors only, which is narrower than what "staffing efficiency"
implies.

## Important: this is an assumed benchmark, not extracted hospital data
Staff counts were **defined by the team**, scaled roughly in proportion to each department's
bed capacity (`bed_capacity.csv`) and adjusted for patient-facing intensity — e.g., Emergency
and ICU carry more staff than Dermatology or Dental. These are **not** real staffing figures
pulled from the original dataset, since no such data was collected in Milestone 1.

## How it should be used
- Join on `department_id` against `admissions_clean.csv` and `doctors_preprocessed.csv` to
  calculate combined workforce metrics — e.g., patients per staff member, doctor-to-support-staff
  ratio, department-level staffing efficiency.
- Treat `Total_Staff` as a **benchmark headcount**, not a real measured value.
- If your mentor or evaluator asks about this dataset, be upfront: it was defined by the team
  to make full Workforce & Staffing Efficiency analysis possible, since the source data only
  included doctors.

## Columns
| Column | Description |
|---|---|
| `department_id` | Matches `departments_clean.csv` |
| `department_name` | Matches `departments_clean.csv` |
| `Total_Staff` | Assumed/benchmark nursing & support staff headcount for the department |

## Related file
See also `bed_capacity.csv` and `BED_CAPACITY_README.md` — same rationale, same approach,
covering the equivalent gap for bed-capacity data.
