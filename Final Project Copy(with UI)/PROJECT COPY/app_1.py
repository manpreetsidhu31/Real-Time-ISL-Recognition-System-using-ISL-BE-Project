import tkinter as tk
from tkinter import font, filedialog
import cv2
import numpy as np
from keras.models import model_from_json
from PIL import ImageTk, Image
from keras.utils import to_categorical

# Global variable to store the recognized sign
recognized_sign = ""

# Create a label for displaying the recognized sign and accuracy
output_label = None

# Global variable to store the complete recognized string
whole_string = ""

# Load the trained model
json_file = open("sign_all_final.json", "r")
model_json = json_file.read()
json_file.close()
model = model_from_json(model_json)
model.load_weights("sign_all_final.h5")

def extract_features(image):
    feature = np.array(image)
    feature = feature.reshape(1, 128, 128, 1)
    return feature / 255.0

def store_sign(event):
    global recognized_sign, whole_string
    if event.keysym == "space":
        recognized_sign = output_label.cget("text")
        whole_string += recognized_sign[6]
        text_label.config(text=f"Text: {whole_string}")

def clear_text():
    global whole_string
    whole_string = ""
    text_label.config(text="Text: ")

def open_image():
    # Create a new window to display the image
    image_window = tk.Toplevel()
    image_window.title("Image Viewer")

    # Load the image "signs.png" and display it
    img = Image.open("signs.jpg")
    img.thumbnail((800, 600))
    img = ImageTk.PhotoImage(img)

    # Create a canvas to contain the image label and scrollbar
    canvas = tk.Canvas(image_window, width=img.width(), height=img.height())
    canvas.pack(expand=True, fill="both")

    # Create a label to display the image
    image_label = tk.Label(canvas, image=img)
    image_label.image = img  # Keep a reference to avoid garbage collection
    canvas.create_window(0, 0, anchor="nw", window=image_label)

    # Function to handle mouse wheel scrolling for zooming
    def scroll_image(event):
        nonlocal img
        if event.delta:
            scale = 1.1 if event.delta > 0 else 0.9
            img = img.resize((int(img.width() * scale), int(img.height() * scale)), Image.ANTIALIAS)
            img_tk = ImageTk.PhotoImage(img)
            canvas.itemconfig(image_label, image=img_tk)
            canvas.config(scrollregion=canvas.bbox("all"))

    canvas.bind("<MouseWheel>", scroll_image)

def run_sign_language_recognition_app():
    # Create the main window
    root = tk.Tk()
    root.title("Sign Language Recognition")

    # Set up app bar
    app_bar = tk.Frame(root, height=50, bg="grey")
    app_title_font = font.Font(family="Arial", size=16)
    app_title = tk.Label(app_bar, text="Indian Sign Language Recognition", fg="black", font=app_title_font)
    app_title.pack(side="top", anchor="center", padx=10, pady=10)
    app_bar.pack(fill="x", expand=False)

    # Set up camera frame
    camera_frame = tk.Frame(root, width=400, height=400)
    camera_frame.pack(expand=False, padx=20, pady=20)

    # Create a label for the camera feed
    camera_label = tk.Label(camera_frame)
    camera_label.pack()

    # Create a label for displaying the grayscale camera feed
    grayscale_label = tk.Label(root)
    grayscale_label.pack()

    label = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    # Create a label for displaying the recognized sign and accuracy
    global output_label
    output_label = tk.Label(root, text="", font=("Arial", 14))
    output_label.pack()

    # Create a label for displaying recognized text
    global text_label
    text_label = tk.Label(root, text="Text: ", font=("Arial", 14))
    text_label.pack(anchor="w")

    # Button to clear the text
    clear_button = tk.Button(root, text="Clear", command=clear_text)
    clear_button.pack(anchor="w")
	
    
    spacer_label = tk.Label(root, text="")  # Empty label for spacing
    spacer_label.pack(pady=500)  # Add 10 pixels of padding using the label

    # Button to open an image
    open_image_button = tk.Button(app_bar, text="Show Signs", command=open_image)
    open_image_button.pack(side="right", padx=10, pady=5)

    # Function to process camera feed and recognize sign
    def recognize_sign():
        _,frame = cap.read()
                
        cropframe = frame[40:400, 0:400]
        cropframe=cv2.cvtColor(cropframe,cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(cropframe, (5, 5), 0)
        _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        cropframe = thresh
        cv2.imshow("segmeneted",cropframe)
        cropframe = cv2.resize(cropframe, (128, 128))
        cropframe = extract_features(cropframe)
        
        pred = model.predict(cropframe)
        prediction_label = label[pred.argmax()]
        
        
        
        if prediction_label != 'blank':
            accu = "{:.2f}".format(np.max(pred) * 100)
            output_label.config(text=f"Sign: {prediction_label}\nAccuracy: {accu}%")

        # # Display the video feed
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        camera_label.imgtk = imgtk
        camera_label.configure(image=imgtk)

        camera_label.after(10, recognize_sign)
        
        

    # Start camera feed and sign recognition
    cap = cv2.VideoCapture(0)
    recognize_sign()

    # Bind spacebar key press event to store recognized sign
    root.bind("<KeyPress>", store_sign)

    # Run the GUI main loop
    root.mainloop()

    # Release the camera when the application is closed
    cap.release()

# Call the function to run the sign language recognition app
run_sign_language_recognition_app()
 	


#  def recognize_sign():
#         ret, frame = cap.read()
                
#         cropframe = frame[40:400, 0:400]
        
#         cropframe_gray = cv2.cvtColor(cropframe, cv2.COLOR_BGR2GRAY)
#         blurred = cv2.GaussianBlur(cropframe_gray, (5, 5), 0)
#         _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
#         cropframe = cv2.resize(thresh, (128, 128))
#         cropframe = extract_features(cropframe)
#         pred = model.predict(cropframe)
#         prediction_label = label[pred.argmax()]
#         if prediction_label != 'blank':
#             accu = "{:.2f}".format(np.max(pred) * 100)
#             output_label.config(text=f"Sign: {prediction_label}\nAccuracy: {accu}%")

#         # Display the video feed
#         cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         img = Image.fromarray(cv2image)
#         imgtk = ImageTk.PhotoImage(image=img)
#         camera_label.imgtk = imgtk
#         camera_label.configure(image=imgtk)

#         # Display the grayscale camera feed
#         cv2image_gray = cropframe_gray
#         img_gray = Image.fromarray(cv2image_gray)
#         imgtk_gray = ImageTk.PhotoImage(image=img_gray)
#         grayscale_label.imgtk = imgtk_gray
#         grayscale_label.configure(image=imgtk_gray)

#         camera_label.after(10, recognize_sign)

#     # Start camera feed and sign recognition
#     cap = cv2.VideoCapture(0)
#     recognize_sign()
