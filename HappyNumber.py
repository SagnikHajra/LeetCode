class HappyNumber(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False

        square_of_num = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
        prev_squares = set([])

        while True:
            num = n
            sum = 0
            if n in prev_squares:
                return False
            if n == 1:
                return True

            prev_squares.add(n)

            while num > 0:
                sum += square_of_num[num % 10]
                num = num // 10
            n = sum



