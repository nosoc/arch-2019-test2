## using peewee - ORM

## TODO: make it time slots variable


from behave import *

# Add the models folder path to the sys.path list
import sys
sys.path.append('~/arch2019-test/hr-example-with-peewee')
# Now you can import your module
from models_ext_js01 import *

## given statement
@given(u'test given clause')
def step_impl(context):
    context.hr1 = HR.create(name='J1', experience=2)
    context.candidate1 = Candidate_New.create(reviewed_by=context.hr1, name="C1", experience=3)
    context.id_hr = context.hr1.id
    context.id_candidate = context.candidate1.id
    
## when part
@when("test given when")
def step_impl(context):
    assert (context.candidate1.test_method_for_inheritance() == "1")

## get results from queries
## two statuses: ExtraRound NoExtraRound
@then("then {roundstatus}")
def step_impl(context, roundstatus):
    assert (context.candidate1.test_method_for_inheritance() == "1")
    # Print the outcome
    # query = (Candidate
    #          .select(Candidate, HR)
    #          .join(HR)
    #          .where(Candidate.id == context.id_candidate))

    

    ## in case of test failure
    ## relevant fields are printed
    # for item in query:
    #     context.scanning_results = item.decision
    #     assert (context.scanning_results == roundstatus)
