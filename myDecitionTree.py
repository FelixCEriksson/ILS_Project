


class DecisionTree:
    def __init__(self, criterion , max_features, max_depth , min_samples_leaf):

        self.criterion= criterion
        self.max_features = max_features
        self.max_depth = max_depth
        self.min_samples_leaf = min_samples_leaf
        self.root = Node(None)

    def fitness(self, X, Y):
        self.root.insert(X,Y)






class Node:

    def __init__(self, parent):
        self.parent = parent
        self.left = None
        self.right = None
        self.xValues = None
        self.yValues = None


    def insert(self, X, Y):
        self.xValues = X
        self.yValues = Y

    ##def split(self):
