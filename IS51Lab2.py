"""
start

acquire # of sheets
sheets / 6
round answer to next number
output result to user

finish

"""
import math

# input: sheet
def calculate(sheet):
    
    # step 1
    answer = sheet / 6
    # step 2 
    rounded = math.ceil(answer)
    print("sheet is : ", sheet)
    print("The answer is: ", answer)
    print("rounded is: ", rounded)
    print("============================")
    # output: # of stamps needed
    return rounded

output = calculate(18)

print("The number of stamps needed =: ", output)