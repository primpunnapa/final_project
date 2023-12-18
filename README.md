# Final project for 2023's 219114/115 Programming I

**A list of files in final project**
  - database.py
    - purpose: For calling useful functions to use in project_manage.py file
    - read_csv method 
      - For reading data from CSV file
    - Database class:
      - insert method 
        - Insert tables in database
      - search method 
        - Search tables in database
    - Table class:
      - filter method  
        - Filter tables
      - update method
        - Update tables with key and value and data in dictionary form
  - project_manage.py
    - purpose: For managing the process of each role in final project
    - login method
      - key username and password in this function, and it will return person ID and your role 
    - Student class:
      - options 
        - Display options of role 'student'
      - students_menu
        - Display information followed by the options that students choose (ex. 'check request' will display the project ID and title which is in 'Pending member' status.)
      - option_lead
        - Display options of role 'lead'
      - lead_menu
        - Display information followed by the options that leader chooses (ex. 'check project's details' will display the title, details and comment from an advisor.)
      - option_member
        - Display options of role 'member'
      - member_menu
        - Display information followed by the options that member chooses (ex. 'check project's status' will display the status of the project.)
    - Faculty class:
      - option_faculty
        - Display options of role 'faculty'
      - faculty_menu
        - Display information followed by the options that faculty chooses (ex. 'Check project's request' will display the project ID and title which is still waiting for an advisor.)
      - option_advisor
        - Display options of role 'advisor'
      - advisor_menu
        - Display information followed by the options that advisor chooses (ex. 'Evaluating projects' will display the project ID and title which is in 'submit' status bur not the one that he supervise of.)
    - Admin class:
      - option_admin
        - Display options of role 'admin'
      - admin_menu
        - Process operations followed by the options that admin chooses (ex. 'Delete project' will delete the projects which is in 'Delete' status.)
    - update_file
      - Update csv files by putting the file name and table
    - for_login
      - Make loop for login method
  - persons.csv
    - purpose: Collecting data including person ID, firstname, lastname and type of each person 
  - login.csv
    - purpose: Collecting data including person ID, username, password and role of each person
  - Advisor_pending_request.csv
    - purpose: Collecting data including project ID, faculty ID, response and response date of each faculty
  - Member_pending_request.csv
    - purpose: Collecting data including project ID, faculty ID, response and response date of each student
  - project_table.csv
    - purpose: Collecting data including project ID, project's title, project's detail, leader ID, member1 ID, member2 ID, advisor ID, status, comment, count_approve of each project
  - TODO.md
    - purpose: The details of each role menu and the process of each role
  - Proposal.md
    - purpose: The details of evaluate steps

**How my final project compile and run**

Run the program by project_manage.py file

1. Login
    - Key username and password, then the program will display your role's menu which you can select options depend on your role.
    - p.s. for username and password, you can choose from login.csv file
2. Menu
    - Display menu will depend on your role, for example if your role is student, your options have Log-out, the invitation request to become members and create a project.
    - For more details of menu, you can read in TODO.md
3. Exit
   - If you want to end the program, you need to log-in as admin and select option '3. Update CSV file and exit'.

**A table detailing each role and its actions**

| Role    | Action                                                                                                | Method         | Class   | Completion percentage |
|---------|-------------------------------------------------------------------------------------------------------|----------------|---------|-----------------------|
| Admin   | Delete project (by make the role of each person to original role)                                     | update         | Admin   | 90%                   |
| Admin   | Add person (Append row into login table and person table                                              | -              | Admin   | 95%                   |
| Admin   | Exit and update csv file                                                                              | update_file    | Admin   | 95%                   |
| student | invitation request to become members                                                                  | filter         | Student | 95%                   |
| student | create project (and send the invitation request to students , faculties)                              | update         | Student | 95%                   |
| Lead    | See the students to whom the requests to be member have been sent to and their responses              | filter         | Student | 80%                   |
| Lead    | See the faculties to whom the requests to be advisor have been sent to be advisor and their responses | filter         | Student | 80%                   |
| Lead    | See and modify project information                                                                    | -              | Student | 90%                   |
| Lead    | See project status                                                                                    | -              | Student | 90%                   |
| Lead    | Delete the project                                                                                    | -              | Student | 90%                   |
| Members | See the students to whom the requests to be member have been sent to and their responses              | filter         | Student | 80%                   |
| Members | See the faculties to whom the requests to be advisor have been sent to be advisor and their responses | filter         | Student | 80%                   |         |         |                       |
| Members | See and modify project information(only details)                                                      | -              | Student | 90%                   |
| Members | See project status                                                                                    | -              | Student | 95%                   |
| Faculty | Evaluate project                                                                                      | filter         | Faculty | 80%                   |
| Faculty | See request to be an advisor of the project                                                           | filter, update | Faculty | 80%                   |
| Advisor | Evaluate project                                                                                      | filter         | Faculty | 80%                   |
| Advisor | Check the project details which they supervise of.                                                    | filter         | Faculty | 80%                   |
| Advisor | Add comment                                                                                           | update         | Faculty | 90%                   |
| Advisor | Change status to be completed                                                                         | update         | Faculty | 80%                   |

**A list of missing features and outstanding bugs**

 - Admin doesn't have power to change name and password for the person who is already in database.
 - Admin doesn't have power to remove person from database.
 - If students select option 'check request' and they don't want to be member of any projects at that moment, they need to enter the project ID which is not display or enter(0) to go back to menu page.
 - If faculties select option 'Check project's request' and they don't want to supervise any projects at that moment, they need to enter the project ID which is not display or enter(0) to go back to menu page.
 - If faculties or advisors select option 'Evaluating projects' and they don't want to evaluate any projects at that moment, they need to enter the project ID which is not display or enter(0) to go back to menu page.
 - In case of 'evaluate steps':
   - If a faculty approved a project and doesn't have other faculties approve that project, the faculty who already approved that project still see the project ID of that project pending in 'evaluate project'.

