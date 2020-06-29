# -*- coding: utf-8 -*-


def compact_encode(hexarray):
    term = 1 if hexarray[-1] == 16 else 0 
    if term: hexarray = hexarray[:-1]
    oddlen = len(hexarray) % 2
    flags = 2 * term + oddlen
    if oddlen:
        hexarray = [flags] + hexarray
    else:
        hexarray = [flags] + [0] + hexarray
    # hexarray now has an even length whose first nibble is the flags.
    o = ''
    for i in range(0,len(hexarray),2):
        o += chr(16 * hexarray[i] + hexarray[i+1])
    return o


def main():
    data = (
        [1, 2, 3, 4, 5],
        [0, 1, 2, 3, 4, 5],
        [0, 0xf, 1, 0xc, 0xb, 8, 0x10],
        [0xf, 1, 0xc, 0xb, 8, 0x10],
    )
    
    for hexarray in data:
        print(hexarray)
        ret = compact_encode(hexarray)
        print(ret.encode().hex())


if __name__ == "__main__":
    main()

