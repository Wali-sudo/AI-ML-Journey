#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old. 

from datetime import datetime
get_name = input("Please enter your name: ")
get_age = int(input("Please enter your age: "))
current_year = datetime.now().year
year_turn_100 = current_year + (100 - get_age)
print(f"Hello {get_name}! You will turn 100 years old in the year {year_turn_100}.")

#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.

number = int(input("Please enter a number: "))
if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")

#Take a list and write a program that prints out all the elements of the list that are less than 5

list_of_numbers = []
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    list_of_numbers.append(num)
count=0
for num in list_of_numbers:
    if num < 5:
        count += 1
        print(num)
print(f"There are {count} numbers less than 5 in the list.")

#Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number.

number = int(input("Please enter a number: "))
divisors = []
for i in range(1, number + 1):
    if number % i == 0:
        divisors.append(i)
print(f"The divisors of {number} are: {divisors}")

#write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

list1 =[]
for i in range(5):
    num = int(input(f"Enter number {i+1} for list 1: "))
    list1.append(num)
list2 =[]
for i in range(7):
    num = int(input(f"Enter number {i+1} for list 2: "))
    list2.append(num)
common_elements =[]
for num in list1:
    if num in list2 and num not in common_elements:
        common_elements.append(num)
print(f"The common elements between the two lists are: {common_elements}")

#Ask the user for a string and print out whether this string is a palindrome or not

user_string = input("Please enter a string: ")
cleaned_string = user_string.replace(" ", "").lower()
if cleaned_string == cleaned_string[::-1]:
    print(f"'{user_string}' is a palindrome.")
else:
    print(f"'{user_string}' is not a palindrome.")

#Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even_elements = [num for num in a if num % 2 == 0]
print(f"The even elements in the list are: {even_elements}")

#Make a two-player Rock-Paper-Scissors  game. (Hint: Ask for player plays (using input), compare them,  print out a message of congratulations to the winner, and ask if the players want to start a new game) 

player1 = input("Player 1, enter your choice (rock, paper, scissors): ").lower()
player2 = input("Player 2, enter your choice (rock, paper, scissors): ").lower()
if player1 == player2:
    print("It's a tie!")
elif (player1 == "rock" and player2 == "scissors") or (player1 == "scissors" and player2 == "paper") or (player1 == "paper" and player2 == "rock"):
    print("Player 1 wins!")
else:
    print("Player 2 wins!") 

#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right

import random
random_number = random.randint(1, 9)
user_guess = int(input("Guess a number between 1 and 9: "))
if user_guess < random_number:
    print("Your guess is too low.")
elif user_guess > random_number:
    print("Your guess is too high.")
else:
    print("Exactly right!")

#Ask the user for a number and determine whether the number is prime or not

number = int(input("Please enter a number: "))
is_prime = True
if number <= 1:
    is_prime = False
else:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
if is_prime:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

#Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function

def get_first_and_last_elements(numbers):
    if len(numbers) < 2:
        return numbers
    return [numbers[0], numbers[-1]]
a = [5, 10, 15, 20, 25]
result = get_first_and_last_elements(a)
print(f"The first and last elements of the list are: {result}")

#Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate

def generate_fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence
num_numbers = int(input("How many Fibonacci numbers would you like to generate? "))
fibonacci_numbers = generate_fibonacci(num_numbers)
print(f"The first {num_numbers} Fibonacci numbers are: {fibonacci_numbers}")

#Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates

def remove_duplicates(input_list):
    return list(set(input_list))
user_list = []
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    user_list.append(num)
unique_list = remove_duplicates(user_list)
print(f"The list without duplicates is: {unique_list}")

#Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order.

def reverse_words(input_string):
    words = input_string.split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words
user_string = input("Please enter a long string containing multiple words: ")
reversed_string = reverse_words(user_string)
print(f"The string with words in backwards order is: '{reversed_string}'")  

#Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

import random
import string
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    while True:
        user_input = input("Would you like to generate a new password? (yes/no): ").lower()
        if user_input == "yes":
            new_password = generate_password()
            print(f"Your new password is: {new_password}")
        elif user_input == "no":
            print("Thank you for using the password generator!")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()

#Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

def is_number_in_list(ordered_list, number):
    return number in ordered_list

# Example usage:
my_list = [1, 3, 5, 7, 9]
print(is_number_in_list(my_list, 5))  # Output: True
print(is_number_in_list(my_list, 4))  # Output: False

#Take the code from the How To Decode A Website exercise (if you didn’t do it or just want to play with some different code, use the code from the solution), and instead of printing the results to a screen, write the results to a txt file. In your code, just make up a name for the file you are saving to.

with open("results.txt", "w") as f:
    f.write("This is the result of the decoding exercise.\n")
    f.write("You can add more results here as needed.\n")

#Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, and print out the results to the screen. 

with open("names.txt", "r") as f:
    names = f.readlines()
name_count = {}
for name in names:
    name = name.strip()
    if name in name_count:
        name_count[name] += 1
    else:
        name_count[name] = 1 
for name, count in name_count.items():
    print(f"{name}: {count}")

#we will keep track of when our friend’s  birthdays are, and be able to find that information based on their name. Create a dictionary (in your file) of names and birthdays. When you run your program it should ask the user to enter a name, and return the birthday of that person back to them

birthdays = {
    "Alice": "January 1",
    "Bob": "February 2",
    "Charlie": "March 3",
    "David": "April 4",
    "Eve": "May 5"
}

name = input("Enter a name: ")
if name in birthdays:
    print(f"{name}'s birthday is {birthdays[name]}.")
else:
    print("Name not found.")
    