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
    
    try:
        if chosen_operation.upper() not in ["ADDITION, SUBSTRACTION, MULTIPLICATION, OR DIVISION"]:
            raise TypeError ("Operation is not available!")

        if chosen_operation == "ADDITION":
            first_number = int(("Enter first number: "))
            second_number = int(("Enter second number: "))
            result = print("The sum is " + str(first_number + second_number))
        elif chosen_operation == "SUBSTRACTION":
            first_number = int(("Enter first number: "))
            second_number = int(("Enter second number: "))
            result = print("The difference is " + str(first_number - second_number))
        elif chosen_operation == "MULTIPLICATION":
            first_number = int(("Enter first number: "))
            second_number = int(("Enter second number: "))
            result = print("The product is " + str(first_number * second_number))
        elif chosen_operation == "DIVISION":
            first_number = int(("Enter first number: "))
            second_number = int(("Enter second number: "))
            if second_number == 0:
                raise ValueError ("Sorry! You are dividing by zero")
            result = print("The quotient is " + str(first_number // second_number))
    except:
        print("Unkown exeption") 
        ask_the_user_if_they_want_to_try_again = print("Do you want to try again? (YES/NO): ")
        ask_the_user_if_they_want_to_try_again = ask_the_user_if_they_want_to_try_again.upper()
        if ask_the_user_if_they_want_to_try_again.upper() != "YES":
            print ("Thank you")
        break
