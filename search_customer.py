def search( file_name, phrase ):
    file = open(file_name, 'r')
    lines = file.readlines()

    res = []
    for line in lines:
        tuple = line.split(';')

        if phrase in tuple[0] or phrase in tuple[1] or phrase in tuple[2]:
            res.append( f"{tuple[0]}\t{tuple[1]}\t{tuple[2]}")

    return res