from random import random, choice
from dictionary import ALPHABET
from mocker.exception import count_must_grater_than_zero


@count_must_grater_than_zero
def Boolean(count=1, true_ratio=0.5):
    return [random() < true_ratio for _ in range(count)]


@count_must_grater_than_zero
def Char(count=1, selection=ALPHABET):
    return [choice(selection) for _ in range(count)]


@count_must_grater_than_zero
def Float(count=1, min=0, max=1):
    return [min + random() * (max - min) for _ in range(count)]


@count_must_grater_than_zero
def Integer(count=1, min=0, max=10):
    return [int(min + random() * (max - min)) for _ in range(count)]


def __generate_string(charset, length):
    return ''.join([choice(charset) for _ in range(length)])


def __int_between_1_and(max_len):
    assert max_len > 1, 'max_len must greater than or equal to 1'
    return int(1 + (random() * max_len - 1))


def String(count=1, selection=None, charset=ALPHABET, fixed_len=None, max_len=None):
    if selection is not None:
        return [choice(selection) for _ in range(count)]

    if fixed_len is not None:
        if isinstance(fixed_len, int):
            return [__generate_string(charset, fixed_len) for _ in range(count)]
        elif isinstance(fixed_len, list):
            assert len(fixed_len) == count, 'if fixed_len is list, len(fixed_len) must equal to count'
            return [__generate_string(charset, _fixed_len) for _fixed_len in fixed_len]
        else:
            raise Exception('fixed_len support int or list only')

    if max_len is not None:
        if isinstance(max_len, int):
            return [__generate_string(charset, __int_between_1_and(max_len)) for _ in range(count)]
        elif isinstance(max_len, list):
            assert len(max_len) == count, 'if max_len is list, len(max_len) must equal to count'
            return [__generate_string(charset, __int_between_1_and(_max_len)) for _max_len in max_len]
        else:
            raise Exception('max_len support int or list only')
