import sys

def solve():

    y = int(sys.stdin.readline().strip()) #o(1)
    y +=1 #o(1)
    while(True): #o(1)
        y_list = list(str(y)) #o(n)
        y_set = set(y_list) #o(n)
        if len(y_set) == 4: #o(1)
            print(y) #o(1)
            break #o(1)
        y +=1 #o(1)
        


if __name__ == '__main__':
    solve() #complejidad, o(n)