# try wrapping the code below that reads a persons.csv file in a class and make it more general such that it can read in any csv file


import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

persons = []
with open(os.path.join(__location__, 'persons.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        persons.append(dict(r))
print(persons)

import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

login_list = []
with open(os.path.join(__location__, 'login.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        login_list.append(dict(r))
print(login_list)


# add in code for a Database class
class Database:
    def __init__(self):
        self.database = []

    def insert(self, table):
        self.database.append(table)

    def search(self, table_name):
        for table in self.database:
            if table.table_name == table_name:
                return table
        return None

# add in code for a Table class

class Table:
    def __init__(self, table_name, table):
        self.table_name = table_name
        self.table = table

    def select(self, attributes_list):
        temps = []
        for item1 in self.table:
            dict_temp = {}
            for key in item1:
                if key in attributes_list:
                    dict_temp[key] = item1[key]
            temps.append(dict_temp)
        return temps

    def insert(self, dic):
        self.table.append(dic)

    def update(self, key, val, data):
        # data = {key: val}
        for item in self.table:
            if item[key] == val:
                for data_key, data_val in data.items():
                    item[data_key] = data_val

    def __str__(self):
        return self.table_name + ':' + str(self.table)


# modify the code in the Table class so that it supports the insert operation where an entry can be added to a list of dictionary

# modify the code in the Table class so that it supports the update operation where an entry's value associated with a key can be updated

# test = Table('person', persons)
# test.update('ID', '9898118', {'fist': 'proudTest'})
