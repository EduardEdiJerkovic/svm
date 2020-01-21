from enum import Enum

class Condition(Enum):
    PRE = 0
    EASY = 1
    HARD = 2
    POST = 3

class Task(Enum):
    READING = 0
    ARITHMETIC = 1