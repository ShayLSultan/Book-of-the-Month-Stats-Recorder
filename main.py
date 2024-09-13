import pandas as pd
import csv 
from datetime import datetime
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

BOTM.init_botm()
BOTM.add_review("09-09-2024", "Shay", "Rendezvous with Rama", "Sci-Fi", 5, "Yes")