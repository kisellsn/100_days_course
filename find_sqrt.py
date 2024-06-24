
def find_sqrt(num):
    if num == 0:
        return 0
    l = 0
    r = num
    while l <= r:
        mid = (l + r) // 2
        if mid * mid == num:
            return mid
        if mid * mid < num:
            l = mid + 1
        else:
            r = mid - 1
    return r

print(find_sqrt(129))