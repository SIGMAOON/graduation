# import sys, os
# sys.path.append(os.pardir)

import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd
# from sklearn.model_selection import train_test_split

# import sklearn.datasets as ds
# from dataset.mnist import load_mnist

class kNN():
    def __init__(self, train_features, train_output, num_neighbors=3, FIND_OUTPUTS=False):
        self.features = train_features
        self.outputs = train_output

        self.K = num_neighbors
        self.find_outputs = FIND_OUTPUTS

    def cal_distance(self, test_features):
        cal = (self.features - test_features)**2
        cal = np.sqrt(cal.sum(axis=1))

        distances = np.zeros((cal.shape[0], 2))
        distances[:,0] = cal
        distances[:,1] = self.outputs

        return distances

    def get_neighbors(self, test_features):
        distances = self.cal_distance(test_features)
        sorted_index = np.argsort(distances[:,0], axis=0)
        neighbors = distances[sorted_index]

        return neighbors[:self.K]

    def predict(self, test_features):
        if self.find_outputs == False:
            predicts = np.array([], dtype=int)

            count = 0
            for feature in test_features:
                neighbors = self.get_neighbors(feature)
                labels, counts = np.unique(neighbors[:,1], return_counts=True)

                max_index = np.argmax(counts)
                predicts = np.append(predicts, int(labels[max_index]))

                print("Complete %08dth data" % count)
                count += 1
        else:
            predicts = np.array([], dtype=float)

            count = 0
            for feature in test_features:
                neighbors = self.get_neighbors(feature)
                predicts = np.append(predicts, np.mean(neighbors[:,1]))

                print("Complete %08dth data" % count)
                count += 1

        return predicts

    def accuracy(self, test_features, test_outputs):
        predicts = self.predict(test_features)
        print(predicts)
        print(test_outputs)

        if self.find_outputs:
            errors = (predicts - test_outputs) / test_outputs
            mean_error = np.mean(errors) * 100

            return "mean of error: %f%%" % mean_error
        else:
            corrects = predicts == test_outputs
            accuracy = (np.sum(corrects) / test_outputs.shape[0]) * 100

            return "accuracy: %f%%" % accuracy

"""
if __name__ == "__main__":
    # dataset = ds.load_iris()
    # print(dataset.DESCR)
    # print(pd.DataFrame(dataset.data).describe())
    # print(dataset.target)

    (train_data, train_labels), (test_data, test_labels) = load_mnist(flatten=True, normalize=True)

    size = 100
    batch_index = np.random.randint(0, test_data.shape[0], size)
    batch_data = test_data[batch_index]
    batch_labels = test_labels[batch_index]

    # normalized_data = min_max_normalize(dataset.data)
    # print(normalized_data)

    # train_data, test_data, train_labels, test_labels = train_test_split(dataset.data, dataset.target, test_size=0.2)
    # train_data, test_data, train_labels, test_labels = train_test_split(normalized_data, dataset.target, test_size=0.2)
    # print(train_data, train_data.shape)
    # print(test_data, test_data.shape)

    classifier = kNN(train_data, train_labels, 3, FIND_OUTPUTS=False)
    # print(classifier.predict(test_data))
    # print(test_labels)
    print(classifier.accuracy(batch_data, batch_labels))
"""