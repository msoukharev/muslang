from muslang.ast import NoteProgression
from mingus.containers.composition import Composition
from mingus.containers.instrument import Piano
from mingus.containers.note import Note as MNote
from mingus.containers.note_container import NoteContainer
from mingus.containers.track import Track


def compose(progression: NoteProgression) -> Composition:
    comp = Composition()
    track = Track(Piano())
    for noteset in progression.notes:
        track.add_notes(NoteContainer([MNote(note.note, note.octave) for note in noteset]))
    comp.add_track(track)
    return comp
