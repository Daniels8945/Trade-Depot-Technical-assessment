def arr(n: list[int]) -> int:
    """ A funnction that takes an array of intigers as input
        and  return the largest number"""
    
    bgst_num = n[0]
    for i in (n):
        if i > bgst_num:
            bgst_num = i
    print(bgst_num)
    return
arr(n=[ 2, 8, 19, 4, 55, 3])
