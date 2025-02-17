from datetime import datetime


date1 = input("Enter the first date (YYYY-MM-DD): ")

date_of_day = datetime.strptime(date1, "%Y-%m-%d")
print(date_of_day.strftime('%A'))