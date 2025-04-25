##First approach
def large(n,arr):
    ans = [0]*n
    i = 0
    while i<len(arr):
        sum_arr = 0
        j = 0
        while j<len(arr):
            sum_arr += int(arr[j])
            j += 1
        ans[i] = sum_arr - int(arr[i])
        print(ans[i], end = " ")
        i+=1
           
if __name__=='__main__':
    n = int(input())
    arr = input().strip().split(" ")
    large(n,arr)

##Second Approach
def large(n,arr):
    ans = [0]*n
    i = 0
    j = 0
    sum_arr = 0
    while j<len(arr):
        sum_arr += int(arr[j])
        j += 1
    while i<len(arr):
        ans[i] = sum_arr - int(arr[i])
        print(ans[i], end = " ")
        i+=1
           
if __name__=='__main__':
    n = int(input())
    arr = input().strip().split(" ")
    large(n,arr)

##Third Approach
def mainFunction(n, arr):
    arr = list(map(int, arr))  
    total = sum(arr)          
    ans = [0] * n
    for i in range(n):
        ans[i] = total - arr[i]
        print(ans[i], end=" ")

    print() 

if __name__ == '__main__':
    n = int(input())
    arr = input().strip().split()
    mainFunction(n, arr)


