## peewee ORM
from peewee import *
## playhouse.hybrid is used
## in order allow define getters
## and methods
## inside peewee classes.
from playhouse.hybrid import *


db_hr = SqliteDatabase('hr_3.db')
db_hr.connect()

from models import Candidate, HR
## decorators like @hybrid_property
## and @hybrid_method allows this functionality



class Candidate_New(Candidate):
    # weird_field = CharField()

    @hybrid_method
    def test_method_for_inheritance(self):
        return("1")



class HR_New(HR):
    timeSlot = CharField()

    # @hybrid_method
    # def test_method_for_inheritance(self):
    #     return("1")




db_hr.create_tables([Candidate_New])
