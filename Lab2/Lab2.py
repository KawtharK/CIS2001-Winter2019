import Progression

simple_progression = Progression.Progression()
simple_progression.print_progression(10)

arithmetic_progression = Progression.ArithmeticProgression(2)
arithmetic_progression.print_progression(10)

geometric_progression = Progression.GeometricProgression(2)
geometric_progression.print_progression(10)

fib = Progression.FibonacciProgression()
fib.print_progression(10)