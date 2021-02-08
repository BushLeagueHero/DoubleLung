import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer=LancasterStemmer()
from nltk.tokenize import word_tokenize as wt
nltk.download('punkt')

import numpy
import tflearn
import tensorflow as tf
from tensorflow.python.framework import ops


import random
import pickle

import json

class AIStats():
    with open('./lib/ai/training/data/nn_stats.json') as f:
        model_data = json.load(f)

    words = []
    labels = []
    x=[]
    y=[]

    for intent in model_data['intents']:
        for pattern in intent['pattern']:
            scrape = wt(pattern)
            words.extend(scrape)
            x.append(scrape)
            y.append(intent["tag"])

        if intent["tag"] not in labels:
            labels.append(intent["tag"])

    words = [stemmer.stem(w.lower()) for w in words if w != "?" or w != "speciescommand" or w != "locationcommand" or w != "weaponcommand" or w != "ammocommand" or w != "callercommand" or w != "scentcommand"]
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

    neur_net = tflearn.input_data(shape=[None,len(training[0])])
    neur_net = tflearn.fully_connected(neur_net,8)
    neur_net = tflearn.fully_connected(neur_net,8)
    neur_net = tflearn.fully_connected(neur_net,len(output[0]),activation="softmax")
    neur_net = tflearn.regression(neur_net)

    model = tflearn.DNN(neur_net)

    model.fit(training,output,n_epoch=500,batch_size=8,show_metric=True)
    model.save('./lib/ai/stats_model.tflearn')

# def conversion_to_stat(question,words):
#     user_bag = [0 for _ in range(len(words))]

#     user_words = nltk.word_tokenize(question)
#     user_words = [stemmer.stem(w.lower()) for w in user_words]

#     for s in user_words:
#         for i,w in enumerate(words):
#             if w == s:
#                 user_bag[i] = 1

#     return numpy.array(user_bag)

# def intake_question():
#     while True:
#         question = input("AskBot: ")
#         if question.lower() == "quit":
#             break

#         results = AIStats.model.predict([conversion_to_stat(question, AIStats.words)])
#         results_index = numpy.argmax(results)
#         tag = AIStats.labels[results_index]

#         for t in AIStats.stat_data["intents"]:
#             if t["tag"] == tag:
#                 response = t["response"]

#         print(response)

# intake_question()