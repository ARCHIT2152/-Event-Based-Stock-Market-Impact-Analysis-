# -Event-Based-Stock-Market-Impact-Analysis-
# Event-Based Stock Market Impact Analysis 📈

This project analyzes the **impact of a major event (Diwali 2023)** on the Indian stock market using historical **NIFTY 50 index data**.  
It compares the average closing prices **before and after the event** to determine whether the event had a **positive, negative, or neutral impact** on market performance.

---

## 📌 Project Objective

The goal of this project is to:
- Study how **major festivals or events** affect stock market behavior
- Apply **data analysis concepts using Python and Pandas**
- Build a foundation for **event-driven financial analysis**

This project does **not use machine learning**, instead it focuses on **statistical and logical analysis**, which is ideal for beginners.

---

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **CSV data processing**
- **Datetime & TimeDelta operations**

---

## 📂 Dataset

- **File:** `nifty50.csv`
- **Columns used:**
  - `Date`
  - `Price` (renamed to `Close` in code)

The dataset contains historical closing prices of the **NIFTY 50 index**.

---

## ⚙️ How the Analysis Works

1. Load the CSV file containing NIFTY 50 data  
2. Convert the `Date` column into a proper datetime format  
3. Clean the price column (remove commas, convert to float)  
4. Sort data chronologically  
5. Define the event date (**Diwali – 12 Nov 2023**)  
6. Create two time windows:
   - **30 days before the event**
   - **30 days after the event**
7. Calculate:
   - Average closing price before the event
   - Average closing price after the event
8. Compute **impact return percentage**
9. Classify the event impact as:
   - **Positive**
   - **Negative**
   - **Neutral**

---

## 📊 Impact Return Formula

```text
Impact Return (%) =
((Average After Event - Average Before Event) / Average Before Event) × 100
