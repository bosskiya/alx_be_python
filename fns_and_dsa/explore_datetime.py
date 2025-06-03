#!/usr/bin/env python3

from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

    future_date = timedelta(days=int(input("Enter the number of days to add to the current date: ")))
    calculate_future_date = current_date + future_date
    print("Future date:", calculate_future_date.strftime("%Y-%m-%d"))

display_current_datetime()