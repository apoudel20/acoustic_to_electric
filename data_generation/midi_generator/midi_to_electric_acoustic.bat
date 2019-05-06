python random_midi_generator.py
cd ..\fluidsynth_binaries
fluidsynth.exe -F "..\synthesized_wav\random_acoustic.wav" "..\generated_midi\random.mid" "..\soundfonts\acoustic.sf2"
fluidsynth.exe -F "..\synthesized_wav\random_electric.wav" "..\generated_midi\random.mid" "..\soundfonts\electric.sf2"
