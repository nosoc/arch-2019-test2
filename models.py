
## peewee ORM
from peewee import *
## playhouse.hybrid is used
## in order allow define getters
## and methods
## inside peewee classes.
from playhouse.hybrid import *

## decorators like @hybrid_property
## and @hybrid_method allows this functionality

db_hr = SqliteDatabase('hr_2.db')
db_hr.connect()

class HR(Model):
    
    name = CharField()
    experience = FloatField()
    
    # getter for experience
    @hybrid_method
    def get_experience(self):
        return(self.experience)
            
    class Meta:
        database = db_hr # This model uses the "hr_2.db" database.


## update values
## before doing that, create candidates
## with status like "pending"

class Candidate(Model):
    
    reviewed_by = ForeignKeyField(HR, backref='candidates')

    name = CharField()
    experience = FloatField()

    ## for testing if claueses
    test_var = CharField(default="df")

    proceed_or_not = CharField(default="pending")
    decision = CharField(default="pending")
    
    @hybrid_property
    def get_name(self):
        return(self.name)
    
    # getter for experience
    # FIXME: might be rewritten using props
    @hybrid_method
    def get_experience(self):
        return(self.experience)

    @hybrid_method
    def get_proceed(self):
        return(self.proceed_or_not)

    # Define get outcome for candidate
    # given information about HR who
    # is reviewing the candidate 
    @hybrid_method
    def get_candidate_outcome(self, hr_person):
        ## first block
        if ((hr_person.get_experience() < 1) & (self.get_experience() < 1) & (self.get_proceed() == "proceed") ):
            self.decision = "ExtraRound"
            self.test_var = "firstblock"
        elif ((hr_person.get_experience() < 1) & (self.get_experience() < 1) & (self.get_proceed() == "notProceed") ):
            self.decision = "NoExtraRound"
            self.test_var = "firstblock"
        ## second block
        elif ((hr_person.get_experience() < 1) & (self.get_experience() > 1) & (self.get_proceed() == "proceed")):
            self.decision = "ExtraRound"
            self.test_var = "secondtblock"
        elif ((hr_person.get_experience() < 1) & (self.get_experience() > 1) & (self.get_proceed() == "notProceed")):
            self.decision = "ExtraRound"
            self.test_var = "secondtblock"
        ## third block
        elif ((hr_person.get_experience() > 1) & (self.get_experience() > 1) & (self.get_proceed() == "proceed")):
            self.decision = "ExtraRound"
            self.test_var = "thirdblock"
        elif ((hr_person.get_experience() > 1) & (self.get_experience() > 1) & (self.get_proceed() == "notProceed")):
            self.decision = "NoExtraRound"
            self.test_var = "thirdblock"
        ## last block
        elif ((hr_person.get_experience() > 1) & (self.get_experience() < 1) & (self.get_proceed() == "proceed") ):
            self.decision = "ExtraRound"
            self.test_var = "fourthblock"
        else:
            self.decision = "NoExtraRound"
            self.test_var = "fourthblock"
            # Return an outcome of the screening
        return(self.decision)
    
    class Meta:
        database = db_hr # This model uses the "hr_2.db" database.

db_hr.create_tables([HR, Candidate])
