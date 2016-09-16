import tovar as tovar
import tipTovara as tip
import pickle
d1 = {}


def view_types():
    for i in d1.keys():
        print i


def view_tovary():
    for i in sum(d1.values(), []):
        print i



def view_all():
    for i in d1.keys():
        print i
        for k in d1[i]:
            print "  " + str(k)

def add_types():
    name = str(raw_input("Type name: "))
    category = str(raw_input("Type category"))
    id = str(raw_input("Type id"))
    tovar_type = tip.tipTovara(name, category, id)
    d1[tovar_type] = None


def add_tovary():
    name = str(raw_input("Type name: "))
    price = str(raw_input("Type price"))
    date = str(raw_input("Type date"))
    tovary = tovar.tovar(name, price, date)
    tovartype = d1.keys()
    for i in range(len(tovartype)):
        print str(i)+". " + str(tovartype[i])
    type1 = int(raw_input("Type category num:"))
    if d1[tovartype[type1]] == None:
        d1[tovartype[type1]] = [tovary]
    else:
        d1[tovartype[type1]].append(tovary)

def del_types():
    tovartype = d1.keys()
    for i in range(len(tovartype)):
        print str(i) + ". " + str(tovartype[i])
    type1 = int(raw_input("Type category num:"))
    del (d1[tovartype[type1]])


def del_tovary():
    sum1 = sum(d1.values(), [])
    for i in range(len(sum1)):
        print str(i) + ". " + str(sum1[i])
    input1 = sum1[int(raw_input("Which tovar do you want to delete?"))]
    for i in d1.keys():
        if input1 in d1[i]:
            d1[i].remove(input1)
            break

def edit_types():
    tovartype = d1.keys()
    for i in range(len(tovartype)):
        print str(i) + ". " + str(tovartype[i])
    type1 = int(raw_input("Which tovartype do you want to edit?"))
    name = raw_input("Seichas imya " + tovartype[type1].name + ", esli vi jelayete pomenyat' ego, vvedite another one: " )
    if name != "":
        tovartype[type1].name = name
    category = raw_input("Seichas category " + tovartype[type1].category + ", esli vi jelayete pomenyat' ee, vvedite another one: ")
    if category != "":
        tovartype[type1].category = category
    id = raw_input("Seichas id " + tovartype[type1].id + ", esli vi jelayete pomenyat' ego, vvedite another one: ")
    if id != "":
        tovartype[type1].id = id


def edit_tovary():
    sum1 = sum(d1.values(), [])
    for i in range(len(sum1)):
        print str(i) + ". " + str(sum1[i])
    input1 = sum1[int(raw_input("Which tovar do you want to edit?"))]
    name = raw_input(
        "Seichas imya " + input1.name + ", esli vi jelayete pomenyat' ego, vvedite another one: ")
    if name != "":
        input1.name = name
    price = raw_input(
        "Seichas price " + input1.price + ", esli vi jelayete pomenyat' ee, vvedite another one: ")
    if price != "":
        input1.price = price
    date1 = raw_input("Seichas date1 " + input1.date1 + ", esli vi jelayete pomenyat' ego, vvedite another one: ")
    if date1 != "":
        input1.date1 = date1

    
def save_into_file_please():
    na_file = open('backup.txt', 'w')
    pickle.dump(d1, na_file)
    na_file.close()


def load_from_file_please():
    global d1
    na_file = open('backup.txt', 'r')
    d1 = pickle.load(na_file)
    na_file.close()

