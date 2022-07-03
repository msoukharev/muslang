from muslang.tokens import Token
from muslang.ast import MergeExpression, NoteProgression, ProgressionExpression, Note
from muslang.module import Module


def parse_sequence(tokens: list[Token], context: Module) -> list[NoteProgression]:
    progs: list[NoteProgression] = []
    for token in tokens:
        match token:
            case Token(type='note'):
                progs.append(NoteProgression([{Note(token.word)}]))
            case Token(type='identifier'):
                progs.append(context.variables[token.word])
            case _:
                raise ValueError('Unrecognized expression')
    return progs

def parse_expression(tokens: list[Token], context: Module) -> NoteProgression:
    match tokens:
        case [Token(word='merge'), *rest]:
            return MergeExpression(parse_sequence(rest, context)).eval()  # type: ignore
        case [Token(word='progression'), *rest]:
            return ProgressionExpression(parse_sequence(rest, context)).eval()  # type: ignore
        case [Token(type='identifier') as binding]:
            return context.variables[binding.word]
        case _:
            raise ValueError(f'Cannot identify expression pattern: {tokens}')


def parse_statements(statements: list[list[Token]]) -> Module:
    module: Module = Module()
    print(statements)
    for statement in statements:
        match statement:
            case [Token(word='module'), Token(type='identifier') as id, Token(word='end')]:
                module.name = id.word
            case [
                Token(word='let'),
                Token(type='identifier') as const,
                Token(word='='), *rest,
                Token(word='end')
                ]:
                module.variables[const.word] = parse_expression(rest, module)
            case [
                Token(word='compose'),
                *rest,
                Token(word='end')
            ]:
                module.output = parse_expression(rest, module)
            case _:
                raise ValueError(f'Statement pattern unrecognized: {statement}')
    if not module.name or not module.output:
        raise ValueError('No module is declared')
    return module
