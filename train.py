import json
import nltk_utils
import torch
# import torch.nn as nn

from torch.utils.data import Dataset, DataLoader
import numpy as np


with open("indents.json", mode='r') as file:
    intents = json.load(file)

# print(indents)
tags = []
all_words = []
xy = []



for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)
    for pattern in intent['patterns']:
        tokenize_words = nltk_utils.tokenize(pattern)
        all_words.extend(tokenize_words)
        xy.append((tokenize_words, tag))

neglect_words = ['?', ',', '.', '!']
all_words = [nltk_utils.stem(word=word) for word in all_words if word not in neglect_words]
all_words = sorted((set(all_words)))
tags = sorted(set(tags))
# print(tags)
# print()
# print(all_words)
# print()
# print(xy)

x_train = []
y_train = []
for (pattern_sentence, tag) in xy:
    bag = nltk_utils.bag_of_words(pattern_sentence, all_words)
    x_train.append(bag)
    label = tags.index(tag)
    y_train.append(label)

x_train = np.array(x_train)
y_train = np.array(y_train)


class ChatDataset(Dataset):
    def __init__(self):
        self.n_samples = len(x_train)
        self.x_data = x_train
        self.y_data = y_train


    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    def __len__(self):
        return self.n_samples


batch_size = 8
dataset = ChatDataset()
train_loader = DataLoader(dataset=dataset, batch_size=batch_size, shuffle=True, num_workers=2)
print(x_train)
print()
print(y_train)
