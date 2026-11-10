def cluster_levels(pivots, tolerance):
    clusters = []
    for p in sorted(pivots, key=lambda x: x["price"]):
        match = next((c for c in clusters if abs(p["price"] - c["mean"]) <= tolerance), None)
        if match:
            match["prices"].append(p["price"])
            match["indices"].append(p["index"])
            match["mean"] = sum(match["prices"]) / len(match["prices"])
        else:
            clusters.append({"prices": [p["price"]], "indices": [p["index"]], "mean": p["price"]})
    return clusters

def build_zones(highs, lows, tolerance, current_price):
    zones = []
    for kind, pivots in (("resistance", highs), ("support", lows)):
        for c in cluster_levels(pivots, tolerance):
            zones.append({"kind": kind, "low": min(c["prices"])-tolerance/2, "high": max(c["prices"])+tolerance/2,
                          "mid": c["mean"], "touches": len(c["prices"]),
                          "distance": abs(c["mean"]-current_price)})
    return sorted(zones, key=lambda z: z["distance"])
