import database as db

def main_menu():
    while(True):
        print "Menu:"
        print " 1.View"
        print " 2.Add"
        print " 3.Delete"
        print " 4.Edit"
        print " 5.Search"
        print " 6.Exit"

        in1 = int(input("Choose menu"))

        if in1 == 1:
            view_menu()

        elif in1 == 2:
            add_menu()

        elif in1 == 3:
            del_menu()

        elif in1 == 4:
            edit_menu()

        elif in1 == 5:
            search_menu()

        elif in1 == 6:
            break

        else: print "Unexpected answer"


def view_menu():
    print "1.Tipu"
    print "2.Tovary"
    print "3.Vse vmeste"
    print "4.Exit"

    in2 = int(input("Choose menu"))

    if in2 == 1:
        db.view_types()

    elif in2 == 2:
        db.view_tovary()

    elif in2 == 3:
        db.view_all()

    elif in2 == 4:
        pass


def add_menu():
    print "1.Tip tovara"
    print "2.Tovar"
    print "3.Exit"
    in2 = int(input("Choose menu"))

    if in2 == 1:
        db.add_types()

    elif in2 == 2:
        db.add_tovary()

    elif in2 == 3:
        pass


def del_menu():
    print "1.Tip tovara"
    print "2.Tovar"
    print "3.Exit"
    in2 = int(input("Choose menu"))

    if in2 == 1:
        db.del_types()

    elif in2 == 2:
        db.del_tovary()

    elif in2 == 3:
        pass


def edit_menu():
    print "1.Tip tovara"
    print "2.Tovar"
    print "3.Exit"
    in2 = int(input("Choose menu"))

    if in2 == 1:
        db.edit_types()

    elif in2 == 2:
        db.edit_tovary()

    elif in2 == 3:
        pass


def search_menu():
    print "search"

