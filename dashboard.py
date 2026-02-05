import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Hydraulic Cylinder AI Dashboard", layout="wide")

st.title("🔧 Hydraulic Cylinder AI Monitoring Dashboard")

@st.cache_data
def load_data():
    return pd.read_csv("data/health_results.csv")

try:
    df = load_data()
except:
    st.error("❌ No data found. Run preprocessing and models first.")
    st.stop()

st.subheader("📊 Sensor Data Preview")
st.dataframe(df.head())

st.subheader("📈 Pressure & Position Over Time")
fig, ax = plt.subplots()
ax.plot(df["time"], df["pressure"], label="Pressure")
ax.plot(df["time"], df["position"], label="Position")
ax.legend()
st.pyplot(fig)

st.subheader("🚨 Anomaly Detection")
fig2, ax2 = plt.subplots()
ax2.plot(df["time"], df["anomaly"], label="Anomaly (1=Normal, -1=Fault)")
ax2.legend()
st.pyplot(fig2)

st.subheader("❤️ Health Index Over Time")
fig3, ax3 = plt.subplots()
ax3.plot(df["time"], df["health_score"], label="Health Score")
ax3.set_ylim(0, 1)
ax3.legend()
st.pyplot(fig3)
