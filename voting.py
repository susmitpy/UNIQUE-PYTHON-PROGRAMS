from vote import option
import re, os
######## MAIN CONTENT
def main():
    def close(yesc, noc, maybec):
        with open("votedata.txt", "w") as a:
            a.write("{} {} {}".format(yesc, noc, maybec))
    with open("votedata.txt", "r") as a:
        text = a.read()
        nums = re.findall(r'\d{1,3}', text)
        vote_counts = [int(i) for i in nums]
    yn = vote_counts[0]
    nn = vote_counts[1]
    mn = vote_counts[2]
    ######## DEFINING THE OPTIONS
    y = option("YES", yn)
    n = option("NO", nn)
    m = option("MAYBE", mn)
    #####################
    print("The question: Is 5 + 3 equal to 8?")
    print("Currenty The Situation Is:")
    print("YES : {} \nNO: {} \nMAYBE : {}".format(yn, nn, mn))
    a = input("Press Enter to begin Voting:\n")
    comp = False
    while comp == False:
        v = input("Press 'y' for 'YES', 'n' for 'NO', 'm' for 'MAYBE', 's' to 'STOP:'\n").upper()
        os.system("cls")
        print("The question: Is 5 + 3 equal to 8?") 
        if v == "Y":
            y.upvote()
        elif v == "N":
            n.upvote()
        elif v == "M":
            m.upvote()
        elif v == "S":
            a = input("Press Enter To Exit")
            comp = True
    yesc = y.count
    noc = n.count
    maybec = m.count
    close(yesc, noc, maybec)
main()

        
        


