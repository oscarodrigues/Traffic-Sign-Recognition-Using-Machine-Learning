from PIL import ImageTk, Image
import numpy as np
from keras.models import load_model

model = load_model('model_tested.h5')

classes = { 1:'Speed Limit (20km/h)',
            2:'Speed Limit (30km/h)',      
            3:'Speed Limit (50km/h)',       
            4:'Speed Limit (60km/h)',      
            5:'Speed Limit (70km/h)',    
            6:'Speed Limit (80km/h)',      
            7:'End of Speed Limit (80km/h)',     
            8:'Speed Limit (100km/h)',    
            9:'Speed Limit (120km/h)',     
            10:'No Passing',   
            11:'No Passing Vehicles Over 3.5 Tons',     
            12:'Right-of-Way at Intersection',     
            13:'Priority Road',    
            14:'Yield',     
            15:'Stop',       
            16:'No Vehicles',       
            17:'Vehicles Over 3.5 Tons are Prohibited',       
            18:'No Entry',       
            19:'General Caution',     
            20:'Dangerous Curve Left',      
            21:'Dangerous Curve Right',   
            22:'Double Curve',      
            23:'Bumpy Road',     
            24:'Slippery Road',       
            25:'Road Narrows on the Right',  
            26:'Road Work',    
            27:'Traffic Signals',      
            28:'Pedestrians',     
            29:'Children Crossing',     
            30:'Bicycles Crossing',       
            31:'Beware of Ice/Snow',
            32:'Wild Animals Crossing',      
            33:'End Speed + Passing Limits',      
            34:'Turn Right Ahead',     
            35:'Turn Left Ahead',       
            36:'Ahead Only',      
            37:'Go Straight or Right',      
            38:'Go Straight or Left',      
            39:'Keep Right',     
            40:'Keep Left',      
            41:'Roundabout Mandatory',     
            42:'End of No Passing',      
            43:'End of No Passing Vehicles Over 3.5 Tons' }

image = Image.open('E:/Documents/University of Windsor/Subjects/4th Year/2nd Semester/Sensor and Vision Systems/Labs and Projects/Project/Traffic Sign Classification/tsrd-test/00034.png')
image = image.resize((30,30))
image = np.expand_dims(image, axis=0)
image = np.array(image)
pred = model.predict_classes([image])[0]
sign = classes[pred+1]
print(sign)

image = Image.open('E:/Documents/University of Windsor/Subjects/4th Year/2nd Semester/Sensor and Vision Systems/Labs and Projects/Project/Traffic Sign Classification/tsrd-test/00350.png')
image = image.resize((30,30))
image = np.expand_dims(image, axis=0)
image = np.array(image)
pred = model.predict_classes([image])[0]
sign = classes[pred+1]
print(sign)

image = Image.open('E:/Documents/University of Windsor/Subjects/4th Year/2nd Semester/Sensor and Vision Systems/Labs and Projects/Project/Traffic Sign Classification/tsrd-test/00461.png')
image = image.resize((30,30))
image = np.expand_dims(image, axis=0)
image = np.array(image)
pred = model.predict_classes([image])[0]
sign = classes[pred+1]
print(sign)

image = Image.open('E:/Documents/University of Windsor/Subjects/4th Year/2nd Semester/Sensor and Vision Systems/Labs and Projects/Project/Traffic Sign Classification/tsrd-test/00522.png')
image = image.resize((30,30))
image = np.expand_dims(image, axis=0)
image = np.array(image)
pred = model.predict_classes([image])[0]
sign = classes[pred+1]
print(sign)

image = Image.open('E:/Documents/University of Windsor/Subjects/4th Year/2nd Semester/Sensor and Vision Systems/Labs and Projects/Project/Traffic Sign Classification/tsrd-test/00998.png')
image = image.resize((30,30))
image = np.expand_dims(image, axis=0)
image = np.array(image)
pred = model.predict_classes([image])[0]
sign = classes[pred+1]
print(sign)