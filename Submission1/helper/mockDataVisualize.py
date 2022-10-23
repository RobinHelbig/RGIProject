from random import randrange
from typing import Dict, List

#I assume that we can a dict in form of:
# key = sentence
# value = how important it is, in my example it will be 4 most important, 0 least important


def transfer_function_output_ranking(list_of_sentences: List[str], most_important_sentences: List[str]) -> Dict[str, int]:
    ranking = {}
    for sentence in list_of_sentences:
        if sentence in most_important_sentences:
            if most_important_sentences.index(sentence) > (len(most_important_sentences)/2):
                ranking[sentence] = 1
            else:
                ranking[sentence] = 2
        else:
            ranking[sentence] = 0

    return ranking
