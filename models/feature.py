from models.enums import Condition

class Feature:
    def __init__(self, name="", task="", condition= Condition.PRE, order=0, isHrValid=False, isScValid=False, fHr=[], fSc=[]):
        self.name = name
        self.task = task
        self.condition = condition
        self.order = order
        self.isHrValid = isHrValid
        self.isScValid = isScValid
        if (len(fHr) != 0):
            self.fHr1 = fHr[0]
            self.fHr2 = fHr[1]
            self.fHr3 = fHr[2]
            self.fHr4 = fHr[3]
            self.fHr5 = fHr[4]
            self.fHr6 = fHr[5]
            self.fHr7 = fHr[6]
        if (len(fSc) != 0):
            self.fSc1 = fSc[0]
            self.fSc2 = fSc[1]
            self.fSc3 = fSc[2]
            self.fSc4 = fSc[3]
            self.fSc5 = fSc[4]
            self.fSc6 = fSc[5]

    def __repr__(self):
        return "Feature({0}, {1}, {2})".format(self.name, self.task, self.condition)
