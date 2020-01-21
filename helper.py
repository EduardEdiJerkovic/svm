from models.feature import Feature
from models.constants import READING, ARITHMETIC, PRE, LOW, HIGH, POST
from models.enums import Task, Condition

def ExtractData(data):
    f = Feature()
    f.name = data[0].strip()
    f.task = ExtractTask(data)
    f.condition = ExtractCondition(data)
    f.order = int(data[3].strip())
    f.isHrValid = ExtractHrValid(data)
    f.isScValid = ExtractHrValid(data)
    f.fHr = EctractHr(data)
    f.fSc = EctractSc(data)

    return f


def ExtractTask(data):
    value = data[1].strip()
    if value == READING:
        return Task.READING
    if value == ARITHMETIC:
        return Task.ARITHMETIC

def ExtractCondition(data):
    value = data[2].strip()
    if value == PRE:
        return Condition.PRE
    if value == POST:
        return Condition.POST
    if value == LOW:
        return Condition.LOW
    if value == HIGH:
        return Condition.HIGH

def ExtractHrValid(data):
    return ExtractFlag(data, 10) == 1

def ExtractScValid(data):
    return ExtractFlag(data, 11) == 1

def ExtractFlag(data, index):
    return int(data[index].strip())

def EctractHr(data):
    result = []
    for i in range (15, 22):
        try:
            value = float(data[i].strip())
        except TypeError:
            value = 0

        result.append(value)

    return result

def EctractSc(data):
    result = []
    for i in range (22, 28):
        try:
            value = float(data[i].strip())
        except TypeError:
            value = 0

        result.append(value)

    return result


    