"""
Some piece of codes are from Internet. 
"""
from websocket import create_connection
import numpy as np
import wave
from pyaudio import PyAudio, paInt16, paFloat32
import time
import struct

framerate = 48000  # 采样率
num_samples = 1024  # 采样点
channels = 1  # 声道
sampwidth = 2  # 采样宽度2bytes
FILEPATH = './recorded_samples/my_recordings.wav'         #文件保存路径
dur = 10            # 设置录音时间（秒）
MODE = 'websocket'

def save_wave_file(filepath, data):
    wf = wave.open(filepath, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(sampwidth)
    wf.setframerate(framerate)
    wf.writeframes(b''.join(data))
    wf.close()
 

#录音
def main():
    pa = PyAudio()
    # 打开一个新的音频stream
    stream = pa.open(format=paInt16, channels=channels,
                     rate=framerate, input=True, frames_per_buffer=num_samples)
    my_buf = [] #存放录音数据
 
    t = time.time()
    print('正在录音...')
    if MODE == 'websocket':
        # ---- websocket ----- #
        ws = create_connection("ws://localhost:9001/")
        ws.send('Start recording')
    package_head = struct.pack('<bi', sampwidth, num_samples)
    while time.time() < t + dur:  # 设置录音时间（秒）
    	#循环read，每次read 2000frames
        string_audio_data = stream.read(num_samples)
        package = string_audio_data
        if MODE == 'websocket':
            ws.send(package)
        else:
            my_buf.append(string_audio_data)
    print('录音结束.')
    if MODE == 'websocket':
        ws.close()
    else:
        save_wave_file(FILEPATH, my_buf)
    stream.close()
 
if __name__ == '__main__':
    main()