class Solution:
    # Not effective algorithm
    def fib1(self, n: int) -> int:
        """
        Calculate the Fibonacci number at position n.

        Args:
            n (int): The position of the Fibonacci number to calculate.

        Returns:
            int: The Fibonacci number at position n.
        """
        if n <= 1:
            return n
        else:
            return self.fib1(n - 1) + self.fib1(n - 2)

    # More efficient algorithm
    def fib2(self, n: int) -> int:
        """
        Calculate the Fibonacci number at position `n`.

        Parameters:
            n (int): The position of the Fibonacci number to calculate.

        Returns:
            int: The Fibonacci number at position `n`.
        """
        values = [0, 1]
        for i in range(2, n + 1):
            values.append(values[i - 1] + values[i - 2])
        return values[n]

    # Much more efficient algorithm
    def fib3(self, n: int) -> int:
        """
        Generates the nth number in the Fibonacci sequence.

        Parameters:
            n (int): The position of the number in the Fibonacci sequence to generate.

        Returns:
            int: The nth number in the Fibonacci sequence.
        """
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b

    # Search last digit of fib number
    def fib_digit(self, n: int) -> int:
        """
        Calculates the nth digit of the Fibonacci sequence modulo 10.

        :param n: The index of the digit to calculate.
        :type n: int
        :return: The nth digit of the Fibonacci sequence modulo 10.
        :rtype: int
        """
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, (a + b) % 10
        return b

    # Finding the remainder of the division of the nth fib number by mod
    def fib_mod(self, n: int, mod: int) -> int:
        """
        Calculate the Fibonacci number at position `n` modulo `mod`.

        Parameters:
            n (int): The position of the Fibonacci number.
            mod (int): The modulo value.

        Returns:
            int: The Fibonacci number at position `n` modulo `mod`.
        """
        start_position = [0, 1]
        i = 2
        while not (start_position[i - 2] == 0 and start_position[i - 1] == 1) or i <= 2:
            start_position.append((start_position[i - 2] + start_position[i - 1]) % mod)
            i += 1
        return start_position[n % (i - 2)]
