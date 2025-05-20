import streamlit as st
import pandas as pd
import numpy as np
from pandasql import sqldf

df = pd.read_csv("D:/Streamlit_app/env/Scripts/cleaned_ola_data.csv")
cleaned_ola_data = df

# Dictionary of 10 questions and their corresponding answers
query_dict = {
    "1. Retrieve all successful bookings": "SELECT * FROM cleaned_ola_data WHERE Booking_Status = 'Success'",

    "2. Find the average ride distance for each vehicle type": "SELECT Vehicle_Type, AVG(Ride_Distance) as avg_distance FROM cleaned_ola_data GROUP BY Vehicle_Type",

    "3. Get the total number of cancelled rides by customers": "SELECT COUNT(*) FROM cleaned_ola_data WHERE Booking_Status = 'Canceled by Customer'",

    "4. List the top 5 customers who booked the highest number of rides": "SELECT Customer_ID, COUNT(Booking_ID) as total_rides FROM cleaned_ola_data GROUP BY Customer_ID ORDER BY total_rides DESC LIMIT 5 ",

    "5. Get the number of rides cancelled by drivers due to personal and car-related issues": "SELECT COUNT(*) FROM cleaned_ola_data WHERE Canceled_Rides_by_Driver = 'Personal & Car related issue'",
    "6. Find the maximum and minimum driver ratings for Prime Sedan bookings": "SELECT MAX(Driver_Ratings) as max_rating, MIN(Driver_Ratings) as min_rating FROM cleaned_ola_data WHERE Vehicle_Type = 'Prime Sedan'",

    "7. Retrieve all rides where payment was made using UPI": "SELECT * FROM cleaned_ola_data WHERE Payment_Method = 'UPI'",

    "8. Find the average customer rating per vehicle type": "SELECT Vehicle_Type, AVG(Customer_Rating) as avg_customer_rating FROM cleaned_ola_data GROUP BY Vehicle_Type",

    "9. Calculate the total booking value of rides completed successfully": "SELECT SUM(Booking_Value) AS total_successful_ride_value FROM cleaned_ola_data WHERE Booking_Status = 'Success'",

    "10. List all incomplete rides along with the reason": "SELECT Booking_ID, Incomplete_Rides_Reason FROM cleaned_ola_data WHERE Incomplete_Rides = 'Yes'",
}



# UI
st.title("Ola Ride Insights")
st.write("This project simulates the core functionality of a ride-hailing platform like Ola, focusing on user experience, ride booking, and route management. It allows users to select pickup and drop-off locations, estimate fares based on distance and ride type, and view driver details. The system integrates real-time features such as location tracking, driver allocation, and trip status updates to replicate a realistic ride-booking workflow. The goal is to provide a seamless and interactive experience while exploring backend logic, APIs, and user interface design commonly used in mobility services.")


st.markdown('''
     ## Select one query below to view its result based on the CSV data:

            ''')

# Selectbox for one query at a time
selected_question = st.selectbox("Choose a Query", ["-- Select --"] + list(query_dict.keys()))

# Run and show query if a valid selection is made
if selected_question != "-- Select --":
    st.subheader(selected_question)
    
    query = query_dict[selected_question]
    st.code(query, language='sql')
    result = sqldf(query, locals())
    st.dataframe(result)  # Interactive table