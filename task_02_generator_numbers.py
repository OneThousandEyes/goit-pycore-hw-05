import re
from typing import Callable


def generator_numbers(text: str):
    '''Generator function that extracts floating-point numbers from a given text.'''
    pattern = r'(?<=\s)-?\d+(?:.\d+)?(?=\s)'
    numbers = re.findall(pattern, text)
    for number in numbers:
        yield float(number)


def sum_profit(text: str, func: Callable):
    '''Function that sums up all floating-point numbers extracted by the generator function.'''
    return sum(func(text))


text = '''Загальний дохід працівника складається з декількох частин: 1000.01 як
основний дохід, доповнений додатковими надходженнями 232 і 324.00000
доларів та витратами на оренду офісного приміщення -222.22 доларів.'''

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
