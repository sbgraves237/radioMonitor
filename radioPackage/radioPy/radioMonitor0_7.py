def radioMonitor(
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

  from radioPackage.radioPy import radioMonitor0_6
  
  while True: 
    radioMonitor0_6.radioMonitor0_6(
        source, RECORD_SECONDS=5, 

    )


