from midiutil import MIDIFile

# Create a new MIDI file
midi = MIDIFile(1)
track = 0
midi.addTempo(track, 0, 96)  # BPM is around 96

# 🎹 **Accurate Chord Progression** (Fm - Eb - Db - Bbm)
chords = [
    [53, 56, 60],  # F minor (F, Ab, C)
    [51, 55, 58],  # Eb major (Eb, G, Bb)
    [49, 53, 56],  # Db major (Db, F, Ab)
    [46, 50, 53]   # Bb minor (Bb, Db, F)
]

# 🎸 **Bassline** (F, Eb, Db, Bb) - Adds bounce with an extra note
bass_notes = [
    (41, 0), (44, 0.5),  # F to Ab
    (39, 1), (42, 1.5),  # Eb to G
    (37, 2), (41, 2.5),  # Db to F
    (34, 3), (37, 3.5)   # Bb to Db
]

# 🥁 **Drum Beat** (Hip-Hop groove)
kick_drum = 36  # MIDI note for kick
snare_drum = 38  # MIDI note for snare
hihat = 42  # MIDI note for closed hi-hat

# 🎵 **Add Chords (Syncopated)**
for i, chord in enumerate(chords):
    for note in chord:
        midi.addNote(track, 0, note, i * 2 + 0.5, 1.5, 80)  # Chords hit slightly late

# 🎵 **Add Bassline**
for note, start_time in bass_notes:
    midi.addNote(track, 1, note, start_time, 0.5, 90)  # Short bass notes

# 🥁 **Drum Pattern (Kick & Snare)**
for i in range(8):  # 8-bar loop
    midi.addNote(track, 9, kick_drum, i * 1, 0.25, 100)  # Kick on beat 1 & 3
    if i % 2 == 1:
        midi.addNote(track, 9, snare_drum, i * 1, 0.25, 100)  # Snare on 2 & 4
    midi.addNote(track, 9, hihat, i * 0.5, 0.1, 60)  # Hi-hat every 8th note

# 🎼 Save the MIDI file
filename = "dont_style.mid"
with open(filename, "wb") as midi_file:
    midi.writeFile(midi_file)

print(f"MIDI file '{filename}' created! 🎶")
