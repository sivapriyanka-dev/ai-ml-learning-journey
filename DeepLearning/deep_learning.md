# What is Deep Learning?

Deep learning is a subset of machine learning that uses neural networks with multiple layers (hence "deep") to learn from data. It is inspired by the structure and function of the human brain, specifically the interconnected neurons.

ML: You manually engineer features.
Deep Learning: Model learns features automatically.
Example image: Instead of telling:
ears
whiskers
fur
tail
Neural network figures those patterns out itself.

# Neural Network intuition

Think of a neuron like a tiny decision maker.
Example:
Student marks prediction:
Inputs:
math = 90
science = 80
attendance = 95

Weights:
importance of each input.

# Core terms

- **Weights**: The importance of each input.
- **Bias**: A value added to the weighted sum of inputs to shift the activation function.
- **Activation Function**: A function that determines whether a neuron should be activated or not based on the weighted sum of inputs and bias.
- **Loss Function**: A function that measures how well the model's predictions match the actual labels.
- **Optimizer**: An algorithm that adjusts the weights and biases to minimize the loss function.
- **neuron**: Tiny math unit. (weight × input) + bias Then activation: output = activation(sum)

-> Activation Functions:

1. ReLU: Most common.
   f(x) = max(0, x)
   Examples:
   -3 → 0
   5 → 5
   Why:
   fast + works well.

2. Sigmoid
   0 to 1
   Used for binary classification.
   Example:
   cat vs dog:
   probability of dog.

3. Softmax
   For multiclass classification.
   Example:
   digits:
   [0.01, 0.03, 0.90, 0.02...]
   Highest wins.

-> Layers:
Simple network: Input → Hidden → Output
Example: MNIST: 28×28 image
Flatten: 784 inputs
Architecture: 784 → 128 → 64 → 10
Meaning:
784 input neurons
hidden layer 128
hidden layer 64
output 10 digits

# Training a Neural Network

Neural network learns by repetition.

1. **Forward Pass**: The input data is passed through the network to generate predictions. image → model → guess
2. **Calculate Loss**: The loss function computes the difference between the predicted output and the actual labels.
3. **Backward Pass**: The optimizer uses the loss to adjust the weights and biases in the network to improve future predictions.

Backpropagation: Send error backward. Adjust weights.
Gradient descent: Optimization algorithm. Tiny steps toward lower error.

# Types of Neural Networks

- **Feedforward Neural Networks**: The simplest type of neural network where connections between the nodes do not form a cycle.
- **Convolutional Neural Networks (CNNs)**: Primarily used for image and video recognition tasks.
- **Recurrent Neural Networks (RNNs)**: Designed for sequential data like time series or natural language processing.
- **Transformer Networks**: Used for tasks involving sequential data, such as language translation and text generation, and have become the state-of-the-art in many NLP tasks.

# Applications of Deep Learning

- Image and speech recognition
- Natural language processing

# Epoch / Batch size

- **Epoch**: One complete pass through the entire training dataset. Eg: 60,000 images processed once.
- **Batch Size**: The number of samples processed before the model's internal parameters are updated. Smaller batch sizes can lead to more noisy updates, while larger batch sizes can lead to more stable updates but require more memory.
  Small chunks.
  Example: batch=32 -> Process 32 images at a time.
  Why: memory efficient.

# Why MNIST?

- Simple and well-known dataset.
  Because this teaches the entire deep learning workflow: images → preprocessing → training → prediction → evaluation

# ANN = Artificial Neural Network

It’s the basic neural network architecture. Input Layer → Hidden Layers → Output Layer
ANN works with tabular / vector data. It treats input as plain numbers. Many neurons together = ANN.
Eg: [25, 50000, 3, 1] means
age
salary
experience
owns house
ANN learns relationships between these values.
Examples:
Customer churn prediction - Output: will churn / won't churn
House price prediction - Output: price
Credit risk - Output: approve/reject

ANN sees: just numbers.
It does NOT know:
neighboring pixels
shapes
edges
spatial structure
So ANN is bad for image understanding.

ANN treats image as just a list of numbers So spatial relationships are lost.
Example:
neighboring pixels relationship disappears.
That’s why CNN exists. CNN preserves image structure.
Which is why: Cats vs Dogs → CNN, not ANN

ANN = basic deep learning learning tool
CNN = actual computer vision model

# CNN = Convolutional Neural Network

CNN is designed for image data. It preserves spatial relationships between pixels.
Special neural network built for images. Instead of flattening immediately, CNN scans image.
Imagine image: Cat image
CNN looks at small windows: 3×3 like
[0 1 1
1 0 0
1 1 0]
Moves across image. This is convolution.

What CNN learns
Early layers:
edges
corners
textures

Middle layers:
eyes
whiskers
ears

Deep layers:
cat face
dog face

So CNN understands image hierarchy.
CNN structure
Input → Convolutional Layers → Pooling Layers → Fully Connected Layers → Output
Convolutional Layers: Extract features using filters.
Pooling Layers: Reduce spatial dimensions (e.g., max pooling).
Fully Connected Layers: Traditional ANN layers for final classification.

CNN is used

- Image classification
  Cat vs Dog
  Input: image
  Output: cat/dog Object detection
- Face recognition - Phone unlock
- Medical imaging - X-ray classification
- OCR - Reading handwritten text
- Self-driving cars
- Security cameras - Object detection

# RNN = Recurrent Neural Network

RNN is designed for sequential data. It has memory to capture information from previous time steps.
Example: Sentiment analysis
Input: "I love this movie!"
RNN processes word by word:
"I" → hidden state 1
"love" → hidden state 2 (remembers "I")
"this" → hidden state 3 (remembers "I love")
"movie!" → hidden state 4 (remembers "I love this")
Output: Positive sentiment
RNN structure
Input → RNN Layers → Output
RNN Layers: Capture sequential dependencies using hidden states.
Challenges with RNNs:
Vanishing gradients: Difficulty learning long-term dependencies.
Solution: LSTM (Long Short-Term Memory) and GRU (Gated Recurrent Unit) architectures.

# Transformer Networks

Transformers are designed for sequential data, but they use self-attention mechanisms to capture relationships between all elements in the sequence simultaneously.
Example: Machine translation
Input: "Hello, how are you?"
Transformer processes the entire sentence at once:
"Hello," "how," "are," "you?"
Output: "Hola, ¿cómo estás?"
Transformer structure
Input → Transformer Layers → Output
Transformer Layers: Use self-attention to capture relationships between all input elements.
Advantages of Transformers:
Parallel processing: Can process entire sequences at once, leading to faster training.
Better long-range dependencies: Can capture relationships between distant elements in the sequence.

Use:
ANN → learning basics + tabular problems
CNN → computer vision
RNN/LSTM → sequence data
Transformers → LLMs / modern NLP

For Cats vs Dogs: CNN
For customer churn: ANN
For ChatGPT: Transformer
