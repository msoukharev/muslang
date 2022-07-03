from typing import Literal
import muslang.ast
import muslang.parser
import muslang.tokens
from muslang.parser import parse_statements
from muslang.scanner import scan
from muslang.composition import compose
from mingus.midi import midi_file_out


def compile(file, target: str):
    with open(file, 'rt') as f:
        module = parse_statements(
            scan(
                f.read()
            )
        )
        comp = compose(module.output)
        midi_file_out.write_Composition(target, comp)
