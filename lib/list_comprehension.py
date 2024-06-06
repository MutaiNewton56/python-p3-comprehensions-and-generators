#!/usr/bin/env python3

def return_evens(int_list):
    return [x for x in int_list if x % 2 == 0]

# Example usage:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = return_evens(numbers)



def make_exclamation(sentences):
    return [sentence + '!' for sentence in sentences]

sentences = ["Hello", "How are you", "Good morning", "Goodbye"]
exclamations = make_exclamation(sentences)

