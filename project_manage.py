import csv
from database import Database, Table, read_csv
my_DB = Database()


def initializing():

# here are things to do in this function:

    # create an object to read all csv files that will serve as a persistent state for this program

    # create all the corresponding tables for those csv files

    person = read_csv('persons.csv')
    logins = read_csv('login.csv')
    # project = read_csv('project_table.csv')
    # advisor = read_csv('Advisor_pending_request.csv')
    # member = read_csv('Member_pending_request.csv')

    persons_table = Table('persons', person)
    logins_table = Table('login', logins)
    # projects_table = Table('project', project)
    # advisor_table = Table('Advisor_pending_request', advisor)
    # member_table = Table('Member_pending_request', member)
    print(logins_table.table)

    my_DB.insert(persons_table)
    my_DB.insert(logins_table)
    # my_DB.insert(projects_table)
    # my_DB.insert(advisor_table)
    # my_DB.insert(member_table)


def login():
    username = input('enter username: ')
    password = input('enter password: ')
    my_login = my_DB.search('login')
    for i in my_login.table:
        if username == i['username'] and password == i['password']:
            # print([i['ID'], i['role']])
            return [i['ID'], i['role']]
    # print('Invalid')
    return None
#
# def student_login():
#     print('role: student')


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
val = login()

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
