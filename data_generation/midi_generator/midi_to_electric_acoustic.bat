python random_midi_generator.py
cd ..\fluidsynth_binaries
for /F %%i in ('dir /b ..\generated_midi\test\') do fluidsynth.exe -F "..\synthesized_wav\acoustic_test_%%i.wav" "..\generated_midi\test\%%i" "..\soundfonts\Nylon Guitar.sf2" && fluidsynth.exe -F "..\synthesized_wav\electric_test_%%i.wav" "..\generated_midi\test\%%i" "..\soundfonts\Heavy.sf2"
