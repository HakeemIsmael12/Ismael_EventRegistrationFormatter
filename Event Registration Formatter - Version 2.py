# Event Registration Formatter - Version 2.0 (Added string formatting)
def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    section = input("Enter your section: ")
    event_name = input("Enter the event name: ")
    year = input("Enter the year (YYYY): ")
    month = input("Enter the month (MM): ")
    day = input("Enter the day (DD): ")

    full_name_proper = f"{first_name.capitalize()} {last_name.capitalize()}"
    full_name_upper = f"{first_name.upper()} {last_name.upper()}"
    section_upper = section.upper()
    event_name_proper = event_name.title()

    print("\nStudent Event Registration Summary")
    print(f"Name: {full_name_proper}")
    print(f"Name Code: {full_name_upper}")
    print(f"Section: {section_upper}")
    print(f"Event: {event_name_proper}")
    print(f"Event Date: {month} {day}, {year}")
    print("Language Used: Python")
    print("String Feature Used: strip(), title(), upper()")
    print("Date/Time Feature Used: None")
    print("\nRegistration record created successfully.")

if __name__ == "__main__":
    main()



    