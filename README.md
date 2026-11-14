# FIRECHRONICLE
### Harmonizing MODIS and VIIRS Satellite Observations for Long-Term Global Fire Activity Analysis

**NASA International Space Apps Challenge 2026**

**Challenge:** MODIS and VIIRS Hotspots Harmonization

**Project Status:** Under Active Development

---

## 1. Project Overview

FIRECHRONICLE is a scientific data analysis and visualization project designed to improve the temporal consistency and interpretability of global satellite-based fire activity observations.

The project focuses on harmonizing active fire detections from NASA's Moderate Resolution Imaging Spectroradiometer (MODIS) and Visible Infrared Imaging Radiometer Suite (VIIRS).

Although both instruments detect thermal anomalies associated with fire activity, differences in spatial resolution, detection sensitivity, satellite overpass times, and observation conditions make direct comparisons of their raw detection counts scientifically unreliable.

FIRECHRONICLE aims to address these differences through a reproducible data processing, harmonization, and validation framework, supported by an interactive global web application.

## 2. The Scientific Problem

MODIS provides a long historical record of active fire observations, while VIIRS offers more recent observations with finer spatial resolution.

Combining these datasets without accounting for sensor differences can introduce artificial changes into long-term fire activity trends.

**Our central research question is:**

*How can MODIS and VIIRS active fire observations be harmonized to produce a more consistent and scientifically interpretable global fire activity time series?*

## 3. Project Objectives

FIRECHRONICLE aims to:

1. Collect and process historical MODIS and VIIRS active fire observations.
2. Standardize relevant data fields while preserving sensor-specific information.
3. Align observations using common spatial and temporal aggregation methods.
4. Investigate differences in sensor detection behavior during overlapping observation periods.
5. Develop and evaluate a harmonization approach for long-term fire activity analysis.
6. Analyze global temporal trends, seasonal patterns, and unusual fire activity.
7. Build an interactive web application for exploring and exporting results.
8. Document methodological limitations, uncertainty, and validation results.

## 4. Data Sources

### NASA Fire Information for Resource Management System (FIRMS)

Primary data will be obtained from NASA FIRMS.

**MODIS**
- Terra and Aqua satellite observations, where available
- MODIS Collection 6.1 active fire products
- Long-term historical fire activity records

**VIIRS**
- Suomi National Polar-orbiting Partnership (S-NPP)
- NOAA-20
- NOAA-21
- VIIRS active fire products, with product versions documented in the data inventory

### Relevant Data Attributes

- Geographic coordinates: latitude and longitude
- Acquisition date and time
- Satellite and instrument identifiers
- Detection confidence
- Fire Radiative Power (FRP)
- Day/night classification
- Thermal anomaly classification, where available

**Official data source:** https://firms.modaps.eosdis.nasa.gov/

## 5. Proposed Scientific Methodology

### Stage 1 — Data Acquisition and Quality Assessment

Download historical MODIS and VIIRS observations from NASA FIRMS.

Inspect data completeness, coordinate validity, temporal coverage, product versions, and sensor-specific quality indicators.

Preserve original source files and record all processing decisions.

### Stage 2 — Data Standardization

Convert source datasets into a common analytical schema while preserving relevant sensor-specific attributes.

Avoid treating MODIS and VIIRS confidence categories or detection measurements as directly equivalent.

### Stage 3 — Spatial and Temporal Alignment

Aggregate observations into common spatial units and temporal intervals.

Investigate the effects of spatial resolution, satellite observation schedules, and repeated detections.

### Stage 4 — Sensor Harmonization

Analyze MODIS–VIIRS differences during overlapping observation periods.

Develop candidate calibration methods and evaluate their suitability for producing a consistent fire activity indicator.

Avoid assuming that raw hotspot counts represent the number of distinct fires.

### Stage 5 — Validation and Uncertainty Assessment

Evaluate harmonization performance using observations not used for model fitting.

Assess sensitivity to spatial resolution, temporal aggregation, geographic region, and methodological assumptions.

Document limitations and uncertainty.

### Stage 6 — Global Fire Activity Analysis

Investigate:

- Long-term temporal patterns
- Seasonal fire activity
- Regional differences
- Fire activity anomalies
- Fire Radiative Power distributions

### Stage 7 — Interactive Web Application

Develop an interactive platform featuring:

- Global fire activity visualization
- Geographic and temporal filtering
- Historical time series
- Seasonal analysis
- Anomaly exploration
- Sensor comparisons
- Downloadable analytical results

## 6. Planned Technology Stack

| Component | Technology |
|---|---|
| Programming | Python |
| Data processing | Pandas, NumPy, DuckDB |
| Data storage | CSV, Parquet |
| Geospatial analysis | GeoPandas and geospatial grid methods |
| Statistical analysis | SciPy, scikit-learn |
| Visualization | Plotly |
| Web application | Streamlit |
| Development | Google Colab, GitHub |

The technology stack may be adjusted as implementation requirements evolve.

## 7. Scientific Integrity

FIRECHRONICLE follows several principles:

- A satellite hotspot detection is not necessarily a unique wildfire.
- Raw MODIS and VIIRS detection counts are not directly interchangeable.
- Sensor-specific characteristics must be considered during harmonization.
- Historical observations and modeled estimates must be distinguishable.
- Uncertainty and methodological limitations must be reported.
- The application is intended for historical analysis and scientific exploration, not as a validated operational fire prediction or emergency warning system.

## 8. Development Roadmap

- [ ] Acquire and inventory NASA FIRMS datasets
- [ ] Implement data quality assessment
- [ ] Standardize MODIS and VIIRS observations
- [ ] Build a common spatial-temporal analysis framework
- [ ] Develop candidate harmonization methods
- [ ] Validate harmonized results
- [ ] Implement global fire activity analyses
- [ ] Develop the interactive web application
- [ ] Complete documentation and testing
- [ ] Prepare the final hackathon submission

## 9. Data Availability and Reproducibility

The project will provide source references, processing code, methodological documentation, and reproducible analytical workflows.

Large raw satellite datasets may be stored outside the GitHub repository. Download instructions and source metadata will be documented.

## 10. References

1. NASA Fire Information for Resource Management System (FIRMS). https://firms.modaps.eosdis.nasa.gov/
2. NASA FIRMS Archive Download. https://firms.modaps.eosdis.nasa.gov/download/
3. NASA FIRMS API Documentation. https://firms.modaps.eosdis.nasa.gov/api/

Additional scientific references and product documentation will be added during development.

---

**FIRECHRONICLE — Making long-term satellite fire observations more comparable, interpretable, and accessible.**

### AI-Assisted Development

Generative AI tools were used to support documentation drafting, programming assistance, and technical explanations during development.

The project team is responsible for reviewing the generated material, making methodological decisions, testing the implementation, and validating the scientific results.
