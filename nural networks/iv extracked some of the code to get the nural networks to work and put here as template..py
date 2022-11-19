import math
import random

def randomlearn(allwigths, allbiases):
    for baises in allbiases:
        for i in range(len(baises)):
            baises[i] = round(baises[i] + random.randrange(-100, 100, 1)/100, 2)
    for wights in allwigths:
        for wightset in wights:
            for i in range(len(wightset)):
                wightset[i] = round(wightset[i] + random.randrange(-100, 100, 1)/100, 2)
    
def sigmoid(inputs, output):
    for i in inputs:
        x = 1.0/(1.0 + pow(math.e, -float(i)))     
        output.append(x)

class neuronLayers:
    def __init__(self, wights, inputs, bias, numberOfNeurons):
        self.inputs = inputs
        self.wights = wights
        self.bias = bias
        self.numberOfNeurons = numberOfNeurons

    def nuronLayer(self, output):
        for neuron in range(0, self.numberOfNeurons):
            biasN = self.bias[neuron]
            wightsN = self.wights[neuron]
            out = 0
            for conection in range(0, len(self.inputs)):
                out = wightsN[conection] * self.inputs[conection] + float(out)
            out += biasN
            output.append(out)
            
allbiases = [[1,1],
             [1,1]]

allwigths = [[[1,1],
              [1,1]],
             [[1,1],
              [1,1]]]

randomlearn(allwigths, allbiases)

print(allwigths, allbiases)