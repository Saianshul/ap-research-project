import cProfile
import keras
from keras.datasets import mnist

def tensorflow():
    # Load the MNIST dataset
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    # Preprocess the data
    x_train, x_test = x_train / 255.0, x_test / 255.0

    # Define the model architecture
    model = keras.models.Sequential([
        keras.layers.Flatten(input_shape=(28, 28)),
        keras.layers.Dense(128, activation='relu'),
        keras.layers.Dropout(0.2),
        keras.layers.Dense(10, activation='softmax')
    ])

    # Compile the model
    model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

    # Train the model
    model.fit(x_train, y_train, epochs=5)

    # Evaluate the model
    loss, accuracy = model.evaluate(x_test, y_test)
    print("Test accuracy:", accuracy)

cProfile.run('tensorflow()')