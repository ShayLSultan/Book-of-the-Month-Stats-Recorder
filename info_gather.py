from datetime import datetime

date_format = "%d-%m-%Y"
options = {"Y": "Yes", "N": "No"}

def get_date(prompt, allow_default = False):
    date_string = input(prompt)
    if allow_default and not date_string:
        return datetime.today().strftime(date_format)
    try:
        valid_date = datetime.strptime(date_string, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid date format. Please enter the date as follows: dd-mm-yyyy ")
        return get_date(prompt, allow_default)

def get_member_name():
    return input("Enter your name ")

def get_book_name():
    return input("Enter book name ")

def get_genre():
    return input("Enter the genre that you would describe this book as ")

def get_rating():
    try:
        amount = float(input("Enter your rating out of 10 for this book e.g. '9' "))
        if amount <= 0:
            raise ValueError("Your rating must be greater than zero ")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()

def get_would_recommend():
    y_n = input("Would you recommend this book? Type 'Y' for Yes or 'N' for No ").upper()
    if y_n in options:
        return options[y_n]
    else: 
        print("Invalid response, please type 'Y' for Yes or 'N' for No ")
        return get_would_recommend()
