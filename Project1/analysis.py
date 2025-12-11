import pandas as pd
import matplotlib.pyplot as plt
data = {"day": [1, 2, 3, 4, 5, 6, 7], "sales": [120, 150, 90, 200, 170, 100, 250]}
df = pd.DataFrame(data)
print(df)

print("Max sales:", df["sales"].max())
print("Min sales:", df["sales"].min())
print("average sales:", df["sales"].mean())
print("Total:", df["sales"].sum())

plt.plot(df["day"], df["sales"])
plt.xlabel("day")
plt.ylabel("sales")
plt.title("Daily Sales")
plt.grid(True)


plt.savefig("sales_chart.png")