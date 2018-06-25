"""
This Program Handles String Compression and Decompression.
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


def deCompressString(comps):
    s = ""
    prev = None
    l = len(comps)
    for index, value in enumerate(comps):
        if not value.isdigit():           # Not a digit
            if prev == None:              #First char or char after  a digit
                prev = value
                
                if index == l - 1:         #Char at last index
                    s += value  
            
            elif value != prev:
                 s += prev
                 prev = value

        elif value.isdigit():
            if index == 0:
                print("Wrong Input")     #First char cannot be a digit
                break
            else:
                s += prev*(int(value))   #Example: prev = s, value = 2 s += "ss"
                prev = None
    print(s) 
                
            
# Taking Input
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
        
