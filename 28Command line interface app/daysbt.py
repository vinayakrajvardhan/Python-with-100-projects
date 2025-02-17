import sys
from datetime import datetime


def calculate_date_difference(date1, date2):
    # Convert the dates to datetime objects
    date1 = datetime.strptime(date1, "%Y-%m-%d")
    date2 = datetime.strptime(date2, "%Y-%m-%d")

    # Calculate the difference between the dates
    difference = abs((date2 - date1).days)

    return difference

date1 = input("Enter the first date (YYYY-MM-DD): ")
date2 = input("Enter the second date (YYYY-MM-DD): ")
print(calculate_date_difference(date2,date1))

