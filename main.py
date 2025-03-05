import streamlit as st


st.markdown("<h1 style='text-align: center;'>  Unit Converter 🔄</h1>", unsafe_allow_html=True )
st.markdown("##### converts Length, Weight, and Time instantly")


category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])


def convert_units(category, value, unit):


    # --------------Units for Length -----------------------
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371  # 1km = 0.621371 miles
        elif unit == "Miles to Kilometers":
            return value / 0.621371  # 1mile = 1.60934 km
        elif unit == "Meters to Feet":
            return value * 3.28084  # 1meter = 3.28084 feet
        elif unit == "Feet to Meters":
            return value / 3.28084  # 1foot = 0.3048 meters
        elif unit == "Centimeters to Inches":
            return value * 0.393701  # 1cm = 0.393701 inches
        elif unit == "Inches to Centimeters":
            return value / 0.393701  # 1inch = 2.54 cm
        elif unit == "Yards to Meters":
            return value * 0.9144  # 1yard = 0.9144 meters
        elif unit == "Meters to Yards":
            return value / 0.9144  # 1meter = 1.09361 yards
        elif unit == "Miles to Feet":
            return value * 5280  # 1mile = 5280 feet
        elif unit == "Feet to Miles":
            return value / 5280  # 1foot = 0.000189394 miles
        elif unit == "Kilometers to Meters":
            return value * 1000  # 1km = 1000 meters
        elif unit == "Meters to Kilometers":
            return value / 1000  # 1meter = 0.001 km
     

        






     # --------------Units for Weight ----------------------
    elif category == "Weight":
        if unit == "Kilograms to pounds":  # 1 kg = 2.20462 pounds 
            return value * 2.20462
        elif unit == "Pounds to kilograms":  # 1 pound = 0.453592 kg 
            return value / 2.20462
        
    elif category == "Time":
        if unit == "Seconds to minutes": #  1sec =  0.0166667 min
            return value / 60
        elif unit == "Minutes to seconds": # 1 min = 60 sec
            return value * 60
        elif unit == "Minutes to hours":
            return value / 60
        elif unit == "Hours to minutes": # 1 hour =60 min
            return value * 60
        elif unit == "Hours to days":
            return value / 24
        elif unit == "Days to hours": # 1 day = 24 hours
            return value * 24
    return 0
        
if category == "Length":
    unit = st.selectbox("📏 Select Conversation", ["Miles to Kilometers","Kilometers to Miles","Meters to Feet", "Feet to Meters", "Centimeters to Inches", "Inches to Centimeter", "Yards to Meters", "Meter to Yards", "Miles to Feet", "Feet to Miles", "Kilometers to Meters", "Meters to Kilometers"])
elif category == "Weight":
    unit = st.selectbox("⚖️ Select Conversation", ["Kilograms to pounds", "Pounds to kilograms"])
        
elif category == "Time":
    unit = st.selectbox("🕑 Select Conversation", ["Seconds to minutes", "Minutes to seconds", "Minutes to hours", "Hours to minutes", "Hours to days", "Days to hours"])

value = st.number_input("Enter the value to convert")

if st.button("Convert" ):
    result = convert_units(category, value, unit)
    st.info(f"The result is {result:.1f}")
    