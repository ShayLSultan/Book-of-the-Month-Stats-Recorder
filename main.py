import pandas as pd
import csv 
from datetime import datetime
from info_gather import get_date, get_member_name, get_book_name, get_genre, get_rating, get_would_recommend
import matplotlib.pyplot as plt

class BOTM:
    csv_file = "botm_data.csv"
    the_columns = ["date", "member name", "book name", "genre", "rating", "would recommend"]
    date_format = "%d-%m-%Y"

    @classmethod
    def init_botm(self):
        try:
            pd.read_csv(self.csv_file) 
        except FileNotFoundError:
            data_frame = pd.DataFrame(columns = self.the_columns)
            data_frame.to_csv(self.csv_file, index = False)
    
    @classmethod
    def add_review(self, date, member_name, book_name, genre, rating, would_recommend):
        new_entry = {
            "date": date,
            "member name": member_name,
            "book name": book_name,
            "genre": genre,
            "rating": rating,
            "would recommend": would_recommend
        }
        with open(self.csv_file, "a", newline = "") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = self.the_columns)
            writer.writerow(new_entry)
        print("Entry successfully added")

def add_entry_interface():
    BOTM.init_botm()
    date = get_date("Enter the date of the book club meeting in the format dd-mm-yyy, or press enter for today's date: ", allow_default= True)
    member_name = get_member_name()
    book_name = get_book_name()
    genre = get_genre()
    rating = get_rating()
    would_recommend = get_would_recommend()
    BOTM.add_review(date, member_name, book_name, genre, rating, would_recommend)

add_entry_interface()