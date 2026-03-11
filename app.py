import streamlit as st
import pandas as pd

st.set_page_config(page_title="Pet Grooming Services", page_icon="🐶")

st.sidebar.title("🐾 Grooming Services")
page = st.sidebar.radio(
    "Navigation",
    ["Home", "Book Grooming", "Service Dashboard", "About"]
)

if page == "Home":

    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        st.title("🐶 Pet Grooming Services")
        st.write("Welcome to our grooming service app!")
        st.write("Pet owners can book grooming appointments easily.")

        st.image(
            "https://cdn-icons-png.flaticon.com/512/616/616408.png",
            width=200
        )

        st.divider()

        if st.button("Book Grooming Appointment"):
            st.success("Use the sidebar and go to the **Book Grooming** page.")

elif page == "Book Grooming":

    st.title("✂️ Book a Grooming Appointment")

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

    st.divider()

    if st.button("Submit Appointment"):
        st.success("Your grooming appointment has been submitted!")

elif page == "Service Dashboard":

    st.title("📊 Grooming Service Dashboard")

    data = {
        "Service": ["Bath", "Haircut", "Nail Trim", "Ear Cleaning"],
        "Bookings": [10, 7, 5, 4]
    }

    df = pd.DataFrame(data)

    st.subheader("Grooming Service Table")
    st.table(df)

    st.subheader("Service Popularity")
    st.bar_chart(df.set_index("Service"))

elif page == "About":

    st.title("About This App")

    st.write("""
This application is a **Pet Grooming Service Booking App**.

It helps pet owners book grooming services for their pets.

Pet owners who want a simple and easy way to schedule grooming appointments.

The app collects:
- Owner name
- Pet name
- Pet type
- Grooming services
- Appointment date and time
- Special instructions

The app shows:
- Appointment confirmation
- A dashboard that displays grooming service bookings.
""")
