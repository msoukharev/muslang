from muslang.ast import NoteProgression


class Module():

    name: str
    bpm: int
    variables: dict[str, NoteProgression]
    output: NoteProgression

    def __init__(self) -> None:
        self.variables = dict()
        self.bpm = 120
