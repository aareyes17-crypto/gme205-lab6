class OutputManager:
    def __init__(self):
        self.results = []

    def display_results(self, results):
        print("\n=== PARCEL DESCRIPTIONS ===")
        for r in results:
            print(r)

    def export_geojson(self, parcels):
        print("\n=== EXPORTING GEOJSON ===")
        geojson_data = []

        for p in parcels:
            geojson_data.append({
                "id": p.parcel_id,
                "geometry": p.geometry
            })

        print("Export complete.")
        return geojson_data

    def generate_report(self, overlap_dict):
        print("\n=== OVERLAP REPORT ===")
        for parcel_id, overlaps in overlap_dict.items():
            print(f"{parcel_id} overlaps with: {overlaps}")