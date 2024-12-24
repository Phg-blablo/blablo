from datetime import datetime

# Get the current date and time
current_date_time = datetime.now()

# Extract the year
current_year = current_date_time.year

def askingages(name):
    while True:
        try:
            year = int(input("Which year were you born:"))
            if 100 > (current_year - year) > 0:
                break
            else:
                print("Please input year smaller than 2024 and larger than 1923")
        except ValueError:
                print("please input valid year")
    name = input("What is your name:")
    age = current_year - year
    print(f"You are {age}")
askingages("Phuong") 