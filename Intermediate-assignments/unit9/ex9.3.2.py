def my_mp4_playlist(file_path, new_song):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    if len(lines) < 3:
        lines += ['\n'] * (3 - len(lines))
        lines[2] = f"{new_song};Unknown;Length;\n"
    else:
        l = lines[2].split(';')
        song, singer, length = l[0], l[1], l[2]
        lines[2] = f"{new_song};{singer};{length};\n"

    with open(file_path, 'w') as f:
        f.writelines(lines)

    with open(file_path, 'r') as f:
        print(f.read())
