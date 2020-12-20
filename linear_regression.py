import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import argparse

# import common
# from sklearn.model_selection import train_test_split
# from Linear_Regression import *
from kNN import *

# from sklearn.linear_model import LinearRegression, LogisticRegression
# import sklearn.datasets as ds

def classify(predicts):
    size = predicts.shape[0]
    sum = np.sum(predicts)
    result = sum / size

    if result > 0.5: return 1
    else: return 0

def run():
    train_data = np.load('npy/train_features.npy')
    train_labels = np.load('npy/train_labels.npy')

    model = kNN(train_data, train_labels, num_neighbors=3)

    features = np.load("output/output_features.npy")
    for f in features:
        for i in range(len(f)):
            if f[i] == -1.:
                f[i] = f[i - 1]

    last_features = np.zeros((features.shape[0], 9))
    for i in range(9):
        last_features[:, i] = features[:, i + 1] - features[:, i]

    predicts = model.predict(last_features)
    if classify(predicts) == 1:
        print("It's HACK!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    else:
        print("Nice player :)")

if __name__ == "__main__":
    # parser = argparse.ArgumentParser()
    # parser.add_argument("--features_path", type=str, default="npy/features.npy", help="path to features")
    # opt = parser.parse_args()

    train_data = np.load('npy/train_features.npy')
    train_labels = np.load('npy/train_labels.npy')
    # print(train_data.shape)
    # print(train_labels.shape)

    # model = LogisticRegression()
    # model.fit(train_data, train_labels)

    model = kNN(train_data, train_labels, num_neighbors=3)

    # model = LinearRegression()
    # model.fit(train_data, train_labels)

    features = np.load("output/output_features.npy")
    for f in features:
        for i in range(len(f)):
            if f[i] == -1.:
                f[i] = f[i - 1]

    last_features = np.zeros((features.shape[0], 9))
    for i in range(9):
        last_features[:,i] = features[:,i+1] - features[:,i]

    # print(last_features)

    predicts = model.predict(last_features)
    if classify(predicts) == 1:
        print("It's HACK!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    else:
        print("Nice player :)")

    # model = kNN(train_data, train_labels, num_neighbors=5)
    # predicts = model.predict(train_data)
    # print(predicts)
    # errors = (predicts == train_labels)
    # count_right = np.sum(errors, axis=0)
    # print(count_right / predicts.shape[0])