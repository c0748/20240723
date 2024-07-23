import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

df = pd.read_csv("data/cases_cumulative_daily (1).csv", encoding="utf-8")

date = "2021/5/10"

df_with_date = df[df["Date"] == date]


# print (df_with_date)

if df_with_date.empty:
    print("データが空っぽです")

else:
    date_data = df_with_date.drop(columns=["Date", "ALL"]).iloc[0]
    print(date_data)

    date_data_sorted = date_data.sort_values(ascending=False)
    print(date_data_sorted)

    colors = ["red" if prefecture == "Iwate" else "skyblue" for prefecture in date_data_sorted.index]

    plt.figure(figsize=(12, 8))
    plt.bar(date_data_sorted.index, date_data_sorted.values, color=colors)
    plt.xlabel("感染者数")
    plt.title(f"都道府県別感染者数{date}")
    plt.xticks(rotation=90)
    plt.show()
