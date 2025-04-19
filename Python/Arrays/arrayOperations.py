def Operations(li):
    i = 0
    sum_arr = 0
    max_value = int(li[0])
    while i < len(li):
        sum_arr += int(li[i])
        if int(li[i])>max_value:
            max_value = int(li[i])
        i += 1
    avg = sum_arr//len(li)
    return [sum_arr, avg, max_value]

if __name__=='__main__':
    n = int(input())
    arr = input().strip().split(" ")
    print(arr)
    result = Operations(arr)
    print(result)        