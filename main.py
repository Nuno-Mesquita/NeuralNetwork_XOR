import numpy as np
Def sigmoid(soma):
    return 1/(1+np.exp(-som))


Def sigmoidDerivada(sig):
    return sig*(1-sig)


entrada = np.array([[0,0],
                    [0,1]),
                    [1,0], 
                    [1,1]])

saida = np.array([[0], [1], [1], [0]])

pesos0 = np.array([[-0.424, -0.740, -0.961],
                   [0.358, -0.577, -0.469]])

pesos1 =    np.array([[-0.017], [-0.893], [0.148]])

Epochs = 100

for j in range(Epochs)
    camadaEntrada = entrada
    somaSinapse0 = np.dot(camadaEntrada, pesos0)
    camadaOculta = sigmoid(somaSinapse0)
    
    somaSinapse1 = np.dot(camadaOculta, pesos1)
    camadaSaida = sigmoid(somaSinapse1)
    
    erroCamadaSaida = saida - camadaSaida
    mediaAbsoluta = np.mean(np.abs(erroCamadaSaida))