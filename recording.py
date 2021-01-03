import sounddevice as sd
import scipy.io.wavfile
import time

SAMPLE_FREQ = 44100
SAMPLE_DUR = 2

print("Recording will start in 10 seconds!")
for i in range(10):
    print(10 - i, '...')
    time.sleep(1)

myRecording = sd.rec(SAMPLE_DUR * SAMPLE_FREQ, samplerate=SAMPLE_FREQ, channels=1, dtype='float64')
print("\nRecording in progress...")
sd.wait()

sd.play(myRecording, SAMPLE_FREQ)
print("\nPlaying recorded sound")
sd.wait()

scipy.io.wavfile.write('sound1.wav', SAMPLE_FREQ, myRecording)
