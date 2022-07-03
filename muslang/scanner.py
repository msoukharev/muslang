from muslang.language import *
from muslang.tokens import Token


def scan(content: str) -> list[list[Token]]:
    tokens: list[Token] = []
    lines: list[str] = content.split('\n')
    print(lines)
    for line in lines:
        if len(line) == 0:
            continue
        words = line.split(' ')
        for word in words:
            tok = Token(word)
            tokens.append(tok)
    groups: list[list[Token]] = []
    group: list[Token] = []
    for token in tokens:
        group.append(token)
        if token.word == 'end':
            groups.append(group)
            group = []
    if group:
        if (group[-1].word == 'end'):
            groups.append(group)
        else:
            raise ValueError(f'Unclosed expression')
    return groups
