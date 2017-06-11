# file:features/steps/strlib.py
# -----------------------------------------------------------------------------
# DOMAIN-MODEL:
# -----------------------------------------------------------------------------


class StrLib(object):
    def __init__(self):
        self.returned = None

    def set_string(self):
        self.returned = "Hello world"

    def set_two_strings(self):
        self.returned = ("value1", "value2")