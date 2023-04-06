endEUI64 = ""
startEU64 = ""

while (True):
    mac = input("Enter MAC address (XX-XX-XX-XX-XX-XX): ")

    correct = True
    count = 0
    for i in mac.split("-"):
        count += 1

        try:
            int(i, 16)
        except ValueError:
            print("Invalid MAC address")
            correct = False
            break

        if len(i) != 2:
            print("Invalid MAC address")
            correct = False
            break

    if (correct == True and count == 6):
        mac = mac.replace("-", "")
        mac = mac.upper()
        endEUI64 = ":" + mac[0:4] + ":" + mac[4:6] + \
            "FF:FE" + mac[6:8] + ":" + mac[8:12]
        break

while (True):
    startIPv6 = input("Enter IPv6 address (XXXX:XXXX:XXXX:XXXX): ")

    # Check if IPv6 address is correct
    correct = True
    count = 0
    for i in startIPv6.split(":"):
        count += 1
        
        try:
            int(i, 16)
        except ValueError:
            print("Invalid IPv6 address")
            correct = False
            break
        
        if len(i) != 4:
            print("Invalid IPv6 address")
            correct = False
            break

    if (correct == True and count == 4):
        startEUI64 = startIPv6.upper()
        break

print("\nEUI-64 address is: " + endEUI64)
print("IPv6 address is: " + startEUI64 + endEUI64)
