import pandas as pd
import random

data = []

for i in range(500):
    vehicles = random.randint(10, 200)
    time = random.randint(0, 23)        # hour of day
    weather = random.randint(0, 2)      # 0=sunny,1=rainy,2=foggy
    road_type = random.randint(0, 2)    # 0=local,1=highway,2=city

    density = vehicles * 0.5 + weather * 10 + road_type * 15 + random.randint(-10, 10)

    data.append([vehicles, time, weather, road_type, density])

df = pd.DataFrame(
    data,
    columns=["vehicles", "time", "weather", "road_type", "density"]
)

df.to_csv("traffic.csv", index=False)
print("✅ traffic.csv generated successfully")
