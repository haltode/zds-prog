# January 2016

Link to the challenge : <https://zestedesavoir.com/forums/sujet/5039/janvier-2016-generation-automatique-de-texte/>

The goal of this month is to generate automatically a text in a specific language with different tasks.

I decided to do this one in Python, because I learned this language a few days before the challenge, and I thought this was a great way to train myself with Python.

## Charabia

The file `charabia.py` contains an algorithm to generate random strings in a language from data collected from a .csv file. The .csv file has info about frequencies in multiple languages. The program also creates a graphical output to show the frequencies of the generated text compared to those from the chosen language.

```sh
$ python charabia.py [LANG] [OUTPUT_LENGTH]
```

Example :

![Output produced by the program](charabia/output_example.png)

## Markov

The program `markov.py` generates a random text by imitating from an input file and creating a [Markov chain](https://en.wikipedia.org/wiki/Markov_chain).
