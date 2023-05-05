import random
from dictionaries.dictionary_low import dictionary_low
import numpy as np



@staticmethod
def guess_the_word():
    answer = draw_a_word()
    print('Słowo ma ' + str(len(answer)) + ' liter. Wpisz słowo:')
    print(answer)
    count = 1
    right_answer = ''
    while count <= 15:
        word = input()
        word_list = list(word.lower())
        temp_answer = checking_word(word_list, answer)
        if len(right_answer) < len(temp_answer):
            right_answer = temp_answer.lower()
            print("Prawidłowy początek: " + right_answer + "...")
            print("Pozostało " + str(15-count) + " prób.")

            if word_list == answer:
                print('Udało się zgadnąć odpowiedź! Wykorzystano prób:')
                break
        elif (len(right_answer) != 0):
            print("Prawidłowy początek: " + right_answer + "...")
            print("Pozostało " + str(15-count) + " prób.")
        else:
            print("Niestety nie... Pozostało " + str(15-count) + " prób.")
        count += 1
    return count


@staticmethod
def checking_word(inputed, answer):
    correct = ''
    i = 0
    for x in inputed:
        if inputed[i] == answer[i]:
            correct += inputed[i]
            i += 1
        else:
            return correct
            break
    correct = correct
    return correct

@staticmethod
def next_char(correct):
    # odpowiedź użytkownika "right answer" sprawdza długość posiadaną i bierze
    # kolejny znak z answer i sprawdza w asci, czy wypisać
    # "v" jako znak niżej, czy "^" jako kolejny znak jest wyżej.
    return 0


@staticmethod
def draw_a_word():
    ans = list(random.choice(dictionary_low))
    for x in ans:
        x.lower()
    return ans

@staticmethod
def cut_word():
    return 0