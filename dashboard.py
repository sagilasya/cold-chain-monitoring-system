import streamlit as st
import pandas as pd

st.set_page_config(page_title="Cold Chain Monitoring", layout="wide")

st.title("🌡️ Cold Chain Monitoring System")

# Top Metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Products", 10)

with col2:
    st.metric("Safe Products", 7)

with col3:
    st.metric("Alert Products", 3)

# Product Status Table
st.subheader("Live Product Status")

data = {
    "Product": [
        "COVID-19 Vaccine",
        "Milk",
        "Frozen Fish"
    ],
    "Temperature": [6, 5, -17],
    "Status": [
        "SAFE",
        "ALERT",
        "ALERT"
    ]
}

df = pd.DataFrame(data)

st.dataframe(df)

# AI Alerts
st.subheader("AI Alerts")

for _, row in df.iterrows():
    if row["Status"] == "ALERT":
        st.warning(
            f"{row['Product']} is outside the safe temperature range!"
        )

# Temperature Graph
st.subheader("Temperature Trends")

graph_data = pd.read_csv("data.csv")

milk = graph_data[graph_data["Product"] == "Milk"]

st.line_chart(
    milk.set_index("Time")["Temperature"]
)