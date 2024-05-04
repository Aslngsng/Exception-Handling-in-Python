#ask the user to choose one of the four math operations (Addition, Subtraction, Multiplication and Division) 
#ask the user for two numbers then display the result 
#ask if the user wants to try again or not.
#if yes, proceed to step 1, if no, display “Thank you!” and the program will exit 
#Use Python Function and appropriate Exceptions to capture errors during runtime

while True:
    print("Choose an operation you want perform")
    print("ADDITION, SUBSTRACTION, MULTIPLICATION, OR DIVISION")

    chosen_operation = input("What operation would you like to choose? ")
    chosen_operation = chosen_operation.upper()

    if chosen_operation == "ADDTION":
        first_number = int(("Enter first number: "))
        second_number = int(("Enter second number: "))
        print("The sum is " + str(first_number + second_number))
    elif chosen_operation == "SUBSTRACTION":
        first_number = int(("Enter first number: "))
        second_number = int(("Enter second number: "))
        print("The difference is " + str(first_number - second_number))
    elif chosen_operation == "MULTIPLICATION":
        first_number = int(("Enter first number: "))
        second_number = int(("Enter second number: "))
        print("The product is " + str(first_number * second_number))
    elif chosen_operation == "DIVISION":
        first_number = int(("Enter first number: "))
        second_number = int(("Enter second number: "))
        print("The quotient is " + str(first_number // second_number))
    else:
        print("Invalid operation to use")

    ask_the_user_if_they_want_to_try_again = print("Do you want to try again? (YES/NO): ")
    if ask_the_user_if_they_want_to_try_again.upper() != "YES":
        print ("Thank you")
    break
