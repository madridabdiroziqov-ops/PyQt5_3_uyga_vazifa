def sum_of_digits_in_string(text: str) -> int:
    num = [int(symbol) for symbol in text if symbol.isdigit()]
    s = sum(num)
    return s

print(sum_of_digits_in_string("a1b2c3d45"))
# Output: 15

print(sum_of_digits_in_string("abc"))
# Output: 0

print(sum_of_digits_in_string("9cats8dogs7"))
# Output: 24

print(sum_of_digits_in_string("hello123world"))
# Output: 6

print(sum_of_digits_in_string("0a0b0"))
# Output: 0
