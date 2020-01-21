from models.feature import Feature
from models.constants import READING, ARITHMETIC, PRE, LOW, HIGH, POST
from models.enums import Task, Condition

def ExtractData(sheet):
    i = 3
    data = []
    while(True):
        try:
            sheet.cell_value(i, 0)
        except IndexError:
            break

        f = Feature()
        f.name = sheet.cell_value(i, 0).strip()
        f.task = ExtractTask(sheet, i)
        f.condition = ExtractCondition(sheet, i)
        data.append(f)

        i += 1

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