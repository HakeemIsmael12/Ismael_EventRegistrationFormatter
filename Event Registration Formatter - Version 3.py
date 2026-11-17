# Event Registration Formatter - Version 3.0 (Added date formatting)
import datetime


def main():
    first_name = input("Enter student first name: ").strip()
    last_name = input("Enter student last name: ").strip()
    section = input("Enter section: ").strip()
    event_name = input("Enter event name: ").strip()

    year = int(input("Enter event year: "))
    month = int(input("Enter event month: "))
    day = int(input("Enter event day: "))

    full_name_proper = f"{first_name} {last_name}".title()
    full_name_upper = f"{first_name} {last_name}".upper()
    section_upper = section.upper()
    event_name_clean = event_name.title()

    
    event_date = datetime(year, month, day)
    readable_date = event_date.strftime("%B %d, %Y")

    print("\nStudent Event Registration Summary")
    print(f"Name: {full_name_proper}")
    print(f"Name Code: {full_name_upper}")
    print(f"Section: {section_upper}")
    print(f"Event: {event_name_clean}")
    print(f"Event Date: {readable_date}")
    print("Language Used: Python")
    print("String Feature Used: strip(), title(), upper()")
    print("Date/Time Feature Used: datetime")
    print("\nRegistration record created successfully.")

if __name__ == "__main__":
    main()

# Reflection: For the third activity, the program is designed to handle student event registrations by prompting users to input their first name, last name, section, event name, and event date details including the year, month, and day. To ensure the registration details are neat and professional, the program incorporates string manipulation methods such as .strip(), .title(), and .upper() to clean and format the names and sections. Furthermore, it utilizes Python's datetime feature to transform numerical date inputs into a clear, readable format, culminating in a comprehensive summary that displays the formatted details, language used, and applied features. 




