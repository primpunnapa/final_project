**Roles in final_project**

Students
  - See the requests to become members of already created projects
  - Accept or deny the request:
    - If the student accepts, he or she will be the members of that project. 
  - Create a project and become a lead (must deny all member requests first):

Lead 
  - See project status (ex. pending member, pending advisor, or ready to solicit an advisor)
  - See and modify project information
  - See who has responded to the requests sent out
  - Send out requests to potential members
  - Send out requests to faculty to supervise the project

Members
  - See project status (ex. pending member, advisor)
  - See and modify project information
  - See who has responded to the requests sent out

Faculty
  - See request to supervisor the project 
  - Accept or deny the request to be an advisor:
    - If the faculty accept, faculty will be an advising faculty of that project.
  - See details of all the projects 
  - Evaluate project

Advisor
  - See request to be a supervisor
    - Send deny response (for projects not eventually serving as an advisor)
    - Advisor_pending_request table needs to be updated
  - See details of all the projects
  - Evaluate project
  - Approve the project
   - Project table needs to be updated

Admin
  - Managing the database
    - See all the tables
    - Adjust the data (ex. change the name, change password)
   

**status**
1. Pending members
    if member = 2 --> Still in progress
2. Submit --> leader submit the project
3. Approve --> faculties approve projects (after leader submit the project)
    if faculties approve >= 2 --> Advisor will change status to completed
4. Completed --> advisor does it
5. Delete --> leader want to delete project --> admin will delete it.
6. Either 'Pending members' or 'Still in progress' --> Advisor can check
7. Faculties can evaluate every project except the one that they supervis.

**อย่าลืมหาทางเก็บคอมเมนต์กับapprove --> completed

*member leave the project --> member_pending[Response] == 'Left' (projectตัวเอง)
                            --> admin check --> เอาเมมออก 
                            --> member_pending[Response] == None (project อื่น)

***อย่าลืมดัก projectid ห้ามเหมือนกัน --> completed
***update file --> มีไฟล์ = update data
                --> ไม่มีไฟล์ = create ใหม่


