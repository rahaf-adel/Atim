# Project Name: Atim

## Idea:
A system to help university graduate students find work, help universities improve education outcomes and help companies find Saudi workers.

## Inspiration:
The inspiration came from a reality in which most recent graduates live, where they find it difficult to find a suitable job due to the lack of experience and qualifications to get a job.

## Goals:
- Facilitate the process of finding a job for graduate students and reduce financial and age waste.
- Improving university education curricula and outcomes, and determining the majors available for admission for the next year, according to unemployment rates.
- Increasing the percentage of Saudization in companies, and facilitating the finding of Saudi graduate students with the appropriate specializations for training and employment.

## List of Services / Features:

- Manage universities . 
- Manage companies . 
- Manage the graduate students.


## User Stories
- Type of users: Admin, Universities, Companies, and Graduate Students.

### Admin

- Create, Read, Update, Delete Universities. 
- Create, Read, Update, Delete Companies. 
- Create, Read, Update, Delete Graduate students.
- Create, Read, Update, Delete Job offer.


### Universities staff
•	Add university to the system.
•	Edit university.
•	Delete university.
•	View student information by university.
•	View student status by university.

### Companies staff
•	Add company to the system.
•	Edit company.
•	Delete company.
•	See graduate students information.
•	Send job offer for students.

### Graduate Students Staff
•	Add graduate students to the system.
•	Edit graduate students information.
•	Delete graduate students from the system.
•	View all the information of graduate students who added them.
•	Search for graduate students by Major.

### Students
•	View his information and status.
•	Accept or reject the job offer.


### Models
#University 
  - Name 
  - Description
  - City
  - User
  
#Company
  - Name
  - Description
  - City
  - User

#Student
  - First name
  - Last name
  - email
  - Major
  - GPA
  - Gradute Date
  - University
  - User


#Job_Offer
  - Name 
  - Description
  - Company
  - Student 
  - isAccepted #boolean




