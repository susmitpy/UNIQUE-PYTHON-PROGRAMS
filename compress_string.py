"""
This Program Compresses String.
For Example:
a -> a
aaa - > a3
aabcc -> a2bc2
"""

def compressString(s):
    cs = ""    #Compressed String
    count = 0  #Count of subsequent Occurence of  Each Char
    prev = None #Previous Character
    l = len(s)  #Length of The GIven String

    for index, value in enumerate(s):
        if index == 0:    # If the character is the first character in the string
            prev = value    
            count = 1   #First Occurence

        else:
            if value == prev:   #The Current char equals the previous char.
                count += 1       #Increasing the Count

            else:               #The Current char DOES NOT equals the previous char.
                if count == 1:  # a -> a
                    cs += prev
                    count = 1
                    prev = value

                else:
                    cs += prev + str(count)
                    prev = value
                    count = 1
        # For The Last char or Subsequent Occurences of a char.
        if index == l - 1:
            if count == 1:
                    cs += prev
            else:
                    cs += prev + str(count)
                    
    print(cs)

while True:
    s = input("Enter The String To Be Compressed: ")  #Taking input
    compressString(s)                                  #Calling The Function
        
