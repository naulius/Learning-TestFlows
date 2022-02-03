"""
Defining scenarios with multiple steps.
"""
from testflows.core import Scenario, Given, When, Then, note

with Scenario ("my scenario"):
    with Given("I have something"):
        note("I got something")
    with When ("I do something"):
        note("I did something")
    with Then ("I check something"):
        note("I checked something")
