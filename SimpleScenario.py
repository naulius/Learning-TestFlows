"""
Simple Scenario which contains multiple instructions.
"""
from testflows.core import Scenario, note

with Scenario("Hello TestFlows"):
    note("Hola amigo")
    note("Te amo Vitashka")
    note("Te amo Elena")
    for i in range(10):
        note("Te amo Iza " + str(i))
    assert 1 != 2