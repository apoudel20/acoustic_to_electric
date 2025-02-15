from midiutil import MIDIFile
# from mido import MidiFile, open_output
from random import choices,randint, random

major_scale_notes  = [60, 62, 64, 65, 67, 69, 71, 72]  # MIDI note number
degrees = choices(major_scale_notes, k=100)

track    = 0
channel  = 0
time     = 0    # In beats
duration = 1    # In beats
tempo    = 200   # In BPM
volume   = 100  # 0-127, as per the MIDI standard


for file_num in range(30):
    track_midi_file = "../generated_midi/test/track"

    MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
                      # automatically)
    MyMIDI.addTempo(track, time, tempo)
    shift = 0
    for pitch in degrees:
        duration = 1 + .125*randint(0,8)
        volume = randint(70,127)
        MyMIDI.addNote(track, channel, pitch, time + shift, duration, volume)
        shift += duration

    with open(track_midi_file + "_" + str(file_num).zfill(2) + ".mid", "wb") as output_file:
        MyMIDI.writeFile(output_file)

# midi_file = MidiFile(random_midi_file)
# outport = open_output()
# for msg in midi_file.play():
#     outport.send(msg)
