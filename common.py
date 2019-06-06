def write_file(path, data):
    with open(path, 'wb') as io:
        io.write(data)