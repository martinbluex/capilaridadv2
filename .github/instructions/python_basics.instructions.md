---
applyTo: '**/*.py'
---
# Geospatial Logistics Analytics Guidelines

Expert Python geospatial analyst for logistics coverage analysis.

## Critical Geospatial Rules
- **CRS:** EPSG:4326 for storage, EPSG:32719 for calculations. Always verify before area/distance ops.
- **Geometry Column:** Use `.geometry.name` (never hardcode 'geometry' or 'SHAPE').
- **Coverage:** 800m buffer for PUDO walking distance. Use `gpd.overlay()` for intersections.
- **Performance:** Group by comuna before processing 200k+ features.
- **Text Normalization:** `unicodedata.normalize()` for spatial joins (remove accents, uppercase).

## Domain Specifics
- **Rural Definition:** `ID_ENTIDAD == 0` in Chilean Census data.
- **Población:** Integer for counts, round percentages to 1-2 decimals.
- **Naming:** Use Census schema (COMUNA, ENTIDAD, MANZENT, TOTAL_PERS, etc.).
- **Parquet:** Use `pyarrow` engine, handle WKB geometries with `shapely.wkb.loads()`.

## Folium Maps
- **HeatMaps:** Use `np.log10()` scaling for population to show magnitude differences.
- **Colors:** Red=uncovered, Green=covered, Blue=infrastructure. Add HTML legends.
- **Markers:** `MarkerCluster` for 100+ points. Include score breakdowns in popups.
- **Performance:** Filter zero-population areas, limit to top N results.

## Jupyter Notebooks
- **Structure:** Add markdown cells before sections with headers, data sources, business logic.
- **Sections:** Use `# ========== STEP N: TITLE ==========` in code cells.
- **Progress:** Print status for long operations ("Processing 20/346...").
- **Memory:** Process in chunks, use `.copy()` explicitly, delete large objects.
- **Outputs:** Save after each major step with descriptive filenames.

## Code Modifications
- **Minimal Changes:** Edit only affected lines, preserve structure.
- **Debug First:** Print diagnostics (columns, unique values, dtypes) before fixing.
- **Validate:** Print summary stats after spatial operations.