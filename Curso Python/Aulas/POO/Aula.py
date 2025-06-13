def soma(num1, num2):
    if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
        return num1 + num2
    else:
        return None

print(soma(1, 3.5))
print(soma('1', 2))