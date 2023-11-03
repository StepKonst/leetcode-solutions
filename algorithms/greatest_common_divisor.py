class Solution:
    # Euclidean algorithm for searching gcd
    def euclidean_algorithm(self, a: int, b: int) -> int:
        """
        Calculates the greatest common divisor (GCD) of two integers.

        Parameters:
            a (int): The first integer.
            b (int): The second integer.

        Returns:
            int: The greatest common divisor of a and b.
        """
        while b:
            a, b = b, a % b
        return a
