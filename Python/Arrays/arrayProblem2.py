def arrayProb(arr):
    count = 0
    i = 0
    while i < len(arr):
        if int(arr[i]) > 35:
            count += 1
        i += 1
    print(count)

if __name__ == '__main__':
    n = int(input())
    arr = input().strip().split(" ")
    arrayProb(arr)            
