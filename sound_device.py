import sounddevice as sd
from scipy.io.wavfile import write
fs=44100
seconds=8
my_recording=sd.rec(int(seconds*fs),samplerate=fs,channel=2)
sd.wait()
write('output.wav',fs,my_recording)