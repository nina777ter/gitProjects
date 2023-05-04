# H/W: FuzzBuzz ./fuzz_buzz.py
# create condition that prints 'Fuzz' if number is dividable by 3,
# returns 'Buzz' if number is dividable by 5, returns 'FuzzBuzz' if the number dividable by 15

# Sample inputs/outputs:
# num = 3  # output 'Fuzz' -> True/False -> Pass/Fail
# num = 27  # output 'Fuzz' -> Pass/Fail
# num = 10  # output 'Buzz' -> Pass/Fail
# num = 30  # output 'FuzzBuzz' -> Pass/Fail
# num = 45  # output 'FuzzBuzz' -> Pass/Fail
# num = 100  # output 'Buzz' -> Pass/Fail
# num = 0  # output 'Not Valid Entry', for any input less than 3 -> Pass/Fail
# num = 'a'  # output 'Not Valid Entry', for any input other than integer -> Pass/Fail
# num = ''  # output 'Not Valid Entry', for any input other than integer -> Pass/Fail
# num = '\t'  # output 'Not Valid Entry', for any input other than integer -> Pass/Fail

# H/W
# for num in range(1, 21):
#     string = ""
#     if num % 3 == 0:
#         string = string + "Fuzz"  # string=Fuzz
#     if num % 5 == 0:
#         string = string + "Buzz"  # sting=FuzzBuzz
#     if num % 5 != 0 and num % 3 != 0:
#         string = string + str(num)  # string = '' + 1 = 1
#     print(string)
# print('-------------------------------')

def fizz_buzz(num):
    string = ""
    if num % 3 == 0:
        string = string + "Fuzz"  # string=Fuzz
    if num % 5 == 0:
        string = string + "Buzz"  # sting=FuzzBuzz
    if num % 5 != 0 and num % 3 != 0:
        string = string + str(num)  # string = '' + 1 = 1
    return string


print(fizz_buzz(15) == 'FuzzBuzz')  # comparison of function result and string 'FuzzBuzz'
print(fizz_buzz(3) == 'Fuzz')
print(fizz_buzz(45) == 'FuzzBuzz')
print(fizz_buzz(5) == 'Buzz')
# print(fizz_buzz('a') == 'Not Valid Entry') # special cases were not handled in the solution
# assert is builtin python statement that verifies the actual result with expected, if matches it goes next line
# if fails (expression returns false) code execution stops at that line, and you get AssertError
assert fizz_buzz(15) == 'FuzzBuzz', f'fizz_buzz(15) failed, please check this case.'

print('assert is executed')