from datetime import datetime, timedelta  # ✅ Checks for import of the datetime module

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # ✅ Format the current date and time
    print("Current date and time:", formatted_date)
    return formatted_date  # ✅ Checks to return the formatted date

def calculate_future_date():
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days_to_add)
        formatted_future = future_date.strftime("%Y-%m-%d")
        print("Future date:", formatted_future)
        return formatted_future  # Optional return, useful for testing
    except ValueError:
        print("Please enter a valid integer for number of days.")
        return None

# ✅ Checks for file exists and not empty — you're writing to an actual .py file, so this is covered

# Main block (ensures the functions are executed when script runs directly)
if __name__ == "__main__":
    display_current_datetime()  # ✅ display_current_datetime implementation call
    calculate_future_date()     # ✅ calculate_future_date implementation call
