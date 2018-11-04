def radioMonitor(
  source="90_1FM", 
  RECORD_MINUTES=1, 
  
  ):
  """Function to record a live stream to a series of """
  """*.wav files in an infinite loop, """
  """subject to manual termination."""
  
  """generalizing:  """
  """PyAudio example: Record a few seconds of audio and save to a WAVE file."""
  """based in part on""" 
  """https://stackoverflow.com/questions/35344649/reading-input-sound-signal-using-python"""
  
  """The series should start at the time the software is called,"""
  """with each file carrying the start time in its name"""
  """and ending the observation on the next integer multiple"""
  """of RECORD_SECONDS.  """

  from radioPackage.radioPy import radioMonitor0_8
  
  while True: 
    radioMonitor0_8.radioMonitor0_8(
        source, RECORD_MINUTES, 
    )

def radioMonitor0_8(
  source="90_1FM", 
  RECORD_MINUTES=1, 
  
  ):
  """Function to record a live stream to a series of """
  """*.wav files in an infinite loop, """
  """subject to manual termination."""
  
  """generalizing:  """
  """PyAudio example: Record a few MINUTES of audio and save to a WAVE file."""
  """based in part on""" 
  """https://stackoverflow.com/questions/35344649/reading-input-sound-signal-using-python"""
  
  """The series should start at the time the software is called,"""
  """with each file carrying the start time in its name"""
  """and ending the observation on the next integer multiple"""
  """of RECORD_MINUTES.  """

  import pyaudio
  import wave

  CHUNK = 1024
  FORMAT = pyaudio.paInt16
  CHANNELS = 2
  RATE = 44100
# RECORD_MINUTES = 5
# In R I would write:  
#   SysTm <- Sys.time()
#   SysTme <- past0(substring(SysTm, 1, 10), 
#       'T', substring(SysTm, 12, 19))
#   SysTime <- gsub(':', '_', SysTme)
# WAVE_OUTPUT_FILENAME <- paste0(source, 
#   SysTime, ".wav")
#  WAVE_OUTPUT_FILENAME = "KKFI2018-10-12T13_08-5sec.wav"
#  import datetime 
#  DtTm = datetime.datetime.now()
  from datetime import datetime
  DtTm = datetime.now()
  YMD = DtTm.strftime("%Y-%m-%d")
  sourceYMD = source+YMD
  
  from radioPackage.radioPy import test_mkdir
  test_mkdir.test_mkdir(sourceYMD)

  DtTmi = DtTm.strftime("%Y-%m-%dT%H_%M")
  
  out_file = source+DtTmi+".wav"
  
  import os
  WAVE_OUTPUT_FILENAME = os.path.join(
    sourceYMD, out_file)
#   
  tm = DtTm.time()
  mins = tm.minute
  secs = tm.second
  micros = tm.microsecond
  dm = mins+RECORD_MINUTES
# minutes remaining to the next 
# integer multiple of RECORD_MINUTES
  dmrem = dm%RECORD_MINUTES
  dsrem = 60*dmrem + secs
# seconds remaining to the next
# integer multiple of RECORD_MINUTES
  ds = 60*RECORD_MINUTES - dsrem
#  td = datetime.timedelta(0, 0, RECORD_MINUTES)
  from datetime import timedelta
# record for ds more seconds less micros  
  td = timedelta(0, ds, -micros)
  endTime = DtTm+td
  
  p = pyaudio.PyAudio()

  stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
                

  print("* recording")

  frames = []

#  for i in range(0, int(RATE / CHUNK * RECORD_MINUTES)):
  while datetime.now() <= endTime:
  
    data = stream.read(CHUNK)
    frames.append(data)

  print("* done recording")

  stream.stop_stream()
  stream.close()
  p.terminate()

  wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
  wf.setnchannels(CHANNELS)
  wf.setsampwidth(p.get_sample_size(FORMAT))
  wf.setframerate(RATE)
  wf.writeframes(b''.join(frames))
  wf.close()


