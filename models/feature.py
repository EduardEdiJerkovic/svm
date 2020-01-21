from models.enums import Condition

class Feature:
    def __init__(self, name="", task="", condition= Condition.PRE, order=0, isHrValid=False, isScValid=False, fHr=[], fSc=[]):
        self.name = name
        self.task = task
        self.condition = condition
        self.order = order
        self.isHrValid = isHrValid
        self.isScValid = isScValid
        self.fHr = fHr
        self.fSc = fSc

    def __repr__(self):
        return "Feature({0}, {1}, {2}, order: {3})".format(self.name, self.task, self.condition, self.order)
