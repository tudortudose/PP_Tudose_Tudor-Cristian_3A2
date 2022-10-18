def getSong(notes, moves, start):
    song = [notes[start]]
    for m in moves:
        start = (start + m) % len(notes)
        song += [notes[start]]
    return song
