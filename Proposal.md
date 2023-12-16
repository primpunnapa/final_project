# Evaluate projects

1. When students choose to create the project, he/she will be leader of that project and a default status of the project is 'pending member'.
2. When the projects have a leader and two members, the status will be 'still in progress'.
   - p.s.1 The project doesn't require members, only leader is enough to manage it.
   - p.s.2 At most 2 members (1 leader) per project
   - p.s.3 Each project must have only one faculty to supervise it.
3. While the status of the project is between 'pending member' and 'still in progress', An advisor of that project can check and add comments to her own project. 
4. After the project has been done by member, the leader is the one who can 'submit' the project to other faculties.
   - p.s. If the project's status is submitted, no one can change details(ex. title) of the project.
5. The status of projects must be 'submit', so the faculties can evaluate them.
   - exception: The advisor can't evaluate the project that he or she supervises of.
   - While project's status is 'submit', an advisor can't add more comments.
6. If at least two faculties 'approve' the projects, the project's status will be 'approved'.
7. After the project has been approved by faculties, the advisor of the project will check and change the status to be 'completed'
8. When the status of projects turn to be 'completed', it means the project completely done.
9. In case of 'delete' status
   - The leader is the only one who can delete the project. If he/she decides to delete, the status will be 'delete'.
   - An admin will delete the project from database.

#### **Conclusion**

I have 6 status for Project's status :
1. Pending member : default status
2. Still in progress : projects has 2 member
3. Submit : a leader submitted the project
4. Approve : at least 2 faculties approved the project
5. Completed : an advisor does it after projects status is 'approve'
6. Delete : a leader decided to delete the project
   
