foods_path = 'templates/foods.csv'
kajak = []
sor_id = 0


class Kaja:
    def __init__(self, etel):
        self.sor = etel
        self.nev = self.sor[0]
        self.leiras = self.sor[1]
        self.allergen = self.sor[2]
        self.id = self.sor[3]
        self.id = sor_id

    def csv_format(self):
        return f'\n {self.nev} ; {self.leiras} ; {self.allergen} ; {self.id}'

    def list_format(self):
        return [self.nev, self.leiras, self.allergen, self.id]


def load(path):
    with open(path, 'r', encoding="UTF-8") as file:
        etelek = []
        file = file.read()
        file = file.strip()
        file = file.split('\n')
        del file[0]

        return file


def get_food_by_id(food_id):
    for kaja in kajak:
        if kaja.id == food_id:
            return kaja
    return 'n/a'


for sor in load(foods_path):
    sor = sor.split(';')
    sor = Kaja(sor)
    kajak.append(sor)


def write(path=foods_path):
    kajak_uj = 'nev;leiras;allergenek;id'
    counter = 1

    for line in kajak:
        line.id = counter
        kajak_uj = kajak_uj + line.csv_format()
        counter += 1

    with open(path, 'w', encoding='UTF-8') as file:
        file.write(kajak_uj)


def add(data):
    try:
        kelid = kajak[-1].id
    except:
        kelid = 0
        print('Első adat!')

    data = [data[0], data[1], data[2], kelid]

    kajak.append(Kaja(data))

    write()


def edit(path):
    data = load(path)
    asdasd = []
    for i in data:
        etel = {
            'nev': i['nev'],
            'leiras': i['leiras'],
            'allergen': i['allergen'],
            'id': i['id'],
            'is_edit': False
        }
        asdasd.append(etel)

    return asdasd


def delete(path, nev):
    data_new = []
    data = load(path)
    for line in data:
        if line["nev"] != nev:
            data_new.append(line)

    write(path, data_new)


def change(path, mi_kell, data):
    uj = []
    regi = load(path)

    for sor in regi:
        if sor["id"] == int(mi_kell):
            uj.append(data)
        else:
            uj.append(sor)

    write(path, uj)


def error_handling(data):
    data_on_disk = load('templates/foods.csv')
    errors = []
    names = []

    for i in data_on_disk:
        names.append(i)

    if data[0] == '':
        errors.append('no_name')
    if data[1] == '':
        errors.append('no_allergen')
    if data[2] == '':
        errors.append('no_leiras')

    if data[0] in names:
        errors.append('same_name')

    print(errors)
