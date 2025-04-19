def arrayProb(k, arr):
    count = 0
    i = 0
    while i < len(arr) -  1:
        if int(arr[i])+int(arr[i+1])==k:
            count += 1
        i += 1
    print(count)

if __name__ =='__main__':
    takeinput = input().strip().split(" ")
    arr = input().strip().split(" ")
    k = int(takeinput[1])
    arrayProb(k, arr)    