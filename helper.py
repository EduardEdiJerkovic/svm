from models.feature import Feature
from models.constants import READING, ARITHMETIC
from models.enums import Task

def ExtractData(sheet):
    i = 3
    data = []
    while(True):
        try:
            sheet.cell_value(i, 0)
        except IndexError:
            break

        f = Feature()
        f.name = sheet.cell_value(i, 0)
        f.task = ExtractTask(sheet, 1)
        data.append(f)

        i += 1

    return data


def ExtractTask(sheet, index):
    value = sheet.cell_value(index, 1)
    if value == READING:
        return Task.READING
    if value == ARITHMETIC:
        return Task.ARITHMETIC