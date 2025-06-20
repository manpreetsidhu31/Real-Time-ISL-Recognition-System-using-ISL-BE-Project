from keras.models import model_from_json
import cv2
import numpy as np
import pyttsx3
#engine = pyttsx3.init()
#engine.setProperty('rate', 150)

json_file = open("sign_all_final.json", "r")
model_json = json_file.read()
json_file.close()
model = model_from_json(model_json)
model.load_weights("sign_all_final.h5")

def extract_features(image):
    feature = np.array(image)
    feature = feature.reshape(1,128,128,1)
    return feature/255.0

# Function to reduce brightness of a grayscale image
'''def reduce_brightness_gray(image, factor=0.8):
    # Reduce pixel values by the given factor
    darkened_image = image * factor
    # Clip pixel values to ensure they remain in the valid range [0, 255]
    darkened_image = np.clip(darkened_image, 0, 255).astype(np.uint8)
    return darkened_image'''

cap = cv2.VideoCapture(0)
label = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
while True:
    _,frame = cap.read()
    cv2.rectangle(frame,(0,40),(400,400),(169, 81, 120),1)
    cropframe=frame[40:400,0:400]

    #gray_image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply Gaussian blur to reduce noise

    cropframe=cv2.cvtColor(cropframe,cv2.COLOR_BGR2GRAY)
    #cropframe = cv2.equalizeHist(cropframe)
    #darkened_gray_frame = reduce_brightness_gray(cropframe, factor=0.8)  # Adjust the factor as needed
    #cropframe=darkened_gray_frame
    blurred = cv2.GaussianBlur(cropframe, (5, 5), 0)
    # Perform thresholding
    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    cropframe = thresh
    cv2.imshow("segmeneted",cropframe)
    cropframe = cv2.resize(cropframe,(128,128))
    cropframe = extract_features(cropframe)
    pred = model.predict(cropframe)
    prediction_label = label[pred.argmax()]
    cv2.rectangle(frame, (0,0), (400, 40), (169, 81, 120), -1)
    if prediction_label == 'blank':
        cv2.putText(frame, " ", (10, 30),cv2.FONT_HERSHEY_SIMPLEX,1, (255,255,255),2,cv2.LINE_AA)
    else:
        accu = "{:.2f}".format(np.max(pred)*100)
        cv2.putText(frame, f'{prediction_label}  {accu}%', (10, 30),cv2.FONT_HERSHEY_SIMPLEX,1, (255,255,255),2,cv2.LINE_AA)
    #text = prediction_label
    #engine.say(text)
    #engine.runAndWait()
    cv2.imshow("output",frame)
    cv2.waitKey(27)
    
    
cap.release()
cv2.destroyAllWindows()