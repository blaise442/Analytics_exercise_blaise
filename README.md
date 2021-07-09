# Analytics exercise

The purpose of this exercise is to demonstrate the following:

- Ability to create normalized Django models
- Ability to parse and load denormalized data into Django models
- Ability to query a database using the Django ORM

Our intention is to provide sufficient scaffolding that you should be able to complete this exercise in 30-60 minutes. If you find yourself spending significantly more time than that, please ask questions rather than continuing to struggle. We respect your time and don't want to waste it. Thanks for your interest in Decisio!

## Instructions

### Create models

Complete the `TODO` in `analytics/apps/patients/models.py` by adding normalized models to store the data provided in `events.csv`. Each row in the CSV contains a patient ID, patient name, and the details of a clinical event like heart rate or respiratory rate measurement.

You will need to run `python3 manage.py makemigrations` and `python3 manage.py migrate` to install your models. See Django's docs on [using models](https://docs.djangoproject.com/en/3.2/topics/db/models/#using-models) if you need additional help.

### Load data

Complete the `TODO` in `analytics/apps/patients/management/commands/load_patient_data.py` to populate the database from the provided `events.csv` file.

Run `python3 manage.py load_patient_data` to test your script.

For more info (probably not needed for this exercise), read about Django's [custom management commands](https://docs.djangoproject.com/en/3.2/howto/custom-management-commands/).

### Return aggregate statistics

Complete the `TODO` in `analytics/apps/patients/views.py` to return the following aggregate statistics for each patient:

- mininum clinical event value, grouped by patient and event type
- maximum clinical event value, grouped by patient and event type
- average clinical event value, grouped by patient and event type
- count of clinical events, grouped by patient and event type
- time of earliest clinical event, grouped by patient and event type
- time of latest clinical event, grouped by patient and event type

Annotate each set of aggregate statistics with the patient's ID and name.

Run `python3 manage.py runserver` and load `http://127.0.0.1/query/` in your browser to test your queries. See Django's tutorial on the [development server](https://docs.djangoproject.com/en/3.2/intro/tutorial01/#the-development-server) if you need help.

## Show your work

Fork this repository, push your work in a branch, and create a pull request on Github with your solution.

We will do the following:
- pull your code
- install any dependencies declared in `requirements.txt`
- run `python3 manage.py migrate`
- run `python3 manage.py load_patient_data`
- run `python3 manage.py runserver`
- load `http://127.0.0.1/query/` to view your results
- provide a review for your PR
