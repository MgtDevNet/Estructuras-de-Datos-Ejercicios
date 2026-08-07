import sys

def solve():
    n = sys.stdin.readline().strip()
    n = list(n)
    nums = set(n)
    #print(n,nums)
    if ("4" not in nums) and ("7" not in nums):
        print("NO")
    else:
        cuat = n.count("4")
        siet = n.count("7")
        res = cuat + siet
        #print(cuat,siet,res)
        if res in [4,7]:
            print("YES")
        else:
            print("NO") 

if __name__ == '__main__':
    solve()