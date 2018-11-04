# radioMonitor
Monitor radio broadcast quality

2018-10-11:  Initiate project with a vision of code to monitor in real time a stream from a radio tuner and compile reports to support identification and diagnosis of problems with broadcast quality.  

PLAN:  

1.  Compare R Markdown Notebooks with R Markdown Documents and Jupyter Notebooks to decide which to use. I decided to use R Markdown Documents, at least until someone convinces me I should do diffently.  A toy example I created in an R Markdown Notebook included a line of code that worked, then gave errors for several hours, then started working again for no reason I could see.  Meanwhile, Project Jupyter suggested I launch a Jupyter Notebook from an Anaconda Navigator.  When I tried that under Windows 7, Ananconda Navigator went into an apparent infinite loop.  When I tried it under macOS, I got a directory of 28 items with a note asking me to "Select items to perform actions on them." Other documentation I've seen suggests that R Markdown Documents can do everything, or nearly everything, that people love about Jupyter Notebooks.  I've decided to use R Markdown Documents at least until I encounter another reason to revisit this decision.  Done: 2018-10-11.  

2.  Radio Monitor-initial testing
= R Markdown Document in "radioMonitor-init2018-10-11.Rmd" that documents What I want in software to monitor a radio broadcast signal and the production of a prototype of it.  I could not find a way to do it in R, but in Python I got code that produces a 5-second *.wav file with sound that seemed consistent with what 90.1 FM, KKFI, was presumably broadcasting during those 5 seconds.  Done:  2018-10-12.

3.  radioMonitor1.py 
= a [Python package](https://packaging.python.org/tutorials/packaging-projects/) containing a function to create a series of *.wav files of a specified length (10 minutes in production) with name indicating the audio source (90_1FM for KKFI) and the time stamp started and ending on even multiples of the specified length.  Production and testing will be documented further in an R Markdown Document "radioMonitor1.Rmd".  

NOTE:  This will likely be implemented in a series of upgrades as outlined in "radioMonitor/README.md" in the "radioMonitor" subfolder of this project folder.  The initial step would be radioMonitor0_1.Rmd that calls  a function radioMonitor0_1.py that creates a single *.wav file.  This would be followed by 0_2, 0_3, 0_4, leading to 1_0, which would create daily folders of individual files, then by 2_0, 2_1, and 2_2 that would create similar folders with files of input, output, and difference plus summary folders of questionable incidents with Fast Fourier Transforms of the signal before, during and after an apparent drop out.  

* 0_1.  Record only one *.wav file with a hard coded name, then stop.  Done 2018-10-28.  

* 0_2.  Record only one *.wav file with a name computed from the current date and time, then stop. Done 2018-11-02. 

* 0_3.  Same as "0_2", but use "while datetime.now() <= endTime:" rather than "for i in range(...):".  Done 2018-11-03.  

* 0_4.  Record only one *.wav file with a name computed from the current date and time, stopping at the nearest integer multiple of RECORD_SECONDS. The resulting *.wav file will therefore have duration at most RECORD_SECONDS.  (Drop the "-5sec" characters from the file name.) Done:  2018-11-03.

* 0_5.  test_mkdir.py: Test for the existence of a directory and create if it does not exist.  Done:  2018-11-04.  

* 0_6.  Put the log files in a folder with a name constructed from "source" followed by the date;  create the folder if it does not already exist.  Done:  2018-11-04.  

* 0_7.  Put the recording in an infinite loop to write a series of *.wav files with names constructed as with version 0_6.  Done: 2018-11-04.

* 0_8.  Replace RECORD_SECONDS with RECORD_MINUTES in 0_7, make the other obvious corresponding adjustments, and put the recording in an infinite loop to write a series of *.wav files with names constructed as with version 0_7.  

* 0_9.  Make the default RECORD_MINUTES=60.  

* 0_10.  Change copyright to a standard software license that's free for noncommercial uses with a def


* 1_0.  Release the version from 0_10 after testing.  

* 2_0.  Modify version 1_0 to record two sources: source and broadcasted.    

* 2_1.  Modify version 2.0 to determine the time synchronization, then compute the difference and write three files:  source, broadcasted and difference.    

* 2_2.  Modify version 2.1 to identify problems in the difference.  
 
4.  Start regular use of radioMonitor1.py, reprting to KKFI's EFT Committee, inviting their suggestions on how to use this and how to enhance it:  First, if we can identify specific times of specific skips, we can then find the corresponding files, read them into Audacity, see what the wave form looks like at the specific time. We can document that in greater detail, report it to the EFT Committee and Una Nowling.  Mike Murphy can share the result with KKFI's radio engineers, Ed Treese and Mike Rogers and get their input regarding the kind of spectrum they would like to see from such events.  I may also share it with a local Python Meetup plus "python-list@python.org" for help with things I don't yet know how to do plus "r-help@r-project.org" to search for a way to do this in R that I may have overlooked.  If any work in this area is done in R or Python, document that in an R Markdown Document with a name like "radioMonitor1a*.Rmd".

5.  radioMonitor1m.py 
= a new function in Python package radioMonitor1.py that would monitor for dead air while continuing to produce the *.wav log files discussed in "3" above.  In particular, it would look for times when the absolute signal strength is at most s0 for more than t0 seconds.  When that happens, a summary of that would be appended to an incident report file (e.g., "thresholdEvents.csv") while optionally sending an email or a text message or calling a certain phone number with a certain recorded message.  The details of s0, t0, incidentSummaryFile, emailAddr, textNumber, and voiceNumber would be in a file with a name like "radioMonitorConfig.csv".  This file could contain several different threshold pairs (s0, t0) with different actions prescribed for each one. Report to KKFI's EFT Committee when this is working, and invite further discussion of what to do next.  Document prouction and testing of this in an R Markdown Document with a name like "radioMonitor1m*.Rmd". 

6.  radioMonitor2.py
= a new function in Python packagage radioMonitor1.py that would read a live stream from the internet or some other source and try to predict T[t] = tuner signal recorded at time t from S[t+d] = live stream at recorded time (t+d), with d being some relatively low-dimensional vector of offsets.  More generally, if S[t+d] is the input to any piece of equipment and T[t] the (stereo = bivariate) output from that piece of equipment, the output should be at most one or two observations behind the input.  If the output is digital, then it should match exactly the input with possibly a lag of one observation (d = 0 or 1).  If the output is analog, the problem could be more difficult with problems of frequency response distorting the signal and redigitization suggesting that the output could best be predicted by a linear interpolation of two observations at an appropriate lag.  However, if S[t+d] is the direct input to the equipment, then d should still be something like (0, 1) with the output being a linear interpolation of the current and previous observation.  If S[t+d] is recorded in the studio and T[t] after the signal returns from the tower, then d should be at most 5 or 10 for signals to move from KKFI's studio to its tower and back, though we could lose a bit more time than that due to digital processing time in several pieces of digital equipment.  I get "2" here, because KKFI's tower is 6 miles (10 km) from its studio = 12 miles (20 km) round trip, and the speed of light is 186,000 miles per second (300,000 km/sec.).  At the standard audio sampling frequency of 44.1 kHz, light travels 4.2 miles (6.8 km) per observation.  Therefore, it takes roughly 3 observations for light to travel to KKFI's tower and back.  We should probably also expect to lose more time averaging, say, 0.5/44100 for each piece of equipment the signal passes through.  With this, we might consider training Kalman filters with d = (3, 4), (4, 5), ..., (10, 11) and use Bayesian Model Averaging over the one or two with the best fit.  If S[t+d] is taken from live stream via the internet, this problem can be much harder.  In one example, matching by ear, the live stream was roughly 32 second (d = -32 x 4400) behind the signal from the tuner.  That may or may not be computationally feasible.  However, if we can match the time, then we can compute the residuals from a bivariate regression and identify events where the absolute residuals are at most s0 for time periods at least t0, as described for the single signal monitor for problems with absolute signal strength.  Document prouction and testing of this in an R Markdown Document with a name like "radioMonitor2*.Rmd". 
