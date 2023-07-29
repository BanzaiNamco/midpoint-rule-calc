#TO DO: implement round half up?
#TO DO: implement graph????
#TO DO: uncomment try except
#TO DO: check if outputs are correct

#import sympy parse_expr to parse the user input into a function
from sympy.parsing.sympy_parser import parse_expr
import math

def get_function():
    user_input = input("Enter your function: ")
    return user_input

def get_bounds():
    lower_bound = float(input("Enter your lower bound: "))
    upper_bound = float(input("Enter your upper bound: "))
    return (lower_bound, upper_bound)

def get_num_of_intervals():
    num_of_intervals = int(input("Enter the number of intervals: "))
    return num_of_intervals

def get_deltaX(lower_bound, upper_bound, num_of_intervals):
    deltaX = (upper_bound - lower_bound) / num_of_intervals
    return deltaX

def solve_function(function, x):
    answer = parse_expr(function, {'x' : x},transformations='all')
    return answer

def main():
    # try:
        function = get_function()
        lower_bound, upper_bound = get_bounds()
        intervals = get_num_of_intervals()
        deltaX = get_deltaX(lower_bound, upper_bound, intervals)
        midpoint = deltaX /2

        fx = lower_bound + midpoint
        sumofFx = 0
        for _ in range(intervals):
            sumofFx += solve_function(function, fx)
            fx += deltaX

        answer = deltaX * sumofFx
        print(round(answer, 4))
    # except:
        # print("An error occurred, please recheck if all your inputs are valid")

if __name__ == "__main__":
    main()