import nltk
from nltk.stem.porter import PorterStemmer
stemmer=PorterStemmer()
from nltk.tokenize import word_tokenize as wt
nltk.download('punkt')
from nltk import Tree

import numpy
import spacy
import tflearn
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.python.framework import ops
from tflearn.layers.estimator import regression


import random
import pickle

import json

class AICommands():
    with open('./lib/ai/training/data/test/nn_commands_test.json') as f:
        model_data = json.load(f)

    words = []
    labels = []
    x=[]
    y=[]

    for intent in model_data['intents']:
        for pattern in intent['pattern']:
            word = pattern.split()
            for w in word:
                cleaned_word = w.replace("'","").replace("-","").replace(".","").lower()
                scrape = wt(cleaned_word)
                words.extend(scrape)
                x.append(scrape)
                y.append(intent["tag"])

        if intent["tag"] not in labels:
            labels.append(intent["tag"])

    words = [stemmer.stem(w.lower()) for w in words if w != "?"]
    words = sorted(list(set(words)))

    labels = sorted(labels)

    training = []
    output = []

    output_setup = [0 for _ in range(len(labels))]

    for i,items in enumerate(x):
        wrd_bag = []

        items_list = [stemmer.stem(w.lower()) for w in items]

        for w in words:
            if w in items_list:
                wrd_bag.append(1)
            else:
                wrd_bag.append(0)

        output_row = output_setup[:]
        output_row[labels.index(y[i])] = 1

        training.append(wrd_bag)
        output.append(output_row)

    training = numpy.array(training)
    output = numpy.array(output)

    ops.reset_default_graph()

    sgd = tflearn.optimizers.SGD(learning_rate=0.001,decay_step=100)
   
    neur_net = tflearn.input_data(shape=[None,len(training[0])])
    neur_net = tflearn.fully_connected(neur_net,8,activation="LeakyReLU")
    neur_net = tflearn.fully_connected(neur_net,len(output[0]),activation="SoftMax")
    # neur_net = regression(neur_net)
    regression = regression(neur_net,optimizer='sgd',loss='binary_crossentropy', learning_rate=5)

    model = tflearn.DNN(regression)

    model.fit(training,output,n_epoch=1000,batch_size=64,show_metric=True,shuffle=True)
    model.save('./lib/ai/cmd_model.tflearn')

def conversion_to_command(question,words):
    user_bag = [0 for _ in range(len(words))]

    user_words = nltk.word_tokenize(question)
    user_words = [stemmer.stem(w.lower()) for w in user_words]

    print(user_words)

    for s in user_words:
        for i,w in enumerate(words):
            if w == s:
                user_bag[i] = 1

    print(user_bag)
    return numpy.array(user_bag)

def intake_question():
    while True:
        en_nlp = spacy.load("en_core_web_trf")

        question = input("AskBot: ")
        if question.lower() == "quit":
            break
        else:
            scrubbed_list = []
            doc = en_nlp(question)
            sentence = next(doc.sents)
            for word in sentence:
                print(f"{word}:{word.dep_}")
                if "sub" in word.dep_ or "obj" in word.dep_ or "amod" in word.dep_ or "compund" in word.dep_ or "num" in word.dep_:
                    scrubbed_list.append(word)
                    scrubbed_question = ' '.join(str(w) for w in scrubbed_list)

        results = AICommands.model.predict([conversion_to_command(scrubbed_question, AICommands.words)])
        results_index = numpy.argmax(results)
        tag = AICommands.labels[results_index]

        for t in AICommands.model_data["intents"]:
            if t["tag"] == tag:
                response = t["response"]

        print(response)

intake_question()