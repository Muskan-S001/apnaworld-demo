def buildings(li):
    i = 0
    max_value = int(li[0])
    while i < len(li):
        if int(li[i])>max_value:
            max_value = int(li[i])
        i += 1
    print(max_value)    
    
    
    current_val = max_value
    while current_val >= 1:
        i = 0
        while i<len(li):
            if current_val<=int(li[i]):
                print("\t*", end="")
            else:
                print("\t", end="")
            i += 1
        print()
        current_val -= 1

if __name__=='__main__':
    n = int(input())
    arr = input().strip().split(" ")   
    print(arr)
    buildings(arr)                      