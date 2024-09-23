from datetime import datetime

date_format = "%d-%m-%Y"
options = {"Y": "Yes", "N": "No"}
genres = {"F": "Fantasy", "S": "Sci-Fi", "C": "Contemporary", "Cl": "Classic", "O": "Other"}

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
    genre = input(" What genre is this book? Type 'F for fantasy, 'S' for Sci-Fi, 'C' for Contemporary, 'Cl' for Classic, or 'O' for Other ")
    if genre in genres:
        return genres[genre]
    else:
        print("Invalid response, please type 'F for fantasy, 'S' for Sci-Fi, 'C' for Contemporary, 'Cl' for Classic, or 'O' for Other ")
        return get_genre()

def get_rating():
    try:
        rating = float(input("Enter your rating out of 10 for this book e.g. '9' "))
        if rating <= 0:
            raise ValueError("Your rating must be greater than zero ")
        return rating
    except ValueError as e:
        print(e)
        return get_rating()

def get_would_recommend():
    y_n = input("Would you recommend this book? Type 'Y' for Yes or 'N' for No ").upper()
    if y_n in options:
        return options[y_n]
    else: 
        print("Invalid response, please type 'Y' for Yes or 'N' for No ")
        return get_would_recommend()
