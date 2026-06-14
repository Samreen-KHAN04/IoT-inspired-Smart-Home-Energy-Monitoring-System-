import pandas as pd
import random
import time
from datetime import datetime, timedelta

CSV_FILE = "data/energy_log.csv"

RATE_PER_KWH = 8

appliances = {
    "Fan": 75,
    "TV": 120,
    "Laptop": 90,
    "AC": 1500,
    "Refrigerator": 300
}

records = []

current_time = datetime.now() - timedelta(hours=24)

for i in range(500):

    appliance = random.choice(list(appliances.keys()))

    voltage = random.randint(220, 240)

    power = appliances[appliance]

    current = round(power / voltage, 2)

    energy = round(power / 1000, 3)

    cost = round(energy * RATE_PER_KWH, 2)

    alert = "HIGH_USAGE" if power > 1000 else "NORMAL"

    records.append({
        "Timestamp": current_time,
        "Appliance": appliance,
        "Voltage": voltage,
        "Current": current,
        "Power": power,
        "Energy_kWh": energy,
        "Cost": cost,
        "Alert": alert
    })

    current_time += timedelta(minutes=3)

df = pd.DataFrame(records)

df.to_csv(CSV_FILE, index=False)

print("Generated 24 Hours Energy Data")