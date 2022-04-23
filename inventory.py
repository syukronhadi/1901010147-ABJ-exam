file = open ("db-inventory.txt","a")
while True:
    tidak = input ("Input data inventory baru? (ya/tidak)")
    if tidak == 'tidak':
        file = open ("db-inventory.txt","r")
        for item in file:
            item = item.strip()
            print(item)
        break
    elif tidak == 'ya':
        print("****************************************************")
        x = input ("Nama Perangkat : ")
        y = input ("Lokasi : ")
        file.write("Nama Perangkat : " + x + ", Lokasi : " + y + "\n")
        print("----------------------------------------------------")
file.close()