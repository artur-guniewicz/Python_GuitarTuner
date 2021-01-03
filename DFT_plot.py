import scipy.io.wavfile
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft

sampleFreq, myRecording = scipy.io.wavfile.read("sound1.wav")
sampleDur = len(myRecording) / sampleFreq
timeX = np.arange(0, sampleFreq / 2, sampleFreq / len(myRecording))

absFreqSpectrum = abs(fft(myRecording))
print(absFreqSpectrum)

plt.plot(timeX, absFreqSpectrum[:len(myRecording) // 2])
plt.ylabel('|X(n)|')
plt.xlabel('frequency[Hz]')
plt.show()
