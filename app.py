import streamlit as st
import pandas as pd

# Sidebar Navigation
st.sidebar.title("Pet Grooming Services")
page = st.sidebar.radio("Navigate", ["Home", "Book Grooming", "Service Dashboard", "About"])

# HOME PAGE
if page == "Home":
    st.title("Pet Grooming Service App")
    st.header("Welcome to our Grooming Service")
    st.write("This app allows pet owners to book grooming services for their pets.")
    st.image("https://cdn-icons-png.flaticon.com/512/616/616408.png", width=200)

    if st.button("Book a Grooming Service"):
        st.success("Go to the Book Grooming page from the sidebar.")

# BOOK GROOMING PAGE
elif page == "Book Grooming":
    st.title("Book a Grooming Appointment")

    name = st.text_input("Owner Name")
    pet_name = st.text_input("Pet Name")

    pet_type = st.selectbox(
        "Pet Type",
        ["Dog", "Cat", "Rabbit", "Other"]
    )

    services = st.multiselect(
        "Select Grooming Services",
        ["Bath", "Haircut", "Nail Trim", "Ear Cleaning"]
    )

    pet_age = st.number_input("Pet Age", 0, 20)

    grooming_date = st.date_input("Appointment Date")

    grooming_time = st.time_input("Preferred Time")

    grooming_style = st.radio(
        "Grooming Style",
        ["Basic", "Standard", "Full Groom"]
    )

    reminder = st.checkbox("Send Appointment Reminder")

    notes = st.text_area("Special Instructions")

    if st.button("Submit Appointment"):
        st.success("Your grooming appointment has been submitted!")

# DASHBOARD PAGE
elif page == "Service Dashboard":
    st.title("Grooming Service Dashboard")

    data = {
        "Service": ["Bath", "Haircut", "Nail Trim", "Ear Cleaning"],
        "Bookings": [10, 7, 5, 4]
    }

    df = pd.DataFrame(data)

    st.table(df)
    st.bar_chart(df.set_index("Service"))

# ABOUT PAGE
elif page == "About":
    st.title("About This App")

    st.write("""
    This app is a Pet Grooming Service booking system.

    It allows pet owners to book grooming services for their pets easily.

    Target users are pet owners who want a simple way to schedule grooming appointments.

    The app collects inputs such as owner name, pet name, pet type,
    grooming services, appointment date, and special instructions.

    The output shows confirmation messages and a simple dashboard
    that displays grooming service bookings.
    """)