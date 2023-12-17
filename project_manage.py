import csv
import sys
import os
import random
from database import Database, Table, read_csv
from datetime import datetime
current_time = datetime.now()
current_date = current_time.date()

my_DB = Database()


def initializing():
    person = read_csv('persons.csv')
    logins = read_csv('login.csv')
    project = read_csv('project_table.csv')
    advisor = read_csv('Advisor_pending_request.csv')
    member = read_csv('Member_pending_request.csv')

    persons_table = Table('persons', person)
    logins_table = Table('login', logins)
    projects_table = Table('project', project)
    advisor_table = Table('Advisor_pending_request', advisor)
    member_table = Table('Member_pending_request', member)

    my_DB.insert(persons_table)
    my_DB.insert(logins_table)
    my_DB.insert(projects_table)
    my_DB.insert(advisor_table)
    my_DB.insert(member_table)


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
        projects = my_DB.search('project')
        if len(projects.table) == 0:
            self.project_id = str(1)
        else:
            self.project_id = str(len(projects.table) + 1)

    # student menu options
    def options(self):
        while True:
            print('options:')
            print('0. Log-out')
            print('1. Check request')
            print('2. Create project')
            options = int(input('select options: '))
            if options in (0, 1, 2):
                return options
            else:
                print('Invalid options, Try again!')

    def students_menu(self):
        print('---Role : Student---')
        persons = my_DB.search('persons')
        logins = my_DB.search('login')
        projects = my_DB.search('project')
        member_pending = my_DB.search('Member_pending_request')
        advisor_pending = my_DB.search('Advisor_pending_request')
        while True:
            option = self.options()
            if option == 1:
                if (len(member_pending.table) == 0
                        or len(projects.filter(lambda x: x['Status'] == 'Pending members').table) == 0):
                    print('No project request!\n')
                else:
                    for item2 in member_pending.table:
                        pro_fil = projects.filter(lambda x: x['Status'] == 'Pending members'
                                                            and x['ProjectID'] == item2['ProjectID']).table
                        if item2['to_be_member'] == self.person_id and len(pro_fil) != 0:
                            print(f"Project ID : {item2['ProjectID']} ({pro_fil[0]['Title']})")
                    print("If you don't want to join any project, enter(0)")
                    ans = input('Please enter project ID which you want to join: ')
                    is_exist = False
                    for project in projects.table:
                        if ans == project['ProjectID']:
                            if project['Member1'] == '':
                                project['Member1'] = self.person_id
                                print(f'You are the member of ProjectID : {ans}')
                            elif project['Member1'] != '' and project['Member2'] == '':
                                project['Member2'] = self.person_id
                                print(f'You are the member of ProjectID : {ans}')
                                project['Status'] = 'Still in progress'
                            is_exist = True

                    if is_exist:
                        member_acc = member_pending.filter(lambda x: x['ProjectID'] == ans
                                                                     and x['to_be_member'] == self.person_id).table
                        member_acc[0]['Response'] = 'accepted'
                        member_acc[0]['Response_date'] = current_date.__str__()

                        member_deny = member_pending.filter(lambda x: x['ProjectID'] != ans
                                                                      and x['to_be_member'] == self.person_id).table
                        for mem_d in member_deny:
                            mem_d['Response'] = 'deny'
                            mem_d['Response_date'] = current_date.__str__()

                        for item in logins.table:
                            if item['role'] == 'student':
                                logins.update('ID', self.person_id, {'role': 'member'})
                        persons.update('ID', self.person_id, {'type': 'member'})
                        print('***Please log-out(0) and log-in again!***\n')

                    else:
                        print('Invalid Project ID!')

            elif option == 2:
                title = input('Please enter title of the project: ')
                persons.update('ID', self.person_id, {'type': 'lead'})
                for item in logins.table:
                    if item['role'] == 'student':
                        logins.update('ID', self.person_id, {'role': 'lead'})
                        member_pending.update('to_be_member', self.person_id, {'Response': 'deny'})
                        member_pending.update('to_be_member', self.person_id, {'Response_date': current_date.__str__()})

                projects.table.append({
                    'ProjectID': self.project_id,
                    'Title': title,
                    'Detail': None,
                    'Lead': self.person_id,
                    'Member1': '',
                    'Member2': '',
                    'Advisor': 'Waiting',
                    'Status': 'Pending members',
                    'Comment': None,
                    'CountApprove': 0
                })

                print('***Please log-out(0) and log-in again!***\n')

                for item in logins.table:
                    if item['role'] == 'student':
                        member_pending.table.append({
                            'ProjectID': self.project_id,
                            'to_be_member': item['ID'],
                            'Response': None,
                            'Response_date': None
                        })
                    elif item['role'] == 'faculty':
                        advisor_pending.table.append({
                            'ProjectID': self.project_id,
                            'to_be_advisor': item['ID'],
                            'Response': None,
                            'Response_date': None
                        })

            elif option == 0:
                break

        for_login()

    def option_lead(self):
        while True:
            print('options:')
            print("0. Log-out")
            print("1. Check member sending request")
            print("2. Check advisor sending request")
            print("3. Check project's details")
            print("4. Check project's status")
            print("5. Delete project")
            options = int(input('select options: '))
            if options in (0, 1, 2, 3, 4, 5):
                return options
            else:
                print('Invalid options, Try again!')

    def lead_menu(self):
        print('---Role : Leader---')
        logins = my_DB.search('login')
        projects = my_DB.search('project')
        member_pending = my_DB.search('Member_pending_request')
        advisor_pending = my_DB.search('Advisor_pending_request')
        for i in projects.filter(lambda x: x['Lead'] == self.person_id).table:
            print(f"Project's ID: {i['ProjectID']}")
            mem_name = logins.filter(lambda x: x['ID'] == i['Member1'] or x['ID'] == i['Member2']).table
            for k in range(len(mem_name)):
                print(f"Member{k + 1}: {mem_name[k]['username']}")
            adv_name = logins.filter(lambda x: x['ID'] == i['Advisor']).table
            for n in range(len(adv_name)):
                print(f"Advisor: {adv_name[n]['username']}")

        while True:
            option = self.option_lead()
            for i in projects.filter(lambda x: x['Lead'] == self.person_id).table:
                if option == 1:
                    mem_pen = member_pending.filter(lambda x: x['ProjectID'] == i['ProjectID']).table
                    for name in range(len(mem_pen)):
                        pen_name = logins.filter(lambda x: x['ID'] == mem_pen[name]['to_be_member']).table
                        print(f"Name: {pen_name[0]['username'].ljust(15)}Response: {mem_pen[name]['Response']}")
                elif option == 2:
                    adv_pen = advisor_pending.filter(lambda x: x['ProjectID'] == i['ProjectID']).table
                    for name in range(len(adv_pen)):
                        adv_name = logins.filter(lambda x: x['ID'] == adv_pen[name]['to_be_advisor']).table
                        print(f"Name: {adv_name[0]['username'].ljust(15)}Response: {adv_pen[name]['Response']}")
                elif option == 3:
                    print(f"---Project's details---")
                    print(f"Title: {i['Title']}")
                    print(f"Details: {i['Detail']}")
                    print(f"Comment: {i['Comment']}")
                    if i['Status'] != 'Submit':
                        ans_ti = input("Do you want to change project's title(y/n)? ")
                        if ans_ti == 'y':
                            title = input("Please write your project's title: ")
                            i['Title'] = title
                            print(f"New title! {title}")
                        ans_de = input("Do you want to change project's details(y/n)? ")
                        if ans_de == 'y':
                            details = input("Please write your project's details: ")
                            i['Detail'] = details
                            print(f"New details! {details}")
                elif option == 4:
                    print(f"---Project's status: {i['Status']}---")
                    if i['Status'] != 'Completed' and i['Status'] != 'Delete' and i['Status'] != 'Approve':
                        print(f"WARNING! If you 'submit' the project, you can't change any details later.")
                        submit = input("Do you want to submit the project(y/n)? ")
                        if submit == 'y' and i['Advisor'] != 'Waiting':
                            i['Status'] = 'Submit'
                            print("You have already submitted, waiting for faculties to approve.")
                elif option == 5:
                    delete = input("Do you want to delete the project?(y/n) ")
                    if delete == 'y':
                        confirm = int(input("Please enter(y) for confirming to delete "))
                        if confirm == 'y':
                            print("Admin is going to delete your project.")
                            projects.update("Lead", self.person_id, {"Status": "Delete"})

                elif option == 0:
                    for_login()

    def option_member(self):
        while True:
            print('options:')
            print("0. Log-out")
            print("1. Check member sending request")
            print("2. Check advisor sending request")
            print("3. Check project's details")
            print("4. Check project's status")
            options = int(input('select options: '))
            if options in (0, 1, 2, 3, 4):
                return options
            else:
                print('Invalid options, Try again!')

    def member_menu(self):
        print('---Role : Member---')
        logins = my_DB.search('login')
        projects = my_DB.search('project')
        member_pending = my_DB.search('Member_pending_request')
        advisor_pending = my_DB.search('Advisor_pending_request')
        for i in projects.table:
            if i['Member1'] == self.person_id or i['Member2'] == self.person_id:
                print(f"Project's ID: {i['ProjectID']}")
        for k in projects.filter(lambda x: x['Member1'] == self.person_id or x['Member2'] == self.person_id).table:
            mem_name = logins.filter(lambda x: x['ID'] == i['Member1'] or x['ID'] == k['Member2']).table
            for m in range(len(mem_name)):
                print(f"Member{m + 1}: {mem_name[m]['username']}")
            adv_name = logins.filter(lambda x: x['ID'] == i['Advisor']).table
            for n in range(len(adv_name)):
                print(f"Advisor: {adv_name[n]['username']}")

        while True:
            option = self.option_member()
            for i in projects.filter(lambda x: x['Member1'] == self.person_id or x['Member2'] == self.person_id).table:
                if option == 1:
                    mem_pen = member_pending.filter(lambda x: x['ProjectID'] == i['ProjectID']).table
                    for name in range(len(mem_pen)):
                        pen_name = logins.filter(lambda x: x['ID'] == mem_pen[name]['to_be_member']).table
                        print(f"Name: {pen_name[0]['username'].ljust(15)}Response: {mem_pen[name]['Response']}")
                elif option == 2:
                    adv_pen = advisor_pending.filter(lambda x: x['ProjectID'] == i['ProjectID']).table
                    for name in range(len(adv_pen)):
                        adv_name = logins.filter(lambda x: x['ID'] == adv_pen[name]['to_be_advisor']).table
                        print(f"Name: {adv_name[0]['username'].ljust(15)}Response: {adv_pen[name]['Response']}")
                elif option == 3:
                    print(f"---Project's details---")
                    print(f"Title: {i['Title']}")
                    print(f"Details: {i['Detail']}")
                    print(f"Comment: {i['Comment']}")
                    if i['Status'] != 'Submit':
                        ans_de = input("Do you want to change project's details(y/n)? ")
                        if ans_de == 'y':
                            details = input("Please write your project's details: ")
                            i['Detail'] = details
                elif option == 4:
                    print(f"---Project's status: {i['Status']}---")
                elif option == 0:
                    for_login()


class Faculty:
    def __init__(self, person_id):
        self.person_id = person_id

    def option_faculty(self):
        while True:
            print('options:')
            print("0. Log-out")
            print("1. Evaluating projects")
            print("2. Check project's request")
            options = int(input('select options: '))
            if options in (0, 1, 2):
                return options
            else:
                print('Invalid options, Try again!')

    def faculty_menu(self):
        print('---Role : Faculty---')
        logins = my_DB.search('login')
        projects = my_DB.search('project')
        persons = my_DB.search('persons')
        advisor_pending = my_DB.search('Advisor_pending_request')
        while True:
            option = self.option_faculty()
            if option == 1:
                eva_pro = projects.filter(lambda x: x['Status'] == 'Submit' and x['Advisor'] != self.person_id).table
                for k in range(len(eva_pro)):
                    print(f"Project ID: {eva_pro[k]['ProjectID']} ({eva_pro[k]['Title']})")
                if len(eva_pro) != 0:
                    print("If you don't want to join any project, enter(0)")
                    eva_id = input("Please enter project ID which you want to evaluate: ")
                    real = projects.filter(lambda x: x['ProjectID'] == eva_id).table
                    if len(real) != 0:
                        lead_name = logins.filter(lambda x: x['ID'] == real[0]['Lead']).table
                        print(f"Leader: {lead_name[0]['username']}, Details: {real[0]['Detail']}")
                        approve = input("Do you want to approve this project?(y/n) ")
                        if approve == 'y':
                            number_count = int(real[0]['CountApprove'])
                            number_count += 1
                            if number_count >= 2:
                                real[0]['Status'] = 'Approve'
                            real[0]['CountApprove'] = number_count
                            print('Approved this project successfully.')

                else:
                    print('No project for evaluating!')

            elif option == 2:
                if len(advisor_pending.table) == 0 or len(projects.filter(lambda x: x['Advisor'] == 'Waiting').table) == 0:
                    print('No project request!\n')
                else:
                    for item2 in advisor_pending.table:
                        pro_fil = projects.filter(lambda x: (x['Status'] == 'Pending members'
                                                             or x['Status'] == 'Still in progress')
                                                            and x['ProjectID'] == item2['ProjectID']
                                                            and x['Advisor'] == 'Waiting').table
                        if item2['to_be_advisor'] == self.person_id and len(pro_fil) != 0:
                            print(f"Project ID: {item2['ProjectID']} ({pro_fil[0]['Title']})")
                    print("If you don't want to supervise any project, enter(0)")
                    ans = input('Please enter project ID which you want to supervise: ')
                    is_exist = False
                    for project in projects.table:
                        if ans == project['ProjectID']:
                            if project['Advisor'] == 'Waiting':
                                projects.update('ProjectID', ans, {'Advisor': self.person_id})
                                print("You are an advisor of this project.")

                            is_exist = True

                    if is_exist:
                        advisor_acc = advisor_pending.filter(
                            lambda x: x['to_be_advisor'] == self.person_id and x['ProjectID'] == ans).table
                        advisor_acc[0]['Response'] = 'accepted'
                        advisor_acc[0]['Response_date'] = current_date.__str__()

                        advisor_deny = advisor_pending.filter(
                            lambda x: x['ProjectID'] != ans and x['to_be_advisor'] == self.person_id).table
                        for advisor_d in advisor_deny:
                            advisor_d['Response'] = 'deny'
                            advisor_d['Response_date'] = current_date.__str__()

                        for item in logins.table:
                            if item['role'] == 'faculty':
                                logins.update('ID', self.person_id, {'role': 'advisor'})
                        persons.update('ID', self.person_id, {'type': 'advisor'})

                        print('Please log-out(0) and log-in again!\n')

                    else:
                        print('Invalid Project ID!')

            elif option == 0:
                for_login()

    def option_advisor(self):
        while True:
            print('options:')
            print("0. Log-out")
            print("1. Evaluating projects")
            print("2. Check project's details")
            print("3. Check project's status")
            options = int(input('select options: '))
            if options in (0, 1, 2, 3):
                return options
            else:
                print('Invalid options, Try again!')

    def advisor_menu(self):
        print('---Role : Advisor---')
        logins = my_DB.search('login')
        projects = my_DB.search('project')
        persons = my_DB.search('persons')
        for i in projects.table:
            if i['Advisor'] == self.person_id:
                print(f"Project's title: {i['Title']}")
        while True:
            options = self.option_advisor()
            if options == 1:
                eva_pro = projects.filter(lambda x: x['Status'] == 'Submit' and x['Advisor'] != self.person_id).table
                for k in range(len(eva_pro)):
                    print(f"Project ID: {eva_pro[k]['ProjectID']} ({eva_pro[k]['Title']})")
                if len(eva_pro) != 0:
                    eva_id = input("Please enter project ID which you want to evaluate: ")
                    real = projects.filter(lambda x: x['ProjectID'] == eva_id).table
                    if len(real) != 0:
                        lead_name = logins.filter(lambda x: x['ID'] == real[0]['Lead']).table
                        print(f"Leader: {lead_name[0]['username']}, Details: {real[0]['Detail']}")
                        approve = input("Do you want to approve this project?(y/n) ")
                        if approve == 'y':
                            number_count = int(real[0]['CountApprove'])
                            number_count += 1
                            if number_count >= 2:
                                real[0]['Status'] = 'Approve'
                            real[0]['CountApprove'] = number_count
                            print('Approved this project successfully.')

            elif options == 2:
                for check_pro in projects.filter(lambda x: x['Advisor'] == self.person_id).table:
                    print(f"Project ID: {check_pro['ProjectID']} ({check_pro['Title']})")
                    lead_name = logins.filter(lambda x: x['ID'] == check_pro['Lead']).table
                    print(f"Leader: {lead_name[0]['username']}")
                    mem_name = logins.filter(lambda x: x['ID'] == check_pro['Member1'] or x['ID'] == check_pro['Member2']).table
                    for m in range(len(mem_name)):
                        print(f"Member{m + 1}: {mem_name[m]['username']}")
                    print(f"Detail: {check_pro['Detail']}")
                    if check_pro['Status'] != 'Submit' and check_pro['Status'] != 'Approve' and check_pro['Status'] != 'Completed':
                        comment = input("Do you want to add comments?(y/n) ")
                        if comment == 'y':
                            comment_de = input("Please write the comment. ")
                            projects.update('Advisor', self.person_id, {'Comment': comment_de})

            elif options == 3:
                for j in projects.filter(lambda x: x['Advisor'] == self.person_id).table:
                    print(f"Status: {j['Status']}")
                    if j['Status'] == 'Approve':
                        complete = input("Do you want to change project's status to be completed?(y/n) ")
                        if complete == 'y':
                            print("The project is completed!")
                            projects.update('Advisor', self.person_id, {'Status': 'Completed'})
                            logins.update('ID', self.person_id, {'role': 'faculty'})
                            persons.update('ID', self.person_id, {'type': 'faculty'})

            elif options == 0:
                for_login()


class Admin:
    def __init__(self, person_id):
        self.person_id = person_id

    def option_admin(self):
        while True:
            print('---Role : Admin---')
            print('options:')
            print("0. Log-out")
            print("1. Delete project")
            print("2. Add person")
            print("3. Update CSV file and exit")
            options = int(input('select options: '))
            if options in (0, 1, 2, 3):
                return options
            else:
                print('Invalid options, Try again!')

    def admin_menu(self):
        logins = my_DB.search('login')
        projects = my_DB.search('project')
        persons = my_DB.search('persons')
        member_pending = my_DB.search('Member_pending_request')
        advisor_pending = my_DB.search('Advisor_pending_request')

        while True:
            options = self.option_admin()
            if options == 1:
                delete_pro = projects.filter(lambda x: x['Status'] == "Delete").table
                for i in range(len(delete_pro)):
                    delete_element = logins.filter(lambda x: x['ID'] == delete_pro[i]['Lead']
                                                             or x['ID'] == delete_pro[i]['Member1']
                                                             or x['ID'] == delete_pro[i]['Member2']).table
                    delete_adv = logins.filter(lambda x: x['ID'] == delete_pro[i]['Advisor']).table
                    for element in delete_element:
                        logins.update("ID", element['ID'], {'role': 'student'})
                        persons.update("ID", element['ID'], {'type': 'student'})
                    if len(delete_adv) > 0:
                        logins.update("ID", delete_adv[0]['ID'], {'role': 'faculty'})
                        persons.update("ID", delete_adv[0]['ID'], {'type': 'faculty'})

                    print(f"You have already deleted project ID: {delete_pro[i]['ProjectID']}")

            elif options == 2:
                fname = input("First name: ")
                lname = input("Last name: ")
                role = input("Role: ")
                while True:
                    new_id = random.randint(1000000,9999999)
                    check_id = persons.filter(lambda x: x['ID'] == new_id).table
                    if len(check_id) == 0:
                        break
                password = random.randint(1000,9999)
                username = f"{fname}.{lname[0]}"
                logins.table.append({
                    "ID": new_id,
                    "username": username,
                    "password": password,
                    "role": role
                })
                persons.table.append({
                    "ID": new_id,
                    "fist": fname,
                    "last": lname,
                    "type": role
                })
                print(f"You added {fname} {lname} role: {role} in database.")

            elif options == 3:
                update_file('project_table', projects.table)
                update_file('Advisor_pending_request', advisor_pending.table)
                update_file('Member_pending_request', member_pending.table)
                update_file('persons', persons.table)
                update_file('login', logins.table)
                print("***ALL CSV FILE ARE ALREADY UPDATED***")
                sys.exit()

            elif options == 0:
                for_login()


def update_file(name, table):
    if len(table) > 0:
        header = list(table[0].keys())
        file_path = f'{name}.csv'
        if os.path.exists(file_path):
            os.remove(file_path)

        my_file = open(file_path, 'w')
        writer = csv.writer(my_file)
        writer.writerow(header)
        for dictionary in table:
            writer.writerow(dictionary.values())
        my_file.close()
        myFile = open(file_path, 'r')
        myFile.close()


def for_login():
    while True:
        val = login()
        if val is not None:
            break
    if val[1] == 'student':
        student = Student(val[0])
        student.students_menu()
    elif val[1] == 'lead':
        lead = Student(val[0])
        lead.lead_menu()
    elif val[1] == 'member':
        member = Student(val[0])
        member.member_menu()
    elif val[1] == 'faculty':
        faculty = Faculty(val[0])
        faculty.faculty_menu()
    elif val[1] == 'advisor':
        advisor = Faculty(val[0])
        advisor.advisor_menu()
    elif val[1] == 'admin':
        admin = Admin(val[0])
        admin.admin_menu()


initializing()
for_login()

