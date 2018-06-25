def compressString(s):
    cs = ""
    count = 0
    prev = None
    l = len(s)

    for index, value in enumerate(s):
        if index == 0:
            prev = value
            count = 1

        else:
            if value == prev:
                count += 1

            else:
                if count == 1:
                    cs += prev
                    count = 1
                    prev = value

                else:
                    cs += prev + str(count)
                    prev = value
                    count = 1

        if index == l - 1:
            if count == 1:
                    cs += prev
            else:
                    cs += prev + str(count)
                    
    print(cs)


def deCompressString(comps):
    s = ""
    temps = ""
    prev = None
    l = len(comps)
    for index, value in enumerate(comps):
        if not value.isdigit():
            if prev == None:
                prev = value
                
                if index == l - 1:
                    s += value
            
            elif value != prev:
                 s += prev
                 prev = value

            
            

        elif value.isdigit():
            if index == 0:
                print("Wrong Input")
                break
            else:
                s += prev*(int(value))
                prev = None

            

        
            

    print(s) 
                
            
    
while True:
    common = "To {} String Type {} and Press Enter"
    print(common.format("Compress", "c"))
    print(common.format("Decompress", "d"))
    query = input("Type Here: ")
    if query == "c" or query == "C":
        s = input("Enter The String To Be Compressed: ")
        compressString(s)
    elif query == "d" or query == "D":
        s = input("Enter The String To Be Decompressed: ")
        deCompressString(s)
        
