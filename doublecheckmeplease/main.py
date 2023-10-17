#!/usr/bin/env python3

from art import check_folder_for_art
from onsite import check_folders_for_designs_with_status_new_art
from production_tracking import get_name, create_spreadsheet_for_all_tables

if __name__ == "__main__":

    print(
        '''
    Press 1 to get a directory listing for a design number
    Press 2 to get a listing of all of the files with status 1.1 or 2.1 that have files in the folder
    Press 3 to lookup an employee ID from the production tracking system
    Press 4 to export the production tracking database to an Excel spreadsheet
    Press 5 to export a specific table from the production tracking database to an Excel spreadsheet
    Press 0 to exit
    ''')

    while True:
        try:
            userChoice = int(input("Choice: "))

            if userChoice == 1:
                check_folder_for_art()

            if userChoice == 2:
                check_folders_for_designs_with_status_new_art()

            if userChoice == 3:
                print(get_name())

            if userChoice == 4:
                create_spreadsheet_for_all_tables()

            if userChoice == 0:
                exit(0)

            if userChoice == 5:
                print('Under construction')

        except ValueError:
            print("Unknown choice")
