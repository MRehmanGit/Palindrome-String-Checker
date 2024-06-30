def removing_space(string):
    #Remove spaces from the given string and convert it to lowercase.
    string = string.lower()  # Convert the string to lowercase
    string_counter = ""  # Initialize an empty string to store the result
    for i in string:
        if i.isspace():
            continue  # Skip spaces
        else:
            string_counter += i  # Append non-space characters

    return string_counter  # Return the processed string


def palindrome_checker():
    #Check if the user-provided string is a palindrome.
    user_input = removing_space(user_string)  # Remove spaces and convert to lowercase
    print("User string : ", user_input)
    reversed_string = removing_space(user_string)[-1::-1]  # Remove spaces, convert to lowercase, and reverse the string
    print("Reversed string: ", reversed_string)

    if reversed_string == user_input:
        return 1  # Return 1 if the string is a palindrome
    else:
        return 2  # Return 2 if the string is not a palindrome


# Get input from the user
user_string = input("Enter a string: ")

# Check if the input string is a palindrome and print the result
if palindrome_checker() == 1:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
