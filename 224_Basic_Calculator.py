class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        sign = 1  # 1 for positive, -1 for negative
        num = 0

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == '+':
                result += sign * num  # Add previous number
                sign = 1             # Set sign for next
                num = 0              # Reset number
            elif char == '-':
                result += sign * num  # Add previous number
                sign = -1            # Set sign for next
                num = 0              # Reset number
            elif char == '(':
                stack.append(result) # Save current result
                stack.append(sign)   # Save current sign
                result = 0           # Reset for sub-expression
                sign = 1             # Reset sign
            elif char == ')':
                result += sign * num # Add last number in parentheses
                result *= stack.pop() # Apply sign before parentheses
                result += stack.pop() # Add result before parentheses
                num = 0              # Reset number
            # Ignore spaces

        # Add the last number if any
        result += sign * num
        return result
