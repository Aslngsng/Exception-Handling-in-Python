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
        if chosen_operation.upper() not in ["ADDITION, SUBTRACTION, MULTIPLICATION, OR DIVISION"]:
            raise TypeError ("Operation is not available!")
        
        first_number = int(input("Enter first number: "))
        second_number = int(input("Enter second number: "))

        if chosen_operation == "ADDITION":
            result = first_number + second_number
            print = ("The sum is " + result)
        elif chosen_operation == "SUBTRACTION": 
            fresult = first_number - second_number
            print = ("The difference is " + result)
        elif chosen_operation == "MULTIPLICATION":
            result = first_number * second_number
            print = ("The product is " + result)
        elif chosen_operation == "DIVISION":
            if second_number == 0:
                raise ValueError ("Sorry! You are dividing by zero")
            result = first_number / second_number
            print = ("The quotient is " + result)

        ask_the_user_if_they_want_to_try_again = print("Do you want to try again? (YES/NO): ").upper()
        if ask_the_user_if_they_want_to_try_again.upper() != "YES":
            print ("Thank you")
            break
    except Exception as error:
        print("An error occured: " + error)
