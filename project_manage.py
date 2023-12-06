import csv
import random
from database import Database, Table, read_csv
my_DB = Database()


def initializing():
    person = read_csv('persons.csv')
    logins = read_csv('login.csv')
    # project = read_csv('project_table.csv')
    # advisor = read_csv('Advisor_pending_request.csv')
    # member = read_csv('Member_pending_request.csv')

    persons_table = Table('persons', person)
    logins_table = Table('login', logins)
    projects_table = Table('project', [])
    advisor_table = Table('Advisor_pending_request', [])
    member_table = Table('Member_pending_request', [])
    my_DB.insert(persons_table)
    my_DB.insert(logins_table)
    my_DB.insert(projects_table)
    my_DB.insert(advisor_table)
    my_DB.insert(member_table)
    print(logins_table)

def login():
    username = input('enter username: ')
    password = input('enter password: ')
    my_login = my_DB.search('login')
    for i in my_login.table:
        if username == i['username'] and password == i['password']:
            return [i['ID'], i['role']]
    print('Invalid')
    return None

class Student:
    def __init__(self, person_id):
        self.person_id = person_id
        # self.name = ''
        self.title = ''
        self.project_id = random.randint(1,100)
        self.num_mem = 0

    def options(self):
        print('options:')
        print('1. Check request')
        print('2. Create project')
        print('3. Exit')
        options = int(input('select options: '))
        return options

    def students_menu(self):
        logins = my_DB.search('login')
        projects = my_DB.search('project')
        member_pending = my_DB.search('Member_pending_request')
        while True:
            option = self.options()
            if option == 1:
                for item in logins.table:
                    if item['role'] == 'student':
                        logins.update('ID', self.person_id, {'role': 'Member'})
                if len(member_pending.table) == 0:
                    print('No project request\n')
                else:
                    for item2 in member_pending.table:
                        if item2['to_be_member'] == self.person_id:
                            print(f"Project ID : {item2['ProjectID']}")
                    ans = int(input('Please enter project ID which you want to join: '))
                    for project in projects.table:
                        if ans == project['ProjectID']:
                            projects.update('ProjectID', ans, {'Member1': self.person_id})
                    print(projects.table)

                # for i in projects.table:
                #     if i['status'] == 'still in progress':
                #         print(i['ProjectID'])

            elif option == 2:
                title = input('Please enter title of the project: ')
                self.title = title
                projects.table.append({
                    'ProjectID': self.project_id,
                    'Title': title,
                    'Lead': self.person_id,
                    'Member1': '',
                    'Member2': '',
                    'Advisor': '',
                    'Status': 'still in progress'
                })

                for item in logins.table:
                    if item['role'] == 'student':
                        logins.update('ID', self.person_id, {'role': 'lead'})

                for item in logins.table:
                    if item['role'] == 'student':
                        member_pending.table.append({
                            'ProjectID': self.project_id,
                            'to_be_member': item['ID'],
                            'Response': '',
                            'Response_date': '',
                        })

                    # else:
                    #     print("You can't create project.")

                print(logins.table)
                print(projects.table)
                print(member_pending.table)

            elif option == 3:
                break

        for_login()

    def lead_menu(self):
        print('Role : Leader')
        print(self.title)


# class Project:
#     def __init__(self, title, lead):
#         self.title = title
#         self.lead = lead
#         self.project_id = random.randint(0,9999)
#         self.detail = ''
#         self.member1 = ''
#         self.member2 = ''
#         self.advisor = ''
#         self.status = 'still in process'
#
#     @property
#     def project_table(self):
#         projects_table = Table('project', [])
#         projects_table.table.append({
#             'ProjectID': self.project_id
#             'Title': self.title
#             'Lead': self.lead
#             'Member1': self.member1
#
#         })
# here are things to do in this function:
   # add code that performs a login task
        # ask a user for a username and password
        # returns [ID, role] if valid, otherwise returning None

# define a function called exit
def exit():
    pass
    # create_file("project_table", my_DB, create_head("project_table"))

# here are things to do in this function:
   # write out all the tables that have been modified to the corresponding csv files
   # By now, you know how to read in a csv file and transform it into a list of dictionaries. For this project, you also need to know how to do the reverse, i.e., writing out to a csv file given a list of dictionaries. See the link below for a tutorial on how to do this:



   # https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python


# make calls to the initializing and login functions defined above

initializing()
def for_login():
    while True:
        val = login()
        if val is not None: break

    if val[1] == 'student':
        print('Role : student')
        student = Student(val[0])
        student.students_menu()
    elif val[1] == 'lead':
        lead = Student(val[0])
        lead.lead_menu()
for_login()


# based on the return value for login, activate the code that performs activities according to the role defined for that person_id

    # if val[1] = 'admin':
        # see and do admin related activities

    # elif val[1] = 'student':
    #     see and do student related activities
    #
    # 1.see pending requests to become members of already created projects(ex. Have 3 projects, expend list of 3 projects ask yes/no
    #   if yes --> break, if no --> see the others, yes/no ,if deny all = lead)
    # 2. Member_pending_request table, respond should have both submit and deny
    # 3. Project table needs to be updated -->

    # elif val[1] = 'member':
    #     see and do member related activities
    # elif val[1] = 'lead':
    #     see and do lead related activities
    # elif val[1] = 'faculty':
    #     see and do faculty related activities
    # elif val[1] = 'advisor':
    #     see and do advisor related activities

# once everyhthing is done, make a call to the exit function
exit()
