import datetime

# Function to calculate the remaining days
def countdown(target_date):
    today = datetime.date.today()  # Get today's date
    delta = target_date - today    # Calculate the difference
    return delta.days

# Input the target date (format: YYYY-MM-DD)
target_date_input = input("Enter the target date (YYYY-MM-DD): ")
try:
    # Convert the input string into a datetime object
    target_date = datetime.datetime.strptime(target_date_input, "%Y-%m-%d").date()
    
    # Calculate the countdown
    days_left = countdown(target_date)
    
    # Display the result
    if days_left > 0:
        print(f"{days_left} days left until {target_date}.")
    elif days_left == 0:
        print("Today is the day!")
    else:
        print(f"{-days_left} days have passed since {target_date}.")
except ValueError:
    print("Invalid date format. Please use YYYY-MM-DD.")
