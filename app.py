from products import products
from analytics import check_temperature, risk_score

sample_data = [
    ("COVID-19 Vaccine", 6),
    ("Milk", 5),
    ("Frozen Fish", -17)
]

print("COLD CHAIN MONITORING REPORT")
print("-" * 50)

for product, temp in sample_data:

    min_temp, max_temp = products[product]

    status = check_temperature(temp, min_temp, max_temp)
    risk = risk_score(temp, min_temp, max_temp)

    print(f"Product: {product}")
    print(f"Temperature: {temp}°C")
    print(f"Status: {status}")
    print(f"Risk Score: {risk}%")

    # AI Alert
    if status == "ALERT":
        print(f"⚠ AI Warning: {product} may spoil if temperature continues.")

    print("-" * 50)