def copy_file_content(source, destination):
    with open(source, 'r') as f_source:
        with open(destination, 'w') as f_dest:
            f_dest.write(f_source.read())
