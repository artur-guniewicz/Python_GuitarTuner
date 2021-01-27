import sounddevice as sd
import numpy as np
import scipy.fftpack
# import os

SAMPLE_FREQ = 44100
WINDOW_SIZE = 44100
WINDOW_STEP = 21050
WINDOW_T_LEN = WINDOW_SIZE / SAMPLE_FREQ
SAMPLE_T_LENGTH = 1 / SAMPLE_FREQ
windowSamples = [0 for _ in range(WINDOW_SIZE)]

CONCERT_PITCH = 440
ALL_NOTES = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]


#def cls():
#    os.system('cls' if os.name == 'nt' else 'clear')


def find_closest_note(pitch):
    i = int(np.round(np.log2(pitch / CONCERT_PITCH) * 12))
    closestNote = ALL_NOTES[i % 12] + str(4 + np.sign(i) * int((9 + abs(i)) / 12))
    closestPitch = CONCERT_PITCH * 2 ** (i / 12)
    return closestNote, closestPitch


def callback(indata, status, x, y):
    global windowSamples
#    if status:
#        print(status)
    if any(indata):
        windowSamples = np.concatenate((windowSamples, indata[:, 0]))
        windowSamples = windowSamples[len(indata[:, 0]):]
        magnitudeSpec = abs(scipy.fftpack.fft(windowSamples)[:len(windowSamples) // 2])

        for i in range(int(62 / (SAMPLE_FREQ / WINDOW_SIZE))):
            magnitudeSpec[i] = 0

        maxInd = np.argmax(magnitudeSpec)
        maxFreq = maxInd * (SAMPLE_FREQ / WINDOW_SIZE)
        closestNote, closestPitch = find_closest_note(maxFreq)

#        cls()
        print(f"Closest note: {closestNote} {maxFreq:.1f}/{closestPitch:.1f}")
    else:
        print('no input')


try:
    with sd.InputStream(channels=1, callback=callback,
                        blocksize=WINDOW_STEP,
                        samplerate=SAMPLE_FREQ):
        while True:
            pass
except Exception as e:
    print(str(e))
