# NeuralNetwork_XOR
Basic XOR Neural Network

![tabela_verdade](images/tabela_verdade.png)

Variable values Table

![entrys](images/entrys.png)

![output](images/output.png)

![layer0](images/layer0.png)

![layer1_w](images/layer1_w.png)

Sinapse 0 sum
Entry(4x2)x weight0(2x3)
Four records of two neurons each, to be multiplied by three weights each neuron, 
resulting in three neurons each record.

![layer1_w](images/soma.png)

Result (4x3)

![layer1_w](images/4x3.png)

Hidden Layer(4x3)
Pass the value of hidden layer neurons through the sigmoid activation function

![layer1_w](images/4x3_oculta.png)

Sum Synapse 1
Hidden Layer (4x3) x 1 weights (3x1)
Four three neurons for each record, to be multiplied by three weights, resulting in one neuron for each record.

![layer1_w](images/soma_1.png)

Resutl (4x1)

![layer1_w](images/res_4x1.png)

Output Layer
Pass the output layer neuron value through the sigmoid activation function

![layer1_w](images/saida.png)

Error
Error for each record = outputs - output layer

![layer1_w](images/erro.png)

Error result

![layer1_w](images/res_erros.png)

Absolute mean between the absolute values ​​of the errors.

Result
0.4988

Gradient
The derivate of the sigmoid is:

![layer1_w](images/derivada.png)

Neural Network scheme

![layer1_w](images/rede.png)