from gc import freeze
from pyexpat import model
import tensorflow as tensorflow
import os
import joblib
import logging



def get_VGG_16_model(input_shape, model_path):
    models = tf.keras.applications.vgg_16.VGG16(
        input_shape = input_shape,
        weights = "imagnet"
        include_top=False
        )
    
    models.save(model_path)
    logging.info("VGG16 model save at {model_path}")
    return model

## freezing the weights

def prepare_model(model, CLASS, freeze_all, freeze_till, learning_rate):
    if freeze_all:
        for layer in model.layers:
            layer.trainable = False
    elif (freeze_till i(s not None) and (freeze_till >1):
        for layer in model.layers[:-freeze_till]:
            layer.trainable = False

## add our fully connected layers
flatten_in = tf.keras.layers.Flatten()(model.output)
prediction = tf.keras.layer.Dense(
unit=CLASSES,
activation="softmax"    
)(flatten_in)

full_model = tf.keras.models.Model(
    inputs = model.input,
    outputs = prediction

full_model.compile(

    optimizer = tf.keras.optimizers.SGD(learning_rate=learning_rate),
    loss = tf.keras.losses.CategoricalCrossentropy(),
    metrics = ["accuracy"])
    
logging.info(f"custom model has been compiled and getting ready to be trained")

return model
