from sys import argv
import random


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
        # End of a sentence, so no actual relation with the next word
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


def generate_text(chain, limit, order):
    choices = list(chain.keys())
    random_start = random.randint(0, len(choices) - 1)
    nb_time = 0
    output = ""

    current = choices[random_start]

    while nb_time < limit:
        possibilities = chain[current]
        suffix = random.randint(0, len(chain[current]) - 1)
        output += possibilities[suffix] + " "

        prefix = current.split(' ')

        if order > 1:
            current = ""
            for i in range(1, order):
                current += prefix[i]
            current += " " + possibilities[suffix]
        else:
            current = possibilities[suffix]

        nb_time += 1

        if current not in chain:
            random_start = random.randint(0, len(choices) - 1)
            current = choices[random_start]

    return output


input = argv[1]
length = int(argv[2])
order = int(argv[3])

with open(input, "r") as f:
    content = f.read()

chain = create_markov_chain(content, order)
output = generate_text(chain, length, order)
print(output)
