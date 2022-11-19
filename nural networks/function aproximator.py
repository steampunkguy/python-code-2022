import math
import random

def randomlearn(awigths, abiases):
    for baises in abiases:
        for i in range(len(baises)):
            baises[i] = round(baises[i] + random.randrange(-100, 100, 1)/100, 2)
    for wights in awigths:
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
        for neuron in range(0,self.numberOfNeurons):
            biasN = self.bias[neuron]
            wightsN = self.wights[neuron]
            out = 0
            for conection in range(0, len(self.inputs)):
                out = wightsN[conection] * self.inputs[conection] + float(out)
            out += biasN
            output.append(out)

def runnetwork(wigths,input,biases):
    layer1 = neuronLayers(wigths[0],input,biases[0],3)
    output1 = []
    inputs1 = []
    layer1.nuronLayer(output1)
    sigmoid(output1, inputs1)
    layer2 = neuronLayers(wigths[1],inputs1,biases[1],3)
    output2 = []
    inputs2 = []
    layer2.nuronLayer(output2)
    sigmoid(output2, inputs2)
    layer3 = neuronLayers(wigths[2],inputs2,biases[2],3)
    output3 = []
    inputs3 = []
    layer3.nuronLayer(output3)
    sigmoid(output3, inputs3)
    layer4 = neuronLayers(wigths[3],inputs3,biases[3],1)
    output4 = []
    layer4.nuronLayer(output4)
    return(output4[0])

def correctness(input,output):
    if input[1] == 0:
        if output == 0:
            return(1)
        else:
            return(0)
    else:
        if output < 0:
            output = output*-1
        percent = output/input[1]
        round(percent,4)
        if percent > 1:
            x = percent-round(percent)
            if x < 0:
                x = x*-1
            return(x)
        else:
            return(percent)

"""

"""

allbiases = [[1,1,1],
             [1,1,1,1,1],
             [1,1,1],
             [1,0]]

allwigths = [[[1,1],[1,1],[1,1]],
             [[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1]],
             [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]],
             [[1,1,1]]]

newbiases = [[1,1,1],
             [1,1,1,1,1],
             [1,1,1],
             [1,0]]

newwigths = [[[1,1],[1,1],[1,1]],
             [[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1]],
             [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]],
             [[1,1,1]]]

inputs = []
for i in range(-10,11):
    inputs.append([i,i*i])

for i in range(10):
    outputs = []
    for i in inputs:
        output = (runnetwork(allwigths,i,allbiases))
        outputs.append(correctness(i,output))
    mean1 = sum(outputs)/len(outputs)
    outputs = []
    randomlearn(newwigths,newbiases)
    for i in inputs:
        output = (runnetwork(newwigths,i,newbiases))
        outputs.append(correctness(i,output))
    mean2 = sum(outputs)/len(outputs)
    print("mean1",mean1,"mean2",mean2)
    if (mean1 < mean2) != True :
        print("mean1")
        newbiases = allbiases 
        newwigths = allwigths
    elif (mean1 > mean2) != True :
        print("mean2")
        allbiases = newbiases
        allwigths = newwigths
print(allwigths,allbiases)
