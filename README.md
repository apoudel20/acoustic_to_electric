# AcousticToElectric
This project is aimed at converting timbre of a given musical piece with the use of VAEs combined with GANs. 
<hr>

## Progress

Currently, this repository contains the automated data generation for acoustic and electric sounds that have been synthesized with the use of the fluidsynth (v1.1.6) for Windows. The `data_generation/midi_generator` directory contains a batch file (`.bat`) that, when executed, produces the following files:
- `generated_midi/random.mid`
- `synthesized_wav/random_acoustic.wav`
- `synthesized_wav/random_electric.wav`
This build process currently only works for windows. However, with the right fluidsynth builds and a few path adjustments, it can run on linux systems as well.

## Requirements 
For the MIDI file generation, `MIDIUtil` was used. It can be installed with the following command
> `pip install MIDIUtil`

The `fluidsynth` binary for x64 is already included in the `data_generation/fluidsynth_binaries` directory because I don't like it when I have to build everything when I download from github. I didn't use the builds for x86 because lol I didn't want to.

You will also need to download some soundfonts for this to run. 
- For acoustic guitar sounds, [Download the Acoustic soundfont](https://drive.google.com/file/d/0B4_6p-MMrzwLVUJTRnVUaEtfVjA/view)
- For electric guitar sounds, [Download the Electric soundfont](https://drive.google.com/file/d/0B4_6p-MMrzwLNXFEbUU2b3BBMjQ/view)

The provided batch script `data_generation/midi_generation.midi_to_electric_acoustic.bat` runs the data generation process and populates the `synthesized_wav`  directory

## Model

Currently, the model is not public since it's part of an academic project. Please reach out to me on [LinkedIn](https://www.linkedin.com/in/aayushpoudel/) to request access. 
