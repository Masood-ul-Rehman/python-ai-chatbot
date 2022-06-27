import json
import nltk
import numpy
import random
import tensorflow
import tflearn
import pickle

from nltk.stem.lancaster import LancasterStemmer

nltk.download('punkt')
stemmer = LancasterStemmer()

with open('intents.json') as file:
    data = json.load(file)

try:
    with open("data.pickle", "rb") as f:
        words, labels, training, output = pickle.load(f)
except:
    words = []  # words
    labels = []  # labeles of intents
    docs_x = []  # to save tokenize words
    docs_y = []  # to save tags of previously tokenize words to understand which word refer to which tag

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            wrds = nltk.word_tokenize(pattern)  # tokenize the words
            words.extend(wrds)
            docs_x.append(wrds)  # adding tokenize words to docs_x
            # adding tag of previously tokenize words to docs_y
            docs_y.append(intent["tag"])

        if intent["tag"] not in labels:
            labels.append(intent["tag"])

    words = [stemmer.stem(w.lower())
             for w in words if w != "?"]  # removing duplicates
    words = sorted(list(set(words)))  # sorting

    labels = sorted(labels)  # sorting labeles

    training = []
    output = []

    out_empty = [0 for _ in range(len(labels))]

    for x, doc in enumerate(docs_x):
        bag = []

        wrds = [stemmer.stem(w.lower()) for w in doc]

        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)

        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1

        training.append(bag)
        output.append(output_row)

    training = numpy.array(training)
    output = numpy.array(output)

    with open("data.pickle", "wb") as f:
        pickle.dump((words, labels, training, output), f)

tensorflow.compat.v1.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
model.save("model.tflearn")

try:
    model.load("model.tflearn")
except:
    model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
    model.save("model.tflearn")


def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    return numpy.array(bag)


class search:
    def __int__(self, rep):

        def chat(inpt):
            while True:
                inp = inpt
                if inp.lower() == "quit":
                    break

                results = model.predict([bag_of_words(inp, words)])[0]
                results_index = numpy.argmax(results)
                tag = labels[results_index]

                if (results[results_index] > 0.7):
                    for tg in data["intents"]:
                        if tg['tag'] == tag:
                            responses = tg['responses']
                    return(random.choice(responses))
                else:
                    return("I'm not sure about that. Try again.")
        self.responce = chat(rep)
