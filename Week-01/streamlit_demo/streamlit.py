import streamlit as st
import pandas as pd
import os
from datetime import date

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(page_title="Personal Finance Tracker", layout="centered")

st.title("💰 Personal Finance Tracker")
st.write("Track your income and expenses easily using Streamlit.")

# ----------------------------
# Data File Setup
# ----------------------------
DATA_FILE = "data.csv"

if not os.path.exists(DATA_FILE):
    df = pd.DataFrame(columns=["date", "description", "amount", "category", "type"])
    df.to_csv(DATA_FILE, index=False)

df = pd.read_csv(DATA_FILE)

# ----------------------------
# Add New Transaction Form
# ----------------------------
st.subheader("➕ Add New Transaction")

with st.form("transaction_form"):
    t_date = st.date_input("Date", value=date.today())
    description = st.text_input("Description")
    amount = st.number_input("Amount", min_value=0.0, step=1.0)
    category = st.selectbox(
        "Category",
        ["Food", "Rent", "Transport", "Shopping", "Salary", "Entertainment", "Other"]
    )
    t_type = st.radio("Type", ["Income", "Expense"])

    submitted = st.form_submit_button("Add Transaction")

    if submitted:
        new_data = {
            "date": t_date,
            "description": description,
            "amount": amount,
            "category": category,
            "type": t_type
        }

        df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
        df.to_csv(DATA_FILE, index=False)
        st.success("✅ Transaction added successfully!")

# Reload data after adding
df = pd.read_csv(DATA_FILE)

# ----------------------------
# Summary Section
# ----------------------------
st.subheader("📌 Summary")

income = df[df["type"] == "Income"]["amount"].sum()
expense = df[df["type"] == "Expense"]["amount"].sum()
balance = income - expense

col1, col2, col3 = st.columns(3)
col1.metric("Total Income", f"₹ {income:.2f}")
col2.metric("Total Expense", f"₹ {expense:.2f}")
col3.metric("Balance", f"₹ {balance:.2f}")

# ----------------------------
# Expense by Category (Streamlit Chart)
# ----------------------------
st.subheader("📉 Expense by Category")

expense_df = df[df["type"] == "Expense"]

if not expense_df.empty:
    category_sum = expense_df.groupby("category")["amount"].sum()
    st.bar_chart(category_sum)
else:
    st.info("No expense data available to show chart.")

# ----------------------------
# Show All Transactions
# ----------------------------
st.subheader("📄 All Transactions")
st.dataframe(df)

# ----------------------------
# Reset Data Option
# ----------------------------
st.subheader("🗑 Reset Data")

if st.button("Delete All Transactions"):
    df = pd.DataFrame(columns=["date", "description", "amount", "category", "type"])
    df.to_csv(DATA_FILE, index=False)
    st.warning("All transactions deleted. Please refresh the page.")
