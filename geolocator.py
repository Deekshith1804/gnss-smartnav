from streamlit_javascript import st_javascript

def get_user_location():
    result = st_javascript("""
        async () => {
            if (!navigator.geolocation) {
                alert("Geolocation is not supported by your browser.");
                return "";
            }

            return new Promise((resolve, reject) => {
                navigator.geolocation.getCurrentPosition(
                    (position) => {
                        const coords = position.coords.latitude + "," + position.coords.longitude;
                        resolve(coords);
                    },
                    (err) => {
                        alert("⚠️ Please allow location access in your browser to use this feature.");
                        resolve("");
                    }
                );
            });
        }
    """)

    if result and "," in result:
        try:
            lat, lon = map(float, result.split(","))
            return lat, lon
        except:
            return None
    return None
