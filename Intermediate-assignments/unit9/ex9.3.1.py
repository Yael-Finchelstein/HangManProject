def my_mp3_playlist(file_path):
    with open(file_path, 'r') as f:
        songs = f.read().splitlines()

    song_list = [song.split(';') for song in songs]
    song_lengths = [song[2] for song in song_list]
    max_length_song_index = song_lengths.index(max(song_lengths))
    max_length_song_name = song_list[max_length_song_index][0]

    song_count = len(song_list)

    operations = [song[1] for song in song_list]
    operation_count = {operation: operations.count(operation) for operation in set(operations)}
    most_common_operation = max(operation_count, key=operation_count.get)

    return max_length_song_name, song_count, most_common_operation
