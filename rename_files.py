# This is a practice program called "Rename Files" written for
# Udacity course "Programming Foundations with Python"

import os

def rename_files():
    #(1) get filre names from the target folder
    file_list = os.listdir(r"C:\Users\Ryan\Desktop\test")
    print(file_list)

    #(2) for each file, rename file removing all numbers

rename_files()
