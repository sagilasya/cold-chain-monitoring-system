
def check_temperature(temp, min_temp, max_temp):
    if min_temp <= temp <= max_temp:
        return "SAFE"
    return "ALERT"

def risk_score(temp, min_temp, max_temp):
    if min_temp <= temp <= max_temp:
        return 0

    deviation = min(
        abs(temp - min_temp),
        abs(temp - max_temp)
    )

    return min(deviation * 20, 100)