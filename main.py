import menu
import database

database.load_from_file_please()
menu.main_menu()
database.save_into_file_please()