def tambah(*data):
    output = 0

    for angka in data:
        output += angka

    return output


def kali(*data):
    output = 1

    for angka in data:
        output *= angka

    return output