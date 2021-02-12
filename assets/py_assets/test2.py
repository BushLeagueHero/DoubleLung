import nltk
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()
from nltk.tokenize import word_tokenize as wt
nltk.download('punkt')

import json

data_set = json.load(open('./lib/ai/training/data/test/nn_commands_test.json'))

question = input('AskBot: ')

def prepare_question(question):
    question_out = []
    
    question_words = wt(question)
    for w in question_words:
        w = w.replace("'","").replace("-","").replace(".","").replace("/","").lower()
        if w != "?":
            question_out.append(stemmer.stem(w)) 

    parse_question(question_out)

def parse_question(question):   
    pass

def convert_to_command(question):
    question_data = prepare_question(question)


convert_to_command(question)