import csv, os, copy

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def read_csv(file_name):
    file_list = []
    with open(os.path.join(__location__, file_name)) as f:
        rows = csv.DictReader(f)
        for r in rows:
            file_list.append(dict(r))

    return file_list


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

    def get_head(self, table_name):
        for table in self.database:
            if table.table_name == table_name:
                return table[0].keys()


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

    def join(self, other_table, common_key):
        joined_table = Table(self.table_name + '_joins_' + other_table.table_name, [])
        for item1 in self.table:
            for item2 in other_table.table:
                if item1[common_key] == item2[common_key]:
                    dict1 = copy.deepcopy(item1)
                    dict2 = copy.deepcopy(item2)
                    dict1.update(dict2)
                    joined_table.table.append(dict1)
        return joined_table

    def filter(self, condition):
        filtered_table = Table(self.table_name + '_filtered', [])
        for item1 in self.table:
            if condition(item1):
                filtered_table.table.append(item1)
        return filtered_table

    def update(self, key, val, data):
        # data = {key: val}
        for item in self.table:
            if item[key] == val:
                for data_key, data_val in data.items():
                    item[data_key] = data_val

    def __str__(self):
        return self.table_name + ':' + str(self.table)

