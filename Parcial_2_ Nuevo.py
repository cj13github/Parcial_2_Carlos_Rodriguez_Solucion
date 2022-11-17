import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.io.wavfile import write

fig2=plt.figure(figsize=(8,8))
ax1=fig2.add_subplot(2,1,1)
ax2=fig2.add_subplot(2,1,2)

señaldeaudi=("C:/Users/Carlos Rodriguez/Desktop/song_mono.wav")
fss, signal=wavfile.read(señaldeaudi)
st.audio(señaldeaudi, format='audio/wav')
st.latex(fss)

audio= signal
L=len(audio)
n1=np.arange(0,L)/fss

f1=np.fft.fft(audio)
freq1=np.fft.fftfreq(len(audio))*fss
fp=len(freq1)
n2=np.arange(-(fp/2),fp/2)

ax1.plot(n1,audio)
ax2.plot(freq1,abs(f1))
#ax1.plot(n1,final)
ax2.axis([0, 2000, 0, 450000000 ])
st.pyplot(fig2)

fig1=plt.figure(figsize=(8,8))
ax1=fig1.add_subplot(1,1,1)

u2 = np.where(freq1>=1,1,0)
u4 = np.where(freq1>=1000,1,0)
u= u2-u4

ax1.plot(freq1,u)
ax1.axis([-2000, 2000, 0, 1.5 ])
st.pyplot(fig1)

suma = f1*u
nuevo_audio=np.fft.ifft(suma)

fig3=plt.figure(figsize=(8,8))
ax1=fig3.add_subplot(2,1,1)
ax2=fig3.add_subplot(2,1,2)
ax1.plot(n1,nuevo_audio)
ax2.plot(freq1,suma)
ax2.axis([0, 2000, 0, 45000000])
st.pyplot(fig3)

write('song_mono_nuevo.wav', fss, nuevo_audio.astype(np.int16))
audio_file = open('song_mono_nuevo.wav', 'rb')
audio_by = audio_file.read()
st.audio(audio_by, format='audio/wav')
