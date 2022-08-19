import sys
s = open(sys.argv[2], "w", encoding = "utf-8")
f = open(sys.argv[1],"rb",)
textak = f.read()


kolik = textak.count(b"\x24\x08")
print("pocet",kolik)

pozice1 = textak.find(b"\x24\x08")
offset = f.seek(pozice1+16) 
size = f.read(2)
print("delka hex",size)
langsize = int.from_bytes(size,byteorder="little")
print("delka",langsize)
