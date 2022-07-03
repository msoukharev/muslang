import pytest
from muslang.ast import MergeExpression, NoteProgression, Note, ProgressionExpression


b_2 = Note('B-2')
noteset_1 = [{Note('C-4'), Note('C-5'), Note('C-6')}]
noteset_2 = [{Note('C-4'), Note('A-5'), Note('B-3')}, {Note('G-3'), Note('F-2')}]
ch1 = NoteProgression(noteset_1)
ch2 = NoteProgression(noteset_2)


def test_progression_expr():
    exp = NoteProgression([*noteset_1, *noteset_2])
    act = ProgressionExpression([ch1, ch2]).eval()
    assert exp == act


def test_merge_expr():
    exp = MergeExpression([ch1, ch2]).eval()
    act = NoteProgression([{*noteset_1[0], *noteset_2[0]}, noteset_2[1]])
    assert exp == act
