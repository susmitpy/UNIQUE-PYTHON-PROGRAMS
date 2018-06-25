def compressString(s):
    cs = ""
    count = 0
    prev = None
    l = len(s)

    for index, value in enumerate(s):
        if prev == None:
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

while True:
    s = input("Enter The String To Be Compressed: ")
    compressString(s)
        
