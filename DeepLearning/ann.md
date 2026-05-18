# ANN = basic deep learning learning tool

ANN = Artificial Neural Network
ANN is the basic neural network architecture. It consists of:
Input Layer → Hidden Layers → Output Layer
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

1. mnist = tf.keras.datasets.mnist
   means Go inside TensorFlow → Keras → datasets → get the MNIST dataset helper, and store it in variable mnist.
   "Find the MNIST bookshelf"

2. (X_train, y_train), (X_test, y_test) = mnist.load_data()
   This line actually:
   downloads dataset (if needed)
   loads images into memory
   "Bring me the books"

3. (X_train, y_train), (X_test, y_test) = mnist.load_data()
   Looks similar because same ML concept.
   Inputs + labels.
   But dataset is already pre-split.
   MNIST returns:
   (
   (training_images, training_labels),
   (test_images, test_labels)
   )
   Which we rename: (X_train, y_train), (X_test, y_test)

4. model = tf.keras.models.Sequential([
   tf.keras.layers.Flatten(input_shape=(28, 28)),
   tf.keras.layers.Dense(128, activation="relu"),
   tf.keras.layers.Dense(10, activation="softmax")
   ])
   This is the heart of your first neural network.
   1. model = tf.keras.models.Sequential([
      We are creating a neural network model. Stored in model
      Sequential means: Layers stacked one after another. Data flows in sequence
      Why use Sequential?
      Because our network is simple. straight flow. No branching.
   2. tf.keras.layers.Flatten(input_shape=(28, 28))
      MNIST image Shape: (28, 28) => 28 rows × 28 columns 2D matrix.
      But ANN expects: 1D vector. So Flatten does: 28 × 28 → 784
      before
      [
      [1,2,3],
      [4,5,6]
      ]
      after flatten: [1,2,3,4,5,6]
   3. tf.keras.layers.Dense(128, activation="relu")
      Now real neural network starts.
      Dense = fully connected layer. Every neuron connected to every neuron in previous layer.
      Input: 784 neurons
      Dense layer: 128 neurons
      Each of those 128 neurons receives ALL 784 inputs.
      Activation: ReLU (Rectified Linear Unit)
      Why ReLU? Because it's fast and works well for hidden layers. Without activation network becomes boring linear math.
      With ReLU: learns complex patterns.
   4. tf.keras.layers.Dense(10, activation="softmax")
      Why 10?
      Digits: 0 1 2 3 4 5 6 7 8 9
      Need 10 output neurons. One neuron per class.
      Example output: [0.01, 0.03, 0.80, 0.01, ...] Meaning: Probability of each digit.
      Softmax-Converts raw scores into probabilities.
      Before: [2.1, 5.8, 1.2]
      After softmax: [0.03, 0.94, 0.03]
      All probabilities sum to: 1.0

Full architecture
28×28 image
↓
Flatten
↓
784 values
↓
Dense(128)
↓
ReLU
↓
Dense(10)
↓
Softmax probabilities

5. model.compile(
   optimizer="adam",
   loss="sparse_categorical_crossentropy",
   metrics=["accuracy"]
   )
   "Train this neural network using Adam optimizer, measure mistakes with sparse categorical crossentropy, and show accuracy while training."
   You built the brain (Sequential model).
   Now compile() tells the brain how to learn.
   Think:Building a student is not enough.
   You must also define:
   how they study
   how mistakes are measured
   how success is tracked
   1. compile() prepares the model for training.
      Before compile: brain exists
      After compile: brain knows learning rules
   2. optimizer="adam"
      When model predicts wrong… how should it improve? That’s optimizer’s job.
      Suppose actual digit: 5
      Model predicts: 2
      Wrong. Now what? The model has weights inside neurons. Optimizer decides: Change these weights so next prediction improves.
      Think: Optimizer = coach
      Why Adam? Adaptive Moment Estimation
      Adam is a smart optimizer. Adam:
      fast
      efficient
      commonly used
      great beginner default
   3. loss="sparse_categorical_crossentropy"
      Loss = how wrong the model is.
      Actual: 7 Prediction: 7 Loss: small
      Actual: 7 Prediction: 2 Loss: big
      Analogy:
      Teacher grading exam.
      Correct answer:small penalty
      Wrong answer:big penalty
      Why "categorical"? Because we are predicting categories/classes.
      Why "crossentropy"? Crossentropy is a mathematical way to measure prediction error for probabilities.
      Why "sparse"? Because labels are simple integers.
   4. metrics=["accuracy"]
      This tells model While training, show me performance.
      Example: 100 images
      Correct: 94 Accuracy: 94%
      Why metric if we already have loss?
      Because:
      Loss = internal mathematical learning signal
      Accuracy = human-friendly performance number

6. history = model.fit(X_train, y_train, epochs=5)
   "Train the model on training data for 5 epochs, and store training history in variable history."
   Think:
   built brain ✅
   defined learning rules ✅
   now actual teaching starts ✅
   1. model.fit() is where the magic happens.
      This is the training loop.
      During fit():
      Model looks at training data
      Makes predictions
      Compares predictions to actual labels
      Calculates loss
      Uses optimizer to adjust weights
      Repeats for all training samples
   2. epochs=5 means we will go through the entire training dataset 5 times. (like revision)
      Why multiple epochs?
      Because one pass might not be enough for the model to learn well.
      Each epoch allows the model to refine its understanding of the data.

7. test_loss, test_accuracy = model.evaluate(X_test, y_test)
   “Take completely unseen images and test how well the model performs.”
   "Evaluate the model on test data, and store loss and accuracy in test_loss and test_accuracy."
   After training, we want to see how well our model performs on new, unseen data. 1. model.evaluate() runs the model on test data and calculates loss and accuracy.
   This gives us an unbiased estimate of how well our model generalizes to new data.
   Example: If test_accuracy is 0.98, it means our model correctly predicts 98% of the test images.

8. predictions = model.predict(X_test)
   “Take the test images and tell me what you think each one is.”
   After evaluating the model, we can use it to make predictions on new data.
   model.predict() takes input data and outputs predicted probabilities for each class.
   Example output: [[0.01, 0.03, 0.90, ...], [0.05, 0.80, 0.10, ...], ...]
   Each inner list corresponds to the predicted probabilities for each class for a given test image.

Image of handwritten 7
↓
Flatten layer
28×28 → 784 numbers
↓
Dense hidden layer
pattern detection
↓
ReLU activation
↓
Output layer (10 neurons)
↓
Softmax probabilities
↓
Highest probability chosen
↓
Prediction = 7
