# app.py
import streamlit as st
from route_mode import show_route_mode
from location_mode import show_location_mode

st.set_page_config(layout="wide", page_title="GNSS SmartNav")

st.markdown("## 🛰️ GNSS SmartNav – Outage-Aware Navigation")
mode = st.radio("Select Mode", ["📍 Location Outage", "🛣️ Route Outage"], horizontal=True)

if mode == "📍 Location Outage":
    show_location_mode()
elif mode == "🛣️ Route Outage":
    show_route_mode()
