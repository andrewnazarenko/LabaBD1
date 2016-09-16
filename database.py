import tovar
import tipTovara as tip

d1 = {}


def view_types():
    print(d1.keys())


def view_tovary():
    return None


def view_all():
    return None


def add_types():
    name = str(raw_input("Type name: "))
    category = str(raw_input("Type category"))
    id = str(raw_input("Type id"))
    tovar_type = tip.tipTovara(name, category, id)
    d1[tovar_type] = None


def add_tovary():
    return None


def del_types():
    return None


def del_tovary():
    return None


def edit_types():
    return None


def edit_tovary():
    return None
