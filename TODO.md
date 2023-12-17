# **Roles in final_project**

**Students**
  - See the invitation request to become members of already created projects
    - If the projects already have 2 members, the students will not see that projects request.
    - Accept or deny the request:
      - If the student accepts, he or she will be the members of that project.
      - If the student denies, he or she will come back to menu.
  - Create a project and become a leader.
    - Create the title (the leader can change it later)
    - Get the project ID following by the order when you created.
    - Status of the projects is 'Pending member'
    - Details of the projects is None
  - Log out: Back to log-in process

**Leader**
  - See project ID and username of members and advisor
  - See the students to whom the requests to be member have been sent to and their responses
  - See the faculties to whom the requests to be advisor have been sent to be advisor and their responses
  - See and modify project information
    - See title of the project: the leader can change the title.
    - See details of the project: the leader can change the details.
    - See comment from the advisor
    - Exception: If the project's status is 'Submit', no one can change any information of the project.
  - See project status
    - the leader can submit the project. 
  - Delete the project
    - If the leader decided to delete the project, admin will see 'delete' status and delete it
  - Log out: Back to log-in process

**Members**
  - See project ID and username of members and advisor
  - See the students to whom the requests to be member have been sent to and their responses
  - See the faculties to whom the requests to be advisor have been sent to be advisor and their responses
  - See project status 
  - See and modify project information
    - See title of the project
    - See details of the project: the members can change the details.
    - See comment from the advisor
    - Exception: If the project's status is 'Submit', no one can change any information of the project.
  - Log out: Back to log-in process

**Faculty**
  - Evaluate project
    - the faculties will see project ID from many projects which is submitted and choose project ID which they want to evaluate.
    - When they chose the project to evaluate, they will see leader's username and project's details
    - They can approve the project
      - if they approve that project, the status will be 'Approve'
  - See request to be an advisor of the project 
    - Accept or deny the request to be an advisor:
      - If the faculty accept the request, faculty will become an advisor of that project and deny other projects.
      - p.s. one advisor can supervise only one project until his project has completely done. After that he can supervise other project. 
  - Log out: Back to log-in process
  
**Advisor**
  - Evaluate project
    - the advisors will see project ID from many projects which is submitted and choose project ID which they want to evaluate.
    - Exception: the advisors can't evaluate the project which they supervise of.
    - When they chose the project to evaluate, they will see leader's username and project's details
    - They can approve the project
      - if they approve that project, the status will be 'Approve'
  - Check the project details which they supervise of.
    - See project information
        - Project ID, title, leader, member, details
        - An advisor can add comments
    - Check the project status which they supervise of.
      - See project status
      - If status is 'Approved', the advisor can change project's status to be 'Completed'
      - After the status is changed to be 'Completed', the advisor will come back to be normal faculty and can supervise other projects
  - Log out: Back to log-in process

**Admin**
  - Delete projects
    - If status of project is 'Delete', the admin will delete that project (the role of leader and members will become student and advisor will become faculty) 
  - Add person   
    - An admin needs to put first name, last name and role of new person
  - Update CSV file and exit program
    - p.s. By the end of the day, admin needs to select this option to update csv file
    - The updated csv file including:
      - person.csv
      - login.csv
      - Advisor_pending_request.csv
      - Member_pending_request.csv
      - project_table.csv
  - Log out: Back to log-in process

## Final project processes


  
   
    



