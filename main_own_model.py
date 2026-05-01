from own_model.parcel import Parcel
from own_model.output_manager import OutputManager


def main():
    # ---------------------------------------------------------
    # 1. Simulated GeoJSON input
    # ---------------------------------------------------------
    geojson_data = [
        {"id": "P1", "owner": "Alice", "geometry": {"x": 10, "y": 10}},
        {"id": "P2", "owner": "Bob", "geometry": {"x": 12, "y": 12}},
        {"id": "P3", "owner": "Charlie", "geometry": {"x": 30, "y": 30}},
    ]

    # ---------------------------------------------------------
    # 2. Load parcels (UML: load_from_geojson)
    # ---------------------------------------------------------
    parcels = Parcel.load_from_geojson(geojson_data)

    # ---------------------------------------------------------
    # 3. Compute area
    # ---------------------------------------------------------
    print("\n=== PARCEL AREAS ===")
    for p in parcels:
        print(f"{p.parcel_id}: {p.compute_area()} sqm")

    # ---------------------------------------------------------
    # 4. Detect overlaps (UML: detect_overlap)
    # ---------------------------------------------------------
    overlap_results = {}
    for p in parcels:
        overlap_results[p.parcel_id] = p.detect_overlap(parcels)

    # ---------------------------------------------------------
    # 5. Output using OutputManager
    # ---------------------------------------------------------
    output = OutputManager()

    output.display_results([p.describe() for p in parcels])
    output.generate_report(overlap_results)

    geojson_output = output.export_geojson(parcels)
    print("\nExported Data:", geojson_output)


if __name__ == "__main__":
    main()