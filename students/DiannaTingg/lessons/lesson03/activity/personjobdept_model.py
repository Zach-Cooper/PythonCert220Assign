"""
Simple database example with Peewee ORM, sqlite and Python
Here we define the schema
Use logging for messages so they can be turned off
"""

import logging
from peewee import SqliteDatabase, Model, CharField, DateField, DecimalField, ForeignKeyField

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info('Here we define our data (the schema).')
logger.info('First name and connect to a database (sqlite here).')

database = SqliteDatabase('personjobdept.db')
database.connect()
database.execute_sql('PRAGMA foreign_keys = ON;')  # needed for sqlite only


class BaseModel(Model):
    class Meta:
        database = database


class Person(BaseModel):
    """
    This class defines Person, which maintains details of someone
    for whom we want to research career to date.
    """
    logger.info("Specifying details for the Person class.")

    person_name = CharField(primary_key=True, max_length=30)
    lives_in_town = CharField(max_length=40)
    nickname = CharField(max_length=20, null=True)


class Job(BaseModel):
    """
    This class defines Job, which maintains details of past Jobs
    held by a Person.
    """
    logger.info('Specifying the details for the Job class.')

    job_name = CharField(primary_key=True, max_length=30)
    start_date = DateField(formats='YYYY-MM-DD')
    end_date = DateField(formats='YYYY-MM-DD')
    salary = DecimalField(max_digits=7, decimal_places=2)
    person_employed = ForeignKeyField(Person, related_name='was_filled_by', null=False)


class Department(BaseModel):
    """
    This class defines a Department for a Job.
    """
    logger.info("Specifying the details for the Department class.")

    dept_num = CharField(primary_key=True, max_length=4)
    dept_name = CharField(max_length=30)
    dept_manager = CharField(max_length=30)
    job_employed = ForeignKeyField(Job, related_name="contains_job", null=False)


class PersonNumKey(BaseModel):
    """
    This class defines Person, which maintains details of someone
    for whom we want to research career to date.
    """
    logger.info('Specifying an alternate Person class.')
    person_name = CharField(max_length=30)
    lives_in_town = CharField(max_length=40)
    nickname = CharField(max_length=20, null=True)
