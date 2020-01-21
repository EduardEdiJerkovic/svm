from models.feature import Feature
from models.constants import READING, ARITHMETIC, PRE, LOW, HIGH, POST
from models.enums import Task, Condition

def ExtractData(sheet):
    data = []
    for i in range(2, sheet.nrows):
        sheet.cell_value(i, 0)


        f = Feature()
        f.name = sheet.cell_value(i, 0).strip()
        f.task = ExtractTask(sheet, i)
        f.condition = ExtractCondition(sheet, i)
        f.order = int(sheet.cell_value(i, 3).strip())
        f.isHrValid = ExtractHrValid(sheet, i)
        f.isScValid = ExtractHrValid(sheet, i)
        data.append(f)

    return data


def ExtractTask(sheet, index):
    value = sheet.cell_value(index, 1).strip()
    if value == READING:
        return Task.READING
    if value == ARITHMETIC:
        return Task.ARITHMETIC

def ExtractCondition(sheet, index):
    value = sheet.cell_value(index, 2).strip()
    if value == PRE:
        return Condition.PRE
    if value == POST:
        return Condition.POST
    if value == LOW:
        return Condition.LOW
    if value == HIGH:
        return Condition.HIGH

def ExtractHrValid(sheet, index):
    return ExtractFlag(sheet, index, 10) == 1

def ExtractScValid(sheet, index):
    return ExtractFlag(sheet, index, 11) == 1

def ExtractFlag(sheet, row, column):
    return int(sheet.cell_value(row, column).strip())


    