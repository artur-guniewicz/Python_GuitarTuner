import scipy.io.wavfile
import matplotlib.pyplot as plt
import numpy as np

sampleFreq, myRecording = scipy.io.wavfile.read("sound1.wav")
sampleDur = len(myRecording) / sampleFreq
timeX = np.arange(0, sampleDur, 1 / sampleFreq)

plt.plot(timeX, myRecording)
plt.ylabel('x(k)')
plt.xlabel('time[s]')
plt.show()
