import nltk
from nltk import word_tokenize
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

import json
from itertools import permutations as perm


data_set = json.load(open('./lib/ai/training/data/test/nn_commands_test.json'))



#iterate question
def iterate_question(question):
    iterate = word_tokenize(question)

    scrub_question(iterate)

#scrub question
def scrub_question(question):
    stemmed_question = []
    
    for w in question:
        stemmed_question.append(stemmer.stem(w))

    concantonate_question(stemmed_question)
#concantonate question
def concantonate_question(question):
    perm_question = []
    for i in range(1,len(question)+1):
        perm_question.append(list(''.join(w) for w in perm(question,i) if w != "." or w != "!" or w != "?"))

    full_list = []
    for l in perm_question:
        for w in l:
            full_list.append(w)

    match_to_dict(full_list)

#match to dict
def match_to_dict(question):
    tagged_word = []
    tagged_command = []
    for i in data_set:
        for key,values in data_set[i].items():
            for v in values:
                for w in question:
                    if w == v:
                        tagged_word.append(v)
                        if i not in tagged_command:
                            tagged_command.append(i)

    print(tagged_word,tagged_command)
    #if no match - ai nlp

#output result

    #if no result - error message

#call command


#obtain question
iterate_question(input("AskBot: "))


#create one stop command processing