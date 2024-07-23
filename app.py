import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

df = pd.read_csv("data/cases_cumulative_daily (1).csv", encoding="utf-8")
df["Date"] = pd.to_datetime(df["Date"])


plt.figure(figsize=(9, 4))

plt.plot(df["Date"], df["ALL"], label="ALL", color="y")
plt.plot(df["Date"], df["Hokkaido"], label="Hokkaido", color="g")
plt.plot(df["Date"], df["Gifu"], label="Gifu", color="b")
plt.plot(df["Date"], df["Okinawa"], label="Okinawa", color="c")
plt.title("北海道・岐阜・沖縄-コロナ感染者数")

plt.xlabel("日付")
plt.ylabel("感染者数")

plt.grid(True)
plt.xticks(rotation=45)

plt.legend()
plt.show()
