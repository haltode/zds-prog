from sys import argv
import operator
import random
import numpy as np
import matplotlib.pyplot as plt

lang_dict = {}
lang_str = ["fr", "de", "es", "pt", "eo", "it", "tr", "sv", "pl", "da", "is",
            "fi", "cs"]
nb_lang = len(lang_str)

def generate_char():
    letter = random.uniform(0.0, 100.0)

    for inter in range(0, nb_poss):
        if inter == 0 and prob[letters[inter]] >= letter:
            return letters[inter]
        if inter == nb_poss - 1:
            return letters[inter]
        elif (  letter >= prob[letters[inter]] and
                letter <= prob[letters[inter + 1]]):
            return letters[inter + 1]

def draw_chart(str):
    occurrence = {}

    # Count occurrences in the output text
    for letter in str:
        occurrence[letter] = occurrence.get(letter, 0) + 1

    # Calculate frequencies
    for letter in letters:
        if letter in occurrence:
            occurrence[letter] = occurrence[letter] / length * 100

    occur_list = sorted(occurrence.items(), key=operator.itemgetter(0))

    x_legend = sorted(occurrence.keys())
    x_length = len(x_legend)
    x_value = [occurrence[x_legend[i]] for i in range(0, x_length)]
    x2_value = [prob_original[x_legend[i]] for i in range(0, x_length)]

    y_legend = np.arange(x_length)

    bar_width = 0.35
    opacity = 0.4
    error_config = {'ecolor': '0.3'}

    fig, ax = plt.subplots()

    rects1 = plt.bar(y_legend, x_value, bar_width,
                    alpha=opacity,
                    color='b',
                    error_kw=error_config,
                    label="Generated Text")

    rects2 = plt.bar(y_legend + bar_width, x2_value, bar_width,
                    alpha=opacity,
                    color='r',
                    error_kw=error_config,
                    label="Original language")

    plt.title("Fréquence d'apparition des lettres")
    plt.xticks(y_legend + bar_width, x_legend)
    plt.legend()
    
    plt.show()

# Init language param
lang = argv[1]
if lang not in lang_str:
    raise LangError("Please specify a valid language")
for iLang in range(0, nb_lang):
    lang_dict[lang_str[iLang]] = iLang

# Get the probabilites from the .csv file and sort them by value
with open("freqLetters.csv") as f:
    # We don't need the first line
    first = f.readline()
    lines = f.readlines()
prob = {}
for line in lines:
    number = line.strip("\n").split(',')
    result = float(number[lang_dict[lang] + 1])
    # Only need letters in the language alphabet
    if result != 0:
        prob[number[0]] = result
prob_list = sorted(prob.items(), key=operator.itemgetter(1)) 

# Extract only letters from the sorted list
letters = [item[0] for item in prob_list]
nb_poss = len(letters)

# Cumulate values in dict (but conserve original probabilities)
prob_original = prob.copy()
for letter in range(1, nb_poss):
    prob[letters[letter]] += prob[letters[letter - 1]]

# Generate the output string
length = int(argv[2])
output = ""
for iChar in range(0, length):
    output += generate_char()

print(output)

draw_chart(output)
