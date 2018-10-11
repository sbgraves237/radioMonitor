# radioMonitor
Monitor radio broadcast quality

2018-10-11:  Initiate project with a vision of code to monitor in real time stream from a radio tuner and compile reports to support identification and diagnosis of problems with broadcast quality.  

PLAN:  

1.  Compare R Markdown Notebooks with R Markdown Documents and Jupyter Notebooks to decide which to use.  I want to be able to mix R and Python code in the same document.  I can do this with R Markdown Documents and Notebooks.  I don't know if I can do this in Jupyter.  After I get examples, share them with "r-help@r-project.org" and "python-list@python.org" and perhaps "Yihui Xie <xie@yihui.name>" to get help (a) understanding the similarities and differences and (b) deciding which to use.  

2.  Produce a single document trying to do this in both R and Python.  I prefer to do it in R, because I know it better.  However, I so far have not found a way to do it in R, and I have found code that will allow me to read an input stream from a radio tuner and write a wav file of whatever length I choose;  start with 5 seconds for simplicity.  Share this with "r-help@r-project.org" and "python-list@python.org" and perhaps others to ask for help with things I do not yet know how to do.  

3.  Wrap the code in a loop to write a series of wav files with the name of the station and start time, e.g., "KKFI2018-10-12T13:10" to log 10 minutes of signal received from 90.1 FM, KKFI.org, starting at 2018-10-12 at 1:10 PM local time in KKFI's studios.  Report to KKFI's EFT Committee when this is working, and invite discussion on what to do next with this.  

4.  Modify the code to monitor for times when the absolute signal strength is at most s0 for more than t0 seconds.  When that happens, append an incident report to a file (e.g., "thresholdEvents.csv") while optionally sending an email or a text message or calling a certain phone number with a certain recorded message.  The details of s0, t0, incidentSummaryFile, emailAddr, textNumber, and voiceNumber would be in a file with a name like "radioMonitorConfig.csv".  This file could contain several different threshold pairs (s0, t0) with different actions prescribed for each one.  Report to KKFI's EFT Committee when this is working, and invite further discussion of what to do next.   

5.  Create new code that would read a live stream from the internet or some other source and try to predict T[t] = tuner signal recorded at time t from S[t+d] = live stream at recorded time (t+d), with d being some relatively low-dimensional vector of offsets.  More generally, if S[t+d] is the input to any piece of equipment and T[t] the (stereo = bivariate) output from that piece of equipment, the output should be at most one or two observations behind the input.  If the output is digital, then it should match exactly the input with possibly a lag of one observation (d = 0 or 1).  If the output is analog, the problem could be more difficult with problems of frequency response distorting the signal and redigitization suggesting that the output could best be predicted by a linear interpolation of two observations at an appropriate lag.  However, if S[t+d] is the direct input to the equipment, then d should still be something like (0, 1) with the output being a linear interpolation of the current and previous observation.  If S[t+d] is recorded in the studio and T[t] after the signal returns from the tower, then d should be at most 5 or 10 for signals to move from KKFI's studio to its tower and back, though we could lose a bit more time than that due to digital processing time in several pieces of digital equipment.  I get "2" here, because KKFI's tower is 6 miles (10 km) from its studio = 12 miles (20 km) round trip, and the speed of light is 186,000 miles per second (300,000 km/sec.).  At the standard audio sampling frequency of 44.1 kHz, light travels 4.2 miles (6.8 km) per observation.  Therefore, it takes roughly 3 observations for light to travel to KKFI's tower and back.  We should probably also expect to lose more time averaging, say, 0.5/44100 for each piece of equipment the signal passes through.  With this, we might consider training Kalman filters with d = (3, 4), (4, 5), ..., (10, 11) and use Bayesian Model Averaging over the one or two with the best fit.  If S[t+d] is taken from live stream via the internet, this problem can be much harder.  In one example, matching by ear, the live stream was roughly 32 second (d = -32 x 4400) behind the signal from the tuner.  That may or may not be computationally feasible.  However, if we can match the time, then we can compute the residuals from a bivariate regression and identify events where the absolute residuals are at most s0 for time periods at least t0, as described for the single signal monitor for problems with absolute signal strength.  
