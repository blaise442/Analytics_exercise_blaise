# Analytics exercise

The purpose of this exercise is to demonstrate the following:

- Ability to create normalized Django models
- Ability to parse and load denormalized data into Django models
- Ability to query a database using the Django ORM

## Instructions

0. Install dependencies using `python3 -m pip install -r requirements.txt`
1. Complete `TODO` in `analytics/apps/patients/models.py` by adding normalized models to represent the data in the provided `events.csv` file
2. Complete `TODO` in `analytics/apps/patients/management/commands/load_patient_data.py` to populate the database from the provided `events.csv` file
3. Complete `TODO` in `analytics/apps/patients/views.py` to return aggregate statistics

### Create models

Complete the `TODO` in `analytics/apps/patients/models.py` by adding normalized models to store the data provided in `events.csv`. Each row in the CSV contains a patient ID, patient name, and the details of a clinical event like heart rate or respiratory rate measurement.

### Load data

Complete the `TODO` in `analytics/apps/patients/management/commands/load_patient_data.py` to populate the database from the provided `events.csv` file

### Return aggregate statistics

Complete the `TODO` in `analytics/apps/patients/views.py` to return the following aggregate statistics for each patient:

- mininum clinical event value, grouped by patient and event type
- maximum clinical event value, grouped by patient and event type
- average clinical event value, grouped by patient and event type
- count of clinical events, grouped by patient and event type
- oldest clinical event, grouped by patient and event type
- newest clinical event, grouped by patient and event type

Annotate each set of aggregate statistics with the patient's ID and name.

## Show your work

Fork this repository, push your work in a branch, and create a pull request on Github with your solution.

We will do the following:
- pull your code
- install any dependencies declared in `requirements.txt`
- run `python3 manage.py migrate`
- run `python3 manage.py load_patient_data`
- load `http://127.0.0.1/query/` to view your results
- provide a review for your PR
