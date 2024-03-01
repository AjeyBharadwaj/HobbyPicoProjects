complete_notes = '''
E4 A4 B4 C5 A4 __ E4 A4 B4 C5 A4

E4 A4 B4 C5 B4 A4 C5 B4 A4 E5 E5 E5

D5 E5 F5 F5 __ F5 E5 D5 F5 E5

D5 C5 B4 E5 C5 B4 A4

E4 A4 B4 C5 A4 __ E4 A4 B4 C5 A4

E4 A4 B4 C5 B4 A4 C5 B4 A4 E5 E5 E5

D5 E5 F5 F5 __ F5 E5 D5 F5 E5

D5 C5 B4 E5 C5 B4 A4
'''

lines = complete_notes.split("\n")
for line in lines:
    notes = line.split(" ")
    for note in notes:
        if len(note) == 0:
            continue
        if "_" in note:
             print(f"\"P\"", end=",")
        else:
            note = note.replace("\n", '')
            note = note.replace("#", "S")
            print(f"\"{note}\"", end=",")
