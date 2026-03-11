import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="The Grooming Pawlor")

if "page" not in st.session_state:
    st.session_state.page = "Home"

st.sidebar.title("🐾 Grooming Services")

nav = st.sidebar.radio(
    "Navigation",
    ["Home", "Book Grooming", "Service Dashboard", "About"],
    index=["Home","Book Grooming","Service Dashboard","About"].index(st.session_state.page)
)

st.session_state.page = nav


if st.session_state.page == "Home":

    left, center, right = st.columns([1,2,1])

    with center:
        st.title("The Grooming Pawlor")

        st.write("Welcome to our Grooming Pawlor app!")
        st.write("Where pet owners can easily book grooming services for their pets.")
        st.write("We offer grooming for different animals.")

        st.divider()

      
        col1, col2,  = st.columns(2)

        with col1:
            st.image(
                "https://cdn-icons-png.flaticon.com/512/616/616408.png",
                caption="Dog"
            )

        with col2:
            st.image(
                "https://cdn-icons-png.flaticon.com/512/616/616430.png",
                caption="Cat"
            )

        st.divider()

        with st.expander("See Available Grooming Services"):
            st.write("🛁 Bath - Cleaning and Shampoo")
            st.write("✂️ Haircut - Professional Trimming")
            st.write("🐾 Nail Trim - Safe Nail Cutting")
            st.write("👂 Ear Cleaning - Gentle Ear Care")

        if st.button("Book Grooming Appointment"):
            st.session_state.page = "Book Grooming"
            st.rerun()


elif st.session_state.page == "Book Grooming":

    st.title("Book a Grooming Appointment")

    name = st.text_input("Owner Name")

    pet_name = st.text_input("Pet Name")

    pet_type = st.selectbox(
        "Pet Type",
        ["Dog", "Cat", "Rabbit", "Hamster", "Other"]
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

        st.write("Processing appointment...")
        progress = st.progress(0)

        for i in range(100):
            time.sleep(0.01)
            progress.progress(i+1)

        st.success("Appointment successfully processed!")


elif st.session_state.page == "Service Dashboard":

    st.title("Grooming Service Dashboard")

    data = {
        "Service": ["Bath", "Haircut", "Nail Trim", "Ear Cleaning"],
        "Bookings": [10, 7, 5, 4]
    }

    df = pd.DataFrame(data)

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Services", "4")

    with col2:
        st.metric("Total Bookings Today", "26")

    st.subheader("Grooming Service Table")
    st.table(df)

    st.subheader("Service Popularity")
    st.bar_chart(df.set_index("Service"))


elif st.session_state.page == "About":

    st.title("About This App")

    st.write("""
    This app is a Pet Grooming Service booking system.

    It allows pet owners to book grooming services for their pets easily.

    Target users are pet owners who want a simple way to schedule grooming appointments.

    The app collects inputs such as owner name, pet name, pet type, grooming services, appointment date, and special instructions.

    The output shows confirmation messages and a simple dashboard that displays grooming service bookings.
    """)
