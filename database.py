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
    for i in d1.keys():
        del(i)

def del_tovary():
    return None


def edit_types():
    return None


def edit_tovary():
    return None


def save_into_file_please():
    na_file = open('backup.txt', 'w')
    pickle.dump(d1, na_file)
    na_file.close()


def load_from_file_please():
    global d1
    na_file = open('backup.txt', 'r')
    d1 = pickle.load(na_file)
    na_file.close()

