# !/usr/bin/env python3
# Created by: Carolyn Webster Pless
# Created on: 2022/12/18
# Get the user input for 5 integers and a sum.
# Uses a function to determine the integer pairs.
# Displays it back to the user.

# Function to find pairs
def sumList(list_1, list_2, sum_user):
    # Variables
    sum_answer = sum_user
    counter = 0
    counter_2 = 1
    # Reversing the list in order from highest to lowest
    list_1.sort(reverse=True)
    list_2.sort(reverse=True)

    # For loops which will go through every possible combination starting from the first index
    for counter_2 in range(5):
        # List 1 stays at the same index throughout the loop until the loop changes
        list_1[counter]
        # List 2 goes through the rest of the numbers to be able to compare numbers in the list
        list_2[counter_2]
        # Sum is both lists together
        sum = list_1[counter] + list_2[counter_2]
        # If the sum is equal to the answer, creates a list and appends both other lists to it.
        # Returns it back to main()
        if sum == sum_answer:
            pairs_list = []
            pairs_list.append(list_1[counter])
            pairs_list.append(list_2[counter_2])
            return pairs_list
        if sum == sum_answer:
            # Increments the counter
            counter = counter + 1
        # Else, the pairs list is set to 0
        else:
            pairs_list = 0
        # Once counter_2 goes up to 4, list_1 moves up to the next number and list_2 goes through the other combinations.
        if counter_2 == 4:
            counter_2 = 1
            counter = counter + 1
            for counter_2 in range(5):
                list_1[counter]
                list_2[counter_2]
                # Sum is both lists together
                sum = list_1[counter] + list_2[counter_2]
                # If the sum is the answer
                if sum == sum_answer:
                    pairs_list = []
                    pairs_list.append(list_1[counter])
                    pairs_list.append(list_2[counter_2])
                    return pairs_list
                if sum == sum_answer:
                    counter = counter + 1
                # Else pairs list at 0
                else:
                    pairs_list = 0
                # Repeating the process
                if counter_2 == 4:
                    counter_2 = 1
                    counter = counter + 1
                    for counter_2 in range(3):
                        list_1[counter]
                        list_2[counter_2]
                        # Sum is both lists together
                        sum = list_1[counter] + list_2[counter_2]
                        # If the sum is the answer
                        if sum == sum_answer:
                            pairs_list = []
                            pairs_list.append(list_1[counter])
                            pairs_list.append(list_2[counter_2])
                            return pairs_list
                        if sum == sum_answer:
                            counter = counter + 1
                        # Else pairs list is 0
                        else:
                            pairs_list = 0
                        # Final combination
                        if counter_2 == 3:
                            counter_2 = 1
                            counter = counter + 1
                            for counter_2 in range(2):
                                list_1[counter]
                                list_2[counter_2]
                                # Sum is both lists together
                                sum = list_1[counter] + list_2[counter_2]
                                # If the sum is the answer
                                if sum == sum_answer:
                                    pairs_list = []
                                    pairs_list.append(list_1[counter])
                                    pairs_list.append(list_2[counter_2])
                                    return pairs_list
                                # No else statement this time in case there was a pair in the last
                                # for loops
                                if sum == sum_answer:
                                    counter = counter + 1
                                counter_2 = counter_2 + 1
        counter_2 = counter_2 + 1

    # If the pairs list is 0, that means there were no combinations anywhere. Returns -1
    if pairs_list == 0:
        return -1


# main()
def main():
    # Variables
    user_list_1 = []
    user_list_2 = []
    loop_counter = 0

    # Title
    print("Sum Pairs!")

    # For loop to ask the user for 5 numbers and appends it to the list
    for loop_counter in range(0, 5):
        user_number_string = input("Enter a number: ")
        # Try Catch to make sure the input is an integer
        try:
            user_number = int(user_number_string)
        except Exception:
            print("please enter an integer!")
        else:
            user_list_1.append(user_number)
            print("{} added to the list ".format(user_list_1[loop_counter]))
            user_list_2.append(user_number)

    # Input for the sum
    user_sum_string = input("Enter the number you would like as the sum: ")

    # try catch for the sum
    try:
        user_sum = int(user_sum_string)
    except Exception:
        print("Please enter an integer!")
    else:
        # Calling the function
        pairs = sumList(user_list_1, user_list_2, user_sum)
        # If the function returned -1, that means there are no pairs
        if pairs == -1:
            print("Sorry, none of your numbers equals {}".format(user_sum))
        else:
            # Else there are pairs. Displays them back to user
            print("The pairs are:")
            print("{}".format(pairs))


if __name__ == "__main__":
    main()
