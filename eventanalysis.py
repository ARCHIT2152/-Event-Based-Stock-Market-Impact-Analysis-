import pandas as pd

df = pd.read_csv("data/nifty50.csv")
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)

df = df.rename(columns={"Price": "Close"})

df["Close"] = (
    df["Close"]
    .astype(str)
    .str.replace(",", "")
    .astype(float)
)

df = df.sort_values("Date").reset_index(drop=True)

diwali_date = pd.to_datetime("2023-11-12")

before_start = diwali_date - pd.Timedelta(days=30)
after_end = diwali_date + pd.Timedelta(days=30)

before_event = df[
    (df["Date"] >= before_start) &
    (df["Date"] < diwali_date)
]

after_event = df[
    (df["Date"] > diwali_date) &
    (df["Date"] <= after_end)
]

before_avg = before_event["Close"].mean()
after_avg = after_event["Close"].mean()

impact_return = ((after_avg - before_avg) / before_avg) * 100

if impact_return > 0:
    impact = "Positive"
elif impact_return < 0:
    impact = "Negative"
else:
    impact = "Neutral"
print("Event: Diwali 2023")
print(f"Average Close BEFORE event: {before_avg:.2f}")
print(f"Average Close AFTER event: {after_avg:.2f}")
print(f"Impact Return: {impact_return:.2f}%")
print(f"Overall Impact: {impact}")
