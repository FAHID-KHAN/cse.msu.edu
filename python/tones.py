from math import pow

print("Welcome to the Musical note to frequency converter ")
print("You will enter three musical notes each as an octave and pitch class ")
print("For each note:")
print("- Enter the octave number (e.g. 4 for the fourth octave).")
print("- Enter the pitch class number (0 for C, 1 for C#, ..., 11 for B)")
print()

# Reference values for A4 (octave 4, pitch class 9)
REFERENCE_OCTAVE = 4
REFERENCE_PITCH = 9
REFERENCE_FREQ = 440

octave1 = int(input("Enter octave number for note 1: "))
pitch1 = int(input("Enter pitch class for note 1: "))

octave2 = int(input("Enter octave number for note 2: "))
pitch2 = int(input("Enter pitch class for note 2: "))

octave3 = int(input("Enter octave number for note 3: "))
pitch3 = int(input("Enter pitch class for note 3: "))


def calculate_frequency(octave, pitch):
    return REFERENCE_FREQ * pow(2, (octave - REFERENCE_OCTAVE) + (pitch - REFERENCE_PITCH) / 12)

freq1 = calculate_frequency(octave1, pitch1)
freq2 = calculate_frequency(octave2, pitch2)
freq3 = calculate_frequency(octave3, pitch3)

# Print results
print(f"\nNote 1: Octave {octave1}, Pitch Class {pitch1} => Frequency: {freq1:.2f} Hz")
print(f"Note 2: Octave {octave2}, Pitch Class {pitch2} => Frequency: {freq2:.2f} Hz")
print(f"Note 3: Octave {octave3}, Pitch Class {pitch3} => Frequency: {freq3:.2f} Hz")