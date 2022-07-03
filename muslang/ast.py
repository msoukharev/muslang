from muslang.language import KEYWORDS


class BaseExpression():

    def eval(self) -> 'NoteProgression':
        raise NotImplementedError


class Context():

    variables: dict

    def __init__(self, variables: dict) -> None:
        self.variables = {}
        self.variables.update(variables)

    def get_variable(self, key: str) -> BaseExpression:
        try:
            return self.variables[key]
        except KeyError:
            raise ValueError(f'Symbol {key} is unbound')

    def set_variable(self, key: str, val: BaseExpression):
        if key in KEYWORDS:
            raise ValueError('Symbol {key} is a reserved keyword')
        self.variables[key] = val


class NoteProgression(BaseExpression):

    notes: list[set['Note']]

    def __init__(self, notes: list[set['Note']]) -> None:
        super().__init__()
        self.notes = notes

    def eval(self) -> 'NoteProgression':
        return self

    def __str__(self) -> str:
        return [str(note) for note in self.notes].__str__()

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, NoteProgression) and len(self.notes) == len(__o.notes):
            for n1, n2 in zip(self.notes, __o.notes):
                if n1 != n2:
                    return False
            return True
        return False

class Note(BaseExpression):

    note: str
    octave: int

    def __init__(self, note: str):
        note_sym, octave = note.split('-')
        self.note = note_sym
        self.octave = int(octave)

    def __str__(self) -> str:
        return self.note + '-' + str(self.octave)

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Note) and str(self) == str(__o)

    def __hash__(self) -> int:
        return hash(str(self))


class ProgressionExpression():

    expressions: list[BaseExpression]

    def __init__(self, expressions: list[BaseExpression]) -> None:
        self.expressions = expressions

    def eval(self) -> NoteProgression:
        prog = []
        for ex in self.expressions:
            notes = ex.eval().notes
            for noteset in notes:
                prog.append(noteset)
        return NoteProgression(prog)


class MergeExpression():

    expressions: list[BaseExpression]

    def __init__(self, expressions: list[BaseExpression]) -> None:
        self.expressions = expressions

    def eval(self) -> NoteProgression:
        exprs = [exp.eval() for exp in self.expressions]
        max_len = max([len(exp.notes) for exp in exprs])
        prog = []
        for i in range(max_len):
            noteset = set()
            for exp in exprs:
                if len(exp.notes) > i:
                    noteset.update(exp.notes[i])
            prog.append(noteset)
        return NoteProgression(prog)
