from numpy import exp, array, random, dot, genfromtxt
import numpy

class MyNN():
    def __init__(self):
        random.seed(1)
        self.weights1stNeuronArray = []
        self.weights2ndNeuronArray = []
        self.weights1stNeuronArray= self.generateWeights(self.weights1stNeuronArray,'weights1stNeuron.txt')
        self.weights2ndNeuronArray= self.generateWeights(self.weights2ndNeuronArray,'weights2ndNeuron.txt')

    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))

    def __sigmoid_derivative(self, x):
        return x * (1 - x)

    def saveWeightsToTxt(self):
        self.weights1stNeuron = 2 * random.random((25, 5)) - 1
        weights1stNeuronArray = numpy.asarray(self.weights1stNeuron)
        numpy.savetxt("weights1stNeuron.txt",weights1stNeuronArray,delimiter=' ')

        self.weights2ndNeuron = 2 * random.random((12, 1)) - 1
        weights2ndNeuronArray = numpy.asarray(self.weights2ndNeuron)
        numpy.savetxt("weights2ndNeuron.txt",weights2ndNeuronArray,delimiter=' ')

    def generateWeights(self,weightsNeuronArray, txtfilename):
        weightsNeuronArray = genfromtxt(txtfilename,delimiter=' ')
        return weightsNeuronArray
if __name__ == "__main__":
    nn = MyNN()

    #weights1stNeuronArray = genfromtxt('weights1stNeuron.txt',delimiter=' ')
    #print(weights1stNeuronArray)
