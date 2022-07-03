import mingus.core.notes as notes
from mingus.containers.track import Track
from mingus.containers.instrument import Instrument, Piano
from mingus.containers.composition import Composition
from mingus.containers.note import Note
from mingus.containers.bar import Bar
from mingus.containers.note_container import NoteContainer

from mingus.midi import midi_file_out


chord_progressions = [
    ['C-4', 'E-4', 'G-4'], # C major
    ['G-4', 'B-4', 'D-4'], # G major
    ['A-4', 'C-4', 'E-4'], # A minor
    ['F-4', 'A-4', 'C-4']
]

def evaluate(track):
    instrument = Piano()
    t = Track(instrument)
    for chord in chord_progressions:
        b = Bar('C', (2, 4))
        t.add_bar(b)
    c = Composition()
    c.add_track(t)
    midi_file_out.write_Composition('./midifile.midi', c, repeat=3, bpm=120)

evaluate(None)
