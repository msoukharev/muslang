from typing import Literal
import re
from muslang.language import OPERATORS


TYPE = Literal[
    'identifier',
    'keyword',
    'operator',
    'note'
]


NOTES = {
    'A-[1-8]',
    'B-[1-8]',
    'C-[1-8]',
    'D-[1-8]',
    'E-[1-8]',
    'F-[1-8]',
    'G-[1-8]'
}


KEYWORDS = {
    'progression',
    'merge',
    'module',
    'compose',
    'end'
}


NOTE_REGEXP = '|'.join([f'({n})' for n in NOTES])


IDENTIFIER_REGEXP = re.compile(r'\w+')


def is_note(word: str):
    return re.match(NOTE_REGEXP, word)


def is_operator(word: str):
    return word in OPERATORS


def is_keyword(word: str):
    return word in KEYWORDS


def is_valid_identifier(word: str):
    return word not in KEYWORDS and IDENTIFIER_REGEXP.match(word)


def resolve_type(word: str) -> TYPE:
    if is_keyword(word):
        return 'keyword'
    elif is_operator(word):
        return 'operator'
    elif is_note(word):
        return 'note'
    elif is_valid_identifier(word):
        return 'identifier'
    else:
        raise ValueError(f'Cannot parse word: word')


class Token():

    word: str
    type: TYPE

    def __init__(self, word: str) -> None:
        self.type = resolve_type(word)
        self.word = word

    def descriptor(self) -> tuple[TYPE, str]:
        return (self.type, self.word)

    def __str__(self) -> str:
        return str(self.descriptor())

    def __repr__(self) -> str:
        return str(self)
