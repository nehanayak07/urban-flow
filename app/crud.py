def calculate_congestion(vehicle_count: int, avg_speed: float) -> str:
    if vehicle_count > 100 and avg_speed < 20:
        return "High"
    elif vehicle_count > 50:
        return "Medium"
    return "Low"
