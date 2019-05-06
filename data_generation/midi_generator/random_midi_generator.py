from midiutil import MIDIFile
# from mido import MidiFile, open_output
from random import randint, random

major_scale_notes  = [60, 62, 64, 65, 67, 69, 71, 72]  # MIDI note number
degrees = [randint(60,80) for x in range(100)]

track    = 0
channel  = 0
time     = 0    # In beats
duration = 1    # In beats
tempo    = 200   # In BPM
volume   = 100  # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
                      # automatically)
MyMIDI.addTempo(track, time, tempo)

random_midi_file = "../generated_midi/random.mid"

shift = 0
for pitch in degrees:
    duration = 1 + 2*random()
    volume = randint(70,100)
    MyMIDI.addNote(track, channel, pitch, time + shift, duration, volume)
    shift += duration

with open(random_midi_file, "wb") as output_file:
    MyMIDI.writeFile(output_file)

# midi_file = MidiFile(random_midi_file)
# outport = open_output()
# for msg in midi_file.play():
#     outport.send(msg)
