# **Roles in final_project**

**Students**
  - See the requests to become members of already created projects
    - If the projects already have 2 members, the students will not see that projects request.
    - Accept or deny the request:
      - If the student accepts, he or she will be the members of that project.
      - If the student denies, he or she will come back to menu.
  - Create a project and become a lead.
    - create the title (the students can change later)
    - Got the project ID following by the order when you created.
    - Status of the projects is 'Pending member'
    - Details of the projects is None
  - Log out: Back to log-in process

Lead
  - See ID's project and username of members and advisor
  - See the student who have been sent the request to be member and the response
  - See the faculty who have been sent the request to be advisor and the response
  - See and modify project information
    - See title of the project: the leader has chances to change the title
    - See details of the project: the leader has chances to change the details.
    - See comment from the advisor
    - Exception: If the project's status is 'Submit', no one can change any information of the project
  - See project status
    - the leader has a chance to submit the project. 
  - Delete the project
    - If the leader decided to delete the project, admin will see 'delete' status and delete it
  - Log out: Back to log-in process
  

Members
  - See ID's project and username of members and advisor
  - See the student who have been sent the request from leader to be member and the response
  - See the faculty who have been sent the request from leader to be advisor and the response
  - See project status 
  - See and modify project information
    - See title of the project
    - See details of the project: the members have chances to change the details.
    - See comment from the advisor
    - Exception: If the project's status is 'Submit', no one can change any information of the project
  - Log out: Back to log-in process


Faculty
  - Evaluate project
    - the faculties will see projects id from many projects which is submitted and choose projects id which they want to evaluate.
    - When they chose the evaluating project, they will see leader's username and project's details
    - They have chances to approve the project
      - if they approve that project, the status will be 'Approve'
  - See request to be an advisor of the project 
    - Accept or deny the request to be an advisor:
      - If the faculty accept, faculty will be an advising faculty of that project and deny other projects.
      - p.s. one advisor can supervise only one project until his project has completely done. After that he can supervise other project. 
  - Log out: Back to log-in process
  
Advisor
  - Evaluate project
    - the advisors will see projects id from many projects which is submitted and choose projects id which they want to evaluate.
    - Exception: the advisors can't evaluate the project which they supervise of.
    - When they chose the evaluating project, they will see leader's username and project's details
    - They have chances to approve the project
      - if they approve that project, the status will be 'Approve'
  - Check the project details which they supervise of.
    - See project information
        - Project ID, title,  leader, member, details
        - An advisor has chances to add comments
    - Check the project status which they supervise of.
      - See project status
      - If status is 'Approved', the advisor will have a chance to change project's status to be 'completed'
      - After the status change to be 'completed', the advisor will come back to be normal faculty and can supervise other projects
  - Log out: Back to log-in process

Admin
  - Delete projects
    - If status of project is 'Delete', the admin will delete that project (the role of leader, member come back to be student and advisor come back to be faculty) 
  - Add person   
    - An admin needs to put first name, last name and role of new person
  - Update CSV file and exit program
    - p.s. By the end of the day, admin need to select this option to update csv file
    - The updated csv file including:
      - person.csv
      - login.csv
      - Advisor_pending_request.csv
      - Member_pending_request.csv
      - project_table.csv
  - Log out: Back to log-in process
  
   
    



