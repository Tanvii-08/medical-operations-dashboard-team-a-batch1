# Facility Geocoding Benchmark Assumption

## Purpose
`facility_geocodes.csv` provides department/facility-level latitude and
longitude values for Milestone 4 geographic analysis.

## Important assumption
The original project datasets do not contain measured patient or facility
latitude/longitude values. Therefore, these coordinates are **synthetic
benchmark mapping points** created for this project.

They are used only to demonstrate geographic visualization and service
coverage analysis. They must **not** be interpreted as actual patient
locations or verified hospital/facility addresses.

## Columns
- `department_id` - department identifier from `departments_clean.csv`
- `department_name` - department name from `departments_clean.csv`
- `latitude` - benchmark latitude
- `longitude` - benchmark longitude

## Join key
The file is designed to join with the department data using:
`department_id`.

## Data quality checks
- One row per department.
- Department IDs are unique.
- Latitude and longitude are numeric and non-null.
