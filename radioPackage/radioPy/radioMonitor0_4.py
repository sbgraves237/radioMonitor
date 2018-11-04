def radioMonitor0_4(
  source="90_1FM", 
  RECORD_SECONDS=5, 
  
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

  import pyaudio
  import wave

  CHUNK = 1024
  FORMAT = pyaudio.paInt16
  CHANNELS = 2
  RATE = 44100
# RECORD_SECONDS = 5
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
  DtTmi = DtTm.strftime("%Y-%m-%dT%H_%M_%S")
  
  WAVE_OUTPUT_FILENAME = source+DtTmi+".wav"
#   
  tm = DtTm.time()
  secs = tm.second
  micros = tm.microsecond
  ds = secs+RECORD_SECONDS
  dsrem = ds%RECORD_SECONDS
#  td = datetime.timedelta(0, 0, RECORD_SECONDS)
  from datetime import timedelta
  td = timedelta(0, RECORD_SECONDS-dsrem, -micros)
  endTime = DtTm+td
  
  p = pyaudio.PyAudio()

  stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
                

  print("* recording")

  frames = []

#  for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
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


