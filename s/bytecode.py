# Convert the abstract syntax tables to a bytecode format that C can understand:
# i.e. dinosaur code.

def wint(i):
    # Find the optimal type for the integer (or float) first:
    o = b""
    isf = False
    if i % 1:
        isf = True
    if isf:   # Very primitive (and messy) float storage, but easy to expand on
        b = 0 # the C end.
        e = 0
        while (i/(10^e)) % 1:
            e += 1
        b = i/(10^e)
        if b >= 32767 or b <= -32767 or e >= 32767 or e <= -32767:
            o = b"F" + b.to_bytes(4, 'little') + e.to_bytes(4, 'little')
        else:
            o = b"f" + b.to_bytes(2, 'little') + e.to_bytes(2, 'little')
    else:
        if i >= 2147483647 or i <= -2147483647:
            print("What are you doing that needs 64-bit integers?")
            o = b"l" + i.to_bytes(8, 'little')
        elif i >= 32767 or i <= -32767:
            o = b"I" + i.to_bytes(4, 'little')
        else:
            o = b"i" + i.to_bytes(2, 'little')
            #print("DEBUG:: 16-bit alert")
    return o

def wstr(s):
    # Get a safe string from an unsafe one
    return b"S"+wint(len(s))+bytes(s)

def wlist(l):
    o = b"L"+wint(len(l))
    for i in l:
        o += wexp(i)
