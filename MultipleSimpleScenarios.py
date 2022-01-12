"""How to define multiples simple scenarios, only one top level test is allowed.
"""
from testflows.core import Scenario, note

with Scenario("Regression"):
    with Scenario("Hello TestFlows"):
        note("Hola amigo")
        note("Te amo Vitashka")
        note("Te amo Elena")
        for i in range(10):
            note("Te amo Iza " + str(i))
        assert 1 != 2

    with Scenario("Hello loco mundo"):
        note("El loco mundo esta")
        note("Las ideologias")

    with Scenario("La loca vida"):
        pass


