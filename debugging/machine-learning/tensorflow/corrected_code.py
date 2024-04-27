import tensorflow_datasets as tfds
import tensorflow as tf
import keras
from keras.layers import TextVectorization, Embedding, Bidirectional, LSTM, Dense

dataset, _ = tfds.load('imdb_reviews', with_info=True, as_supervised=True)
training_dataset, testing_dataset = dataset['train'], dataset['test']

training_dataset = training_dataset.shuffle(10000).batch(32).prefetch(tf.data.experimental.AUTOTUNE)
testing_dataset = testing_dataset.batch(32).prefetch(tf.data.experimental.AUTOTUNE)

vectorize_layer = TextVectorization(
    max_tokens=10000,
    output_mode='int',
    output_sequence_length=250
)
vectorize_layer.adapt(training_dataset.map(lambda text, label: text))

model = keras.Sequential([
    vectorize_layer,
    Embedding(input_dim=10000, output_dim=64, mask_zero=True),
    Bidirectional(LSTM(64)),
    Dense(1, activation='sigmoid')
])

model.compile(loss=keras.losses.BinaryCrossentropy(), optimizer='adam', metrics=['accuracy'])
model.fit(training_dataset, epochs=1, validation_data=testing_dataset)
loss, accuracy = model.evaluate(testing_dataset)

print('Loss: ', loss)
print('Accuracy: ', accuracy)
