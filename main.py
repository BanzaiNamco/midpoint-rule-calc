#TO DO: implement round half up?
#TO DO: implement graph????
#TO DO: uncomment try except
#TO DO: check if outputs are correct

#import sympy parse_expr to parse the user input into a function
from sympy.parsing.sympy_parser import parse_expr


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
        #get user inputs
        function = get_function()
        lower_bound, upper_bound = get_bounds()
        intervals = get_num_of_intervals()

        #solve for deltaX
        deltaX = get_deltaX(lower_bound, upper_bound, intervals)
        
        #solve for the "midpoint" of each interval
        midpoint = deltaX /2

        #get the first x for each f(x)
        x = lower_bound + midpoint

        #variable for summation of f(x)
        sumofFx = 0

        #solve for the summation of f(x)
        for _ in range(intervals):
            #get the f(x) for each interval
            sumofFx += solve_function(function, x)
            #increment the x for each interval
            x += deltaX

        #deltaX * summation of f(x)
        answer = deltaX * sumofFx

        #print the answer rounded to 4 decimals
        print(round(answer, 4))
    # except:
        # print("An error occurred, please recheck if all your inputs are valid")

if __name__ == "__main__":
    main()