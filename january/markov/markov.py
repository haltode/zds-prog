from sys import argv
import random


ORDER = 2


def rearrange(content):
    new_string = ""
    for c in content:
        if c.isalpha() or c == ' ' or c == '.':
            new_string += c.lower()
    return new_string


def create_markov_chain(content, order):
    words = content.split(' ')
    chain = {}
    for start in range(len(words) - order):
        # Create a string of the specific order
        string = ""
        for i in range(order):
            string += words[start + i]
            if i != order - 1:
                string += " "
        # End of a sentence, so no actual relation with the next words
        if '.' in string:
            continue

        # Add it to the chain
        if string in chain:
            list = chain[string]
            list.append(words[start + order])
        else:
            list = [words[start + order]]
        chain[string] = list

    return chain


def generate_text(chain, limit):
    choices = list(chain.keys())
    random_start = random.randint(0, len(choices) - 1)
    nb_time = 0

    current = choices[random_start]

    while current in chain and nb_time < limit:
        possibilities = chain[current]
        suffix = random.randint(0, len(chain[current]) - 1)
        print(possibilities[suffix])

        prefix = current.split(' ')
        current = prefix[1] + " " + possibilities[suffix]

        nb_time += 1


# Input file
input = argv[1]
with open(input, "r") as f:
    content = f.read()

#content = rearrange(content)
chain = create_markov_chain(content, ORDER)
generate_text(chain, int(argv[2]))
