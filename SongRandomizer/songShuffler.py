import numpy as np

# returns a random permutation containing every number between start and end (both inclusive)
start = 1
end = 20

songs = [None] * (end - start + 1)
index = end - start + 1

def randomize(start, end):
    length = end - start + 1
    songs = [None] * length
    visited = [False] * length
    index = 0

    while index < length:
        song = np.random.randint(start, end + 1)
        while visited[song - start] is True:
            song = np.random.randint(start, end + 1)

        songs[index] = song
        index += 1
        visited[song - start] = True

    return songs