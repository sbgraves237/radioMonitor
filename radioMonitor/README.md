# radioMonitor1.py 
Monitor radio broadcast quality

A [Python package](https://packaging.python.org/tutorials/packaging-projects/) containing a function to create a series of *.wav files of a specified length (10 minutes in production) with name indicating the audio source (90_1FM for KKFI) and the time stamp started and ending on even multiples of the specified length.  Production and testing will be documented further in an R Markdown Document "radioMonitor1.Rmd".  

Plan for different versions:  

* 0.1.  Record only one *.wav file, then stop.  

* 0.2.  From the start time, compute the end time as the next integer multiple of RECORD_SECONDS, construct a file name containing the start time, then record to the end time, then stop.  

* 0.3.  Put the recording in an infinite loop to write a series of *.wav files with names constructed as with version 0.2.  

* 0.4.  Modify the infinite loop of 0.3 to create a file folder for each day and store the *.wav files for that day in that folder.  

* 1.0.  Release the version from 0.4 after testing.  

* 2.0.  Modify version 1.0 to record two sources: source and broadcasted.    

* 2.1.  Modify version 2.0 to determine the time synchronization, then compute the difference and write three files:  source, broadcasted and difference.    

* 2.2.  Modify version 2.1 to identify problems in the difference.  
 