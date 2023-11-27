**Roles in final_project**

1. Students
  1.1 See the requests to become members of already created projects
  1.2 Accept or deny the request:
    - If the student accepts, he or she will be the members of that project.
    - Member_pending_request table needs to be updated.
    - Project table needs to be updated.
  1.3 Create a project and become a lead (must deny all member requests first):
    - Project table needs to be updated
    - Login table needs to be updated
    - If more members needed, send out requests and update the member_pending_request table; 
      requests can only go to those whose role is student (i.e., not yet become a member or a lead)

2. Lead 
  2.1 See project status (ex. pending member, pending advisor, or ready to solicit an advisor)
  2.2 See and modify project information:
    - Project table needs to be updated
  2.3 See who has responded to the requests sent out:
  2.4 Send out requests to potential members:
    - Member_pending_request table needs to be updated
  2.5 Send out requests to faculty to supervise the project; 
      can only do one at a time and after all members have accepted or denied the requests to join in the projects.
    - Advisor_pending_request table needs to be updated

3. Members
  3.1 See project status (ex. pending member, advisor)
  3.2 See and modify project information
    - Project table needs to be updated
  3.3 See who has responded to the requests sent out

4. Faculty
  4.1 See request to supervisor the project
  4.2 Accept or deny the request to be an advisor:
    - If the faculty accept, faculty will be an advising faculty of that project.
    - Advisor_pending_request table needs to be updated
    - Project table needs to be updated.
  4.3 See details of all the projects
  4.4 Evaluate project

5. Advisor
  5.1 See request to be a supervisor
    - Send deny response (for projects not eventually serving as an advisor)
    - Advisor_pending_request table needs to be updated
  5.2 See details of all the projects
  5.3 Evaluate project
  5.4 Approve the project
   - Project table needs to be updated

6. Admin
  6.1 Managing the database
    - See all the tables
   







