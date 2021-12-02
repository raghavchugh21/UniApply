
# UniApply

My Microsoft Engage FTE 2021 submission on Problem Statement :

**Build a functional prototype of a platform that gives students an array of digital academic and social tools to stay engaged with their studies, peers and broader university community during pandemic.**

My Submission :

**UniApply :** Functional prototype of a job portal which can be used by the students and faculty members of the respective university where the Faculties can post on-campus jobs (Eg. Research Assistant, Teaching Assistant) on the portal and the student can directly apply for the job position from the job portal. College grades have also been integrated in this portal as they are usually very helpful in the selection of candidates for these jobs.

## Hosted Web App

Usage : [Demo Video](https://vimeo.com/650750639)

Admin ( Moderator ) Account :
```
Email : admin@uniapply.com
Password : supersecure
```

Teacher Account :
```
Email : pandurangan@lnmiit.ac.in
Password : supersecure
```

Student Account :
```
Email : 18ucs105@lnmiit.ac.in
Password : supersecure
```

Try it out! <br> [Link to Web App](https://uniapply.herokuapp.com/)

## Installation

Create Anaconda Environment
```
conda create -n env python=3.7.10
conda activate env
```

Clone Github Repository
```
git clone https://github.com/raghavchugh21/UniApply.git
cd UniApply/
```

Install Requirements
```
pip install -r requirements.txt
```

The course list and email data used is fetched from <b>media/json/course_data.json</b> and <b>media/json/email_data.json</b>

Database
```
Set database configuration from settings.py
```

Migrate the database and collect the static files
```
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
```

## Features

<br>
<p align="center">
  <img src="https://user-images.githubusercontent.com/65908705/143215313-ac5fe95d-3189-4421-8cb4-ef683957873d.png" />
</p>
<br>

## Screenshots

<details>
  <summary> Homepage </summary>
  <img src="https://user-images.githubusercontent.com/65908705/143259130-711339c6-07ec-485e-b775-507292a31f90.png" name="image-name">
</details>

<details>
  <summary> Job View (as teacher)</summary>
  <img src="https://user-images.githubusercontent.com/65908705/143260013-ef5071eb-74e8-4dea-b51b-0b034bc26a58.png" name="image-name">
</details>

<details>
  <summary> Job View (as student) </summary>
  <img src="https://user-images.githubusercontent.com/65908705/143260345-a69c9d2d-7df8-421f-9412-979df53ccbb9.png" name="image-name">
</details>

<details>
  <summary> Dashboard (as student) </summary>
  <img src="https://user-images.githubusercontent.com/65908705/143260223-6c655619-6ebd-4de5-975c-00be96676a7b.png" name="image-name">
</details>

<details>
  <summary> Dashboard (as teacher) </summary>
  <img src="https://user-images.githubusercontent.com/65908705/143260108-4873e631-8fe6-4c3a-ab06-3a562286af45.png" name="image-name">
</details>

## Design

<br>
<p align="center">
  <img src="https://user-images.githubusercontent.com/65908705/143260575-7ab05501-db2e-4985-8fa5-f88cd8e085d5.png" />
</p>
<br>

## Future Scope

<ul>
  <li> Using resume section for Students to find matching jobs for students (using keywords) so that they can be brought on top </li>
  <li> Using further intelligence to recommend related jobs below a certain job to a student </li>
</ul>
