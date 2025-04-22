#imported libs for all considered models
import os
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import random
from memory_profiler import profile
from memory_profiler import memory_usage
import joblib
from sklearn.preprocessing import StandardScaler
from skimage import io, color, feature
from skimage.transform import resize

# Load the trained model
model = tf.keras.models.load_model("models/cnn_image_classification_model.h5")


def preprocess_image(image_path):
    img = image.load_img(image_path, target_size=(150, 150))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img /= 255.0
    return img

#kNN, logistic
#def preprocess_image(image_path):
#    image = io.imread(image_path)
#    if len(image.shape) == 3 and image.shape[-1] == 4:
#        image = image[:, :, :3]
#    img = resize(image, output_shape=(227,227))
#    img = (img - np.min(img)) / (np.max(img) - np.min(img)) * 255
#    img_gray = color.rgb2gray(img)
#    hog_features = feature.hog(img_gray, block_norm='L2-Hys', pixels_per_cell=(16, 16))
#    img = hog_features.reshape(1, -1)
#    return img


@profile
def calling_decorators(image_path):
    img = preprocess_image(image_path)
    prediction =  model.predict(img)
    return prediction

def predict_single_image(image_path):
    prediction = calling_decorators(image_path)
    if prediction[0][0] > 0.5:
        return "Positive"
    else:
        return "Negative"

def main(input_path):
    if os.path.isfile(input_path):
        print("Input should be a directory containing images.")
        return
        
    elif os.path.isdir(input_path):
        num_iterations = 1
        batch_size = 100
        all_predictions = []
        
        for _ in range(num_iterations):
            batch_predictions = []
            files = os.listdir(input_path)
            random.shuffle(files)
            for i, filename in enumerate(files):
                if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
                    image_path = os.path.join(input_path, filename)
                    predicted_class = predict_single_image(image_path)
                    batch_predictions.append((filename, predicted_class))
                    if (i + 1) % batch_size == 0:
                        break
            all_predictions.append(batch_predictions)
            print("--------------------------------------")
        
    else:
        print("Invalid input path.")

input_path = os.path.join(os.getcwd(), 'Images100')  # for test data
main(input_path)
