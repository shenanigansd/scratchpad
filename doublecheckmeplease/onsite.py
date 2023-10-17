import os

from databases.filemaker import connect
from files import get_design_folder


def check_folders_for_designs_with_status_new_art():
    connection = connect()
    cursor = connection.cursor()
    for row in cursor.execute("SELECT d.ID_Design FROM des d WHERE d.id_Serial_Status=2.1 OR d.id_Serial_Status=1.1"):
        try:
            if os.listdir(get_design_folder(int(row.ID_Design))):
                print(str(int(row.ID_Design)) + ": " + str(os.listdir(get_design_folder(int(row.ID_Design)))))
        except FileNotFoundError:
            print("Error checking " + str(int(row.ID_Design)) + ": folder not found")
