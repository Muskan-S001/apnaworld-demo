def adding(arr1, arr2):
    i = len(arr1)-1
    j = len(arr2)-1
    n3 = max(len(arr1),len(arr2))+1
    ans = [0]*n3
    print(ans)
    k = len(ans)-1
    carry = 0
    while i>0 or j>0:
        val1 = 0
        if i>=0:
            val1 = arr1[i]
        val2 = 0
        if j>=0:
            val2 = arr2[j]
        s = int(val1) + int(val2) + carry
        carry = s//10
        ans[k] = s%10
        i -= 1
        j -= 1
        k -= 1
    if carry ==1:
        print(carry, end="")
    for k in range(0,n3):
        print(ans[k])

if __name__ == '__main__':
    n1 = int(input())
    arr1 = input().strip().split(" ")
    n2 = int(input())
    arr2 = input().strip().split(" ")
    adding(arr1, arr2)