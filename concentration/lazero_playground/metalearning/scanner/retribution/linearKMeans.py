# linear-k-means.
# how the fuck can I apply this shit?
# import pandas as pd
# use numpy instead.
import math
import numpy as np
import matplotlib.pyplot as plt
ycombinator=1
# I know shit about matricies.
# i know nothing about ML.
# one fucking tab saves you fucking eight spaces!
def Euclidean_distance(feat_one, feat_two):
    squared_distance = 0
    #Assuming correct input to the function where the lengths of two features are the same
    for i in range(len(feat_one)):
        # only my fucking unicode parser will fix this mother fucking problem.
            # squared_distance+=(feat_one[i] – feat_two[i])**2
            # fucking idiot.
            squared_distance+=(feat_one[i]-feat_two[i])**2
    ed = math.sqrt(squared_distance)
    return ed

def linearDistance(a,b):
    return abs(a-b)

class K_Means:
    def __init__(self, k =5, tolerance = 0.0001, max_iterations = 500):
        self.k = k # the number of centers.
# what is this k?
# trinity?
        self.tolerance = tolerance
        self.max_iterations = max_iterations
    def fit(self, data):

        self.centroids = {}

        #initialize the centroids, the first 'k' elements in the dataset will be our initial centroids
        for i in range(self.k):
            self.centroids[i] = data[i]

        #begin iterations
        for i in range(self.max_iterations):
            self.classes = {}
            for i in range(self.k):
                self.classes[i] = []

                #find the distance between the point and cluster; choose the nearest centroid
            for features in data:
        # fuck you!
                distances = [linearDistance(features,self.centroids[centroid]) for centroid in self.centroids]
                classification = distances.index(min(distances))
                self.classes[classification].append(features)

            previous = dict(self.centroids)

                #average the cluster datapoints to re-calculate the centroids
            for classification in self.classes:
                self.centroids[classification] = np.average(self.classes[classification], axis = 0)

            isOptimal = True

            for centroid in self.centroids:

                original_centroid = previous[centroid]
                curr = self.centroids[centroid]

                if np.sum((curr - original_centroid)/original_centroid * 100.0) > self.tolerance:
                    isOptimal = False

                #break out of the main loop if the results are optimal, ie. the centroids don't change their positions much(more than our tolerance)
                if isOptimal:
                    break

    def pred(self, data):
        distances = [linearDistance(data,self.centroids[centroid]) for centroid in self.centroids]
        classification = distances.index(min(distances))
        return classification
# get data from outside?
# i guess the most valuable thing about computer vision is the vectorization.
# determine the fucking color blocks and the relationship between colors.
# fuck the mathematicians! they are cocksuckers!
def mainShit(f0):
    X=np.array(f0)
    km = K_Means(5)
    km.fit(X)
    # Plotting starts here
    colors = 10*["r", "g", "c", "b", "k"]

    for centroid in km.centroids:
            plt.scatter(km.centroids[centroid], ycombinator, s = 130, marker = "x")

    for classification in km.classes:
            color = colors[classification]
            for features in km.classes[classification]:
                    plt.scatter(features,ycombinator, color = color,s = 30)
    plt.show()
    # easy to see. two fucking center. simple fucking algorithm.
    # it is time to simplify this shit.
    # but how to determine the number of centers?
    # never mind use the fucking number to determine. the biggest one is the things.
