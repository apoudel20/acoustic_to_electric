# AcousticToElectric
This project is aimed at converting acoustic guitar sounds into electric with the use of neural networks. 
<hr>

## Progress

Currently, all that has been completed is the automated data generation for acoustic and electric sounds that have been synthesized with the use of the fluidsynth (v1.1.6) for Windows. The `data_generation` directory contains a batch file (`.bat`) that, when executed, produces the following files:
- `generated_midi/random.mid`
- `synthesized_wav/random_acoustic.wav`
- `synthesized_wav/random_electric.wav`
This build process currently only works for windows. However, with the right fluidsynth builds and a few path adjustments, it can run on linux systems as well.

## Requirements 
For the MIDI file generation, `MIDIUtil` was used. It can be installed with the following command
> `pip install MIDIUtil`

The `fluidsynth` binary for x64 is already included in the `data_generation/fluidsynth_binaries` directory because I don't like it when I have to build everything when I download from github. I didn't use the builds for x86 because lol I didn't want to.

## Working On
Now that the data generation is complete, I will attempt to understand and segment the spectrogram data. I'm thinking of creating the data by segmenting it into ~0.05 second chunks (2047 samples) because I read somewhere that the human persistence of sound is like 0.1 seconds and I want my system to be realtime so that a significant delay is not observed in processing. I will also try to apply autoencoders to convert the vertical lines on the spectrogram of an acoustic sound into the same of an electric sound. I'll get back to this once I figure out which approach works best.