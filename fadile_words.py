import random

with open('Dictionnary.txt', 'r') as file:
    word_list = [line.strip() for line in file]
    
def jumbled_choice():
    return random.choice(word_list)

string = jumbled_choice()

def jumbled_word():
    jumbled_car = []
    for i in string:
        jumbled_car.append(i)
    print("Real : "+string.upper())
    random.shuffle(jumbled_car)
    return jumbled_car