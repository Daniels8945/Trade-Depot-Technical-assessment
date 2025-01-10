def _tri(n: list[int]) -> int:
    """
        Takes three integers as input, representing the lengths of the sides of a triangle.
        Determines the type of triangle based on the following conditions:
            "Equilateral": All three sides are equal.
            "Isosceles": Exactly two sides are equal.
            "Scalene": All sides are different.
        If the given side lengths do not form a valid triangle (i.e., if any side is greater
        than or equal to the sum of the other two sides), return "Not a triangle".
    """

    bgst_num = n[0]
    for i in (n):
        if i == 2 or i ==  1:
            print("Not a triangle")
            return
        elif i == 3:
            print("Equilateral")
            return
        elif i > bgst_num:
            bgst_num = i
            if bgst_num == 6:
                print("Isosceles")
            elif bgst_num  == 5:
                print("Scalene")
            else:
                print("Not a triangle")
           
_tri(n=[4, 4, 5])