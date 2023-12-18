# Final project for 2023's 219114/115 Programming I

**A list of files in final project**
  - database.py
    - purpose: For calling useful functions to use in project_manage.py file
  - project_manage.py
    - purpose: For managing the process of each role in final project
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
    - purpose: The evaluation steps

**How my final project compile and run**

1. Login
    - Key username and password, then the program will display your role's menu which you can select your options of your role.
2. Menu
    - Display menu will depend on your role, for example if your role is student, your options have Log-out, the invitation request to become members and create a project)
    - For more details of menu, you can read in TODO.md
    - In case of 'Admin menu': it has 'exit' to end the program and update csv file

| Role   | Action                                                                                                | Method         | Class   | Completion percentage |
|--------|-------------------------------------------------------------------------------------------------------|----------------|---------|-----------------------|
| Admin  | Delete project (by make the role of each person to original role)                                     | update         | Admin   | 90                    |
| Admin  | Add person (Append row into login table and person table                                              | -              | Admin   | 95                    |
| Admin  | Exit and update csv file                                                                              | update_file    | Admin   | 95                    |
| student | invitation request to become members                                                                  | filter         | Student | 95                    |
| student | create project (and send the invitation request to students , facultise)                              | update         | Student | 85                    |
| Lead   | See the students to whom the requests to be member have been sent to and their responses              | filter         | Student | 80                    |
| Lead   | See the faculties to whom the requests to be advisor have been sent to be advisor and their responses | filter         | Student | 80                    |
| Lead   | See and modify project information                                                                    | -              | Student | 80                    |
| Lead   | See project status                                                                                    | -              | Student | 80                    |
| Lead   | Delete the project                                                                                    | -              | Student | 80                    |
| Members| See the students to whom the requests to be member have been sent to and their responses              | filter         | Student | 80                    |
| Members   | See the faculties to whom the requests to be advisor have been sent to be advisor and their responses | filter         | Student | 80                    |         |         |                       |
| Members | See and modify project information(only details)                                                      | -              | Student | 80                    |
| Members   | See project status                                                                                    | -              | Student | 80                    |
| Faculty   | Evaluate project                                                                                      | filter         | Faculty | 80                    |
| Faculty   | See request to be an advisor of the project                                                           | filter, update | Faculty | 80                    |
| Advisor   | Evaluate project                                                                                      | filter         | Faculty | 80                    |
| Advisor   | Check the project details which they supervise of.                                                    | filter         | Faculty | 80                    |
| Advisor   | Add comment                                                                                           | update         | Faculty | 80                    |
| Advisor   | Change status to be completed                                                                         | update         | Faculty | 80                    |

