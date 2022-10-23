music_list = ['BROTHERS IN ARMS', 'BOHEMIAN RHAPSODY', 'STAIRWAY TO HEVEN', 'RIDERS ON THE STORM', 'WISH YOU WERE HERE']

print(music_list)

music_list.append('CHILD IN TIME')
music_list.append('AGAIN')

print(music_list)

music_list.insert(2, 'HOTEL CALIFORNIA')

print(music_list)

music_list.insert(0, 'THE SOUND OF SILENCE')

print(music_list)

print(music_list.index('HOTEL CALIFORNIA'))

music_list.remove('HOTEL CALIFORNIA')
print(music_list)

music_list[0] = 'ENJOY THE SILENCE'
print(music_list)

hits_to_read = music_list.copy()
print(hits_to_read)

hits_to_read.reverse()
print(hits_to_read)

hits_to_read.sort()
print(hits_to_read)


print(hits_to_read.pop(0))
print(hits_to_read.pop(0))
print(hits_to_read)

additional_songs = ['NOTHING COMPARES 2 YOU', 'WISH YOU WERE HERE']
print(additional_songs)

hits_to_read.extend(additional_songs)

print(hits_to_read)

print(hits_to_read.count('RIDERS ON THE STORM'))
print(hits_to_read.count('WISH YOU WERE HERE'))


hits_to_read.clear()
print(hits_to_read)


