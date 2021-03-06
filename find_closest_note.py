import numpy as np

CONCERN_PITCH = 440
ALL_NOTES = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]


def find_closest_note(pitch):
    i = int(np.round(np.log2(pitch / CONCERN_PITCH) * 12))
    closest_note = ALL_NOTES[i % 12] + str(4 + np.sign(i) * int((9 + abs(i)) / 12))
    closest_pitch = CONCERN_PITCH * 2 ** (i / 12)
    
    return closest_note, closest_pitch


