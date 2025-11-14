from flask import Flask, request
import numpy as np
import tensorflow as tf
from PIL import Image
import io

app = Flask(__name__)
model = tf.keras.models.load_model('vgg16Variant.keras')

@app.route('/summary', methods=['GET'])
def model_info():
   return {
      "version": "vgg16Variant",
      "name": "Katrina_damage",
      "description": "Classify satellite images of buildings in the aftermath of a hurricane into 'damage' or 'no_damage' categories",
      "number_of_parameters": 16812353
   }
# def model_info():
#    return {
#       "version": "leNet5Variant",
#       "name": "Katrina_damage",
#       "description": "Classify satellite images of buildings in the aftermath of a hurricane into 'damage' or 'no_damage' categories",
#       "number_of_parameters": 2601153
#    }
    
@app.route('/inference', methods=['POST'])
def upload_file():

    # check if the post request has the file part
   if 'image' not in request.files:
      # if the user did not pass the image under `image`, we don't know what they are
      # don't, so return an error.
      return {"error": "Invalid request; pass a binary image file as a multi-part form under the image key."}, 404
   # get the data
   data = request.files['image']
   # do something with data...
   print(data) # apparently this is a FileStorage object?? 
    # Googled how to deal with it and got the following code to turn it into a numpy array
   image_bytes = data.read()
   image_stream = io.BytesIO(image_bytes)
    
   with Image.open(image_stream).convert("RGB") as pil_image:
       data = np.asarray(pil_image)

   print(data.shape) 
   data = data / np.max(data)
   data = data.reshape(1,128,128,3)
   prediction = model.predict(data)[0][0]
   if prediction < 0.5:
       return {"prediction": "damage"}
   else:
       return {"prediction": "no_damage"}

# start the development server
if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')