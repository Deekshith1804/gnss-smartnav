import streamlit as st
from streamlit_javascript import st_javascript

def get_user_location():
    result = st_javascript("""
    navigator.geolocation.getCurrentPosition(
        (loc) => {
            const coords = loc.coords.latitude + "," + loc.coords.longitude;
            window.parent.postMessage({type: "streamlit:setComponentValue", value: coords}, "*");
        },
        (err) => {
            console.warn("Error getting location", err);
            window.parent.postMessage({type: "streamlit:setComponentValue", value: ""}, "*");
        }
    );
    """)
    if result:
        try:
            lat, lon = map(float, result.split(','))
            return lat, lon
        except:
            return None
    return None
