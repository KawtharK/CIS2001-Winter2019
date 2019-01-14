import Progression

simple_progression = Progression.Progression()
simple_progression.print_progression(10)

arithmetic_progression = Progression.ArithmeticProgression(2)
arithmetic_progression.print_progression(10)

geometric_progression = Progression.GeometricProgression(2)
geometric_progression.print_progression(10)

fib = Progression.FibonacciProgression()
fib.print_progression(10)

r = 1
while r >= 1 or r < 0:
    r = float(input("Enter an r value < 1: "))

verify_sum_progression = Progression.GeometricProgression(r)
expected_sum = 1 / ( 1 - r )
actual_sum = next(verify_sum_progression)

print(expected_sum)
while abs(expected_sum-actual_sum) > .000001:
    print(actual_sum)
    actual_sum += next(verify_sum_progression)


count_of_leading_digits = {}
for number in range(10):
    count_of_leading_digits[str(number)] = 0

fib = Progression.FibonacciProgression()
for number in range(500):
    next_fib = next(fib)
    count_of_leading_digits[str(next_fib)[0]] += 1
    
for key, value in count_of_leading_digits.items():
    print(key, ":", value)