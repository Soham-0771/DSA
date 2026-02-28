class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        result = [0] * (m + n)

        # Reverse iteration for digit multiplication
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                sum_ = mul + result[i + j + 1]

                result[i + j + 1] = sum_ % 10
                result[i + j] += sum_ // 10

        # Convert result to string, skipping leading zeros
        res = []
        for digit in result:
            if not res and digit == 0:
                continue
            res.append(str(digit))

        return "".join(res)
