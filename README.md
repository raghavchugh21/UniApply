# UniApply

My Microsoft Engage FTE 2021 submission on Problem Statement :

**Build a functional prototype of a platform that gives students an array of digital academic and social tools to stay engaged with their studies, peers and broader university community during pandemic.**

My Submission :

**UniApply :** Functional prototype of a job portal which can be used by the students and faculty members of the respective university where the Faculties can post on-campus jobs (Eg. Research Assistant, Teaching Assistant) on the portal and the student can directly apply for the job position from the job portal. College grades have also been integrated in this portal as they are usually very helpful in the selection of candidates for these jobs.

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

Database
```
Set database configuration from settings.py
```

Migrate the database and collect the static files
```
python manage.py makemigrations
python manage,py migrate
python manage.py collectstatic
```

## Features

> To be added

## Screenshots

> To be added

## Design

> To be added