# radioMonitor.py 2018-10-24

from pydub import AudioSegment
from pydub.utils import make_chunks


raw_file = "swamp.wav"
seconds = 60

extentions = ["wav", "mp3", "ogg"]
try:
    for _ext in extentions:
        if raw_file.endswith("." + _ext):
            ext = _ext
            audio_file = AudioSegment.from_file(raw_file, ext)
            print('\n', raw_file + " Loaded!")
except:
    print('\n', "Please check your File format")


chunk_length = 1000 * seconds
chunks = make_chunks(audio_file, chunk_length)
print('\n', "----Exporting File----")
for i, chunk in enumerate(chunks):
    chunk_name = "chunk{0}.wav".format(i)
    print("exporting", chunk_name)
    chunk.export(chunk_name, format=ext)
