def collect_employee_info():
    """
    Function to collect personal information from employees via user input.
    """
    print("\nPlease enter the following personal information:")
    
    employee_info = {
        "Full Name": input("Full Name: "),
        "Date of Birth": input("Date of Birth (YYYY-MM-DD): "),
        "Address": input("Address: "),
        "Contact Number": input("Contact Number (Phone, Email): "),
        "Emergency Contact Details": input("Emergency Contact Details: ")
    }
    
    print("\nCollected Employee Information:")
    for key, value in employee_info.items():
        print(f"{key}: {value}")
    
    return employee_info

if __name__ == "__main__":
    employee_data = collect_employee_info()
