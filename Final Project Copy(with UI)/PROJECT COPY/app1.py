import tkinter as tk
from tkinter import font, filedialog
import cv2
import numpy as np
from keras.models import model_from_json
from PIL import ImageTk, Image
from keras.utils import to_categorical
#import customtkinter
#from tkinter import *
#import pyttsx3
from gtts import gTTS
#import os
import pygame
from io import BytesIO


cap = None

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




whole_string = ""

def store_sign(event):
    global recognized_sign, whole_string
    if event.keysym == "1":
        recognized_sign = output_label.cget("text")
        whole_string += recognized_sign[6]
        text_label.config(text=f"Text: {whole_string}")
    elif event.keysym == "space":
        whole_string += " "  # Add a space if the space bar is pressed
    elif event.keysym == "BackSpace":  # Check if the pressed key is BackSpace
        backspace(event)  # Call the backspace function
    # Add more conditions for other key bindings if needed
    
def convert_to_speech():
    # Get the text from the label
    #text = text_label.cget("text")

    # Initialize the text-to-speech engine
    #engine = pyttsx3.init()

    # Convert the text to speech
    #engine.say(whole_string)

    # Wait for the speech to finish
    #engine.runAndWait()
    #Convert text to speech
    #tts = gTTS(text=whole_string, lang='en')
    # Convert text to speech
    tts = gTTS(text=whole_string, lang='en')

    # Create an in-memory stream to store the speech
    speech_stream = BytesIO()
    tts.write_to_fp(speech_stream)
    speech_stream.seek(0)

    # Initialize pygame mixer
    pygame.mixer.init()
    
    # Load the speech from the in-memory stream
    pygame.mixer.music.load(speech_stream)
    
    # Play the speech
    pygame.mixer.music.play()

    # Save the speech to a file
    #tts.save("output.mp3")

    # Play the speech using the default media player
    #os.system("start output.mp3")

def backspace(event):
        global whole_string
        # Get the current text in the label
        current_text = text_label.cget("text")
        if current_text.startswith("Text: "):
        # Get the text after "Text: "
            text_after_prefix = current_text[len("Text: "):]
            # Check if there's anything to delete
            if text_after_prefix:
                # Remove the last character
                new_text = text_after_prefix[:-1]
                whole_string = new_text  # Update whole_string
                # Update the text label
                text_label.config(text=f"Text: {new_text}")
        '''if current_text.startswith("Text: "):
            current_text = current_text[6:]  # Remove "Text: " prefix
    # Remove the last character
        # Remove the last character
        new_text = current_text[:-1]
        whole_string = new_text  # Update whole_string
        # Update the text label
        text_label.config(text=new_text)'''

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
    #canvas.grid(row=0, column=0, sticky="nsew")


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
    root.configure(bg="#F9F7F7")
    root.eval("tk::PlaceWindow . center")
    root.geometry("600x600")

    #scrollbar = Scrollbar(root)
    #scrollbar.pack( side = RIGHT, fill=Y ) 

    #scroll_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Georgia", 12), bg="#DBE2EF")
    #scroll_text.pack(fill=tk.BOTH, expand=True)

    # Set up app bar
    app_bar = tk.Frame(root, height=300, width=400, bg="#DBE2EF")
    app_title_font = font.Font(family="Georgia", size=16)
    app_title = tk.Label(app_bar, text="Indian Sign Language Recognition", fg="#112D4E", font=app_title_font, bg="#DBE2EF")
    app_title.pack(side="top", anchor="center", padx=10, pady=10)
    app_bar.pack(fill="x", expand=False)
    #app_title.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
    #app_bar.grid(row=2, column=0, sticky="ew")
    


    # Set up camera frame
    camera_frame = tk.Frame(root, width=400, height=300)
    #camera_frame.pack(expand=False, padx=20, pady=20)
    #camera_frame.grid(row=3, column=0, padx=20, pady=20)


    # Create a label for the camera feed
    camera_label = tk.Label(camera_frame)
    camera_label.pack()
    #camera_label.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)

    # Create a label for displaying the grayscale camera feed
    #grayscale_label = tk.Label(root)
    #grayscale_label.pack(side=tk.LEFT, padx=10, pady=10)
    #grayscale_label.grid(row=5, column=0, sticky=tk.W, padx=10, pady=10)


    label = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    # Create a label for displaying the recognized sign and accuracy
    #global output_label
    #output_label = tk.Label(root, text="", font=("Georgia", 14))
    #output_label.pack()
    #output_label.grid(row=6, column=0)





    def open_camera():
        global cap

        if cap is None or not cap.isOpened():

            cap = cv2.VideoCapture(0)

            if cap.isOpened():
                def recognize_sign():
                    _,frame = cap.read()
                            
                    cropframe = frame[40:400, 0:400]
                    cropframe=cv2.cvtColor(cropframe,cv2.COLOR_BGR2GRAY)
                    blurred = cv2.GaussianBlur(cropframe, (5, 5), 0)
                    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
                    cropframe = thresh

                    cropframe_button = tk.Button(root, text="See Segmented Frame", font=("Georgia", 14), fg="#DBE2EF", command=cv2.imshow("Segmented Frame",cropframe), bg="#3F72AF")
                    cropframe_button.pack(anchor="w")
                    #cropframe_button.grid(row=7, column=0, sticky="w")

                    
                    cropframe = cv2.resize(cropframe, (128, 128))
                    cropframe = extract_features(cropframe)
                    
                    pred = model.predict(cropframe)
                    prediction_label = label[pred.argmax()]
                    
                    cv2.rectangle(frame, (0,0), (400, 40), (169, 81, 120), -1)
                    
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

                    button.config(text="Close Camera")
                    button.config(command=close_camera)
                    print("Camera opened")

            
            '''def recognize_sign():
                _,frame = cap.read()
                        
                cropframe = frame[40:400, 0:400]
                cropframe=cv2.cvtColor(cropframe,cv2.COLOR_BGR2GRAY)
                blurred = cv2.GaussianBlur(cropframe, (5, 5), 0)
                _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
                cropframe = thresh

                cropframe_button = tk.Button(root, text="See Segmented Frame", font=("Georgia", 14), fg="#DBE2EF", command=cv2.imshow("Segmented Frame",cropframe), bg="#3F72AF")
                cropframe_button.pack(anchor="w")
                #cropframe_button.grid(row=7, column=0, sticky="w")

                
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

                camera_label.after(10, recognize_sign)'''

            recognize_sign()

    def close_camera():
        global cap
        # Check if the camera is open
        if cap is not None and cap.isOpened():
            # If open, release the camera
            cap.release()
            # Change button text and command back to open_camera
            button.config(text="Open Camera")
            button.config(command=open_camera)
            print("Camera closed")
            clear_camera_feed()
            cv2.destroyAllWindows()
        else:
            print("Camera is not open")

    def clear_camera_feed():
    # Display a blank image in the camera frame
        blank_image = Image.new("RGB", (640, 480), "white")
        blank_imgtk = ImageTk.PhotoImage(image=blank_image)
        camera_label.imgtk = blank_imgtk
        camera_label.configure(image=blank_imgtk)
    # Initialize the camera variable
    cap = None

    def open_window():
        # Create a new window
        window = tk.Toplevel(root)
        window.title("Instructions")
        window.configure(bg="#DBE2EF")

        # Add a label with some text to the new window
        label = tk.Label(window, text="These are the instructions for this system.\n1. Press 1 to display the predicted letters on the screen.\n2. Press Space to add space when creating your sentence.\n3. Press Backspace to delete anything you want!\n4. Open and Close Camera will start and stop your camera feed respectively.\nA segmented frame is provided so you can make sure the background \nis black and your hand is white!", font=("Georgia", 14), fg="#112D4E", bg="#DBE2EF")
        label.pack(fill=tk.BOTH, expand=True)

    button1 = tk.Button(root, text="Read Instructions!", command=open_window, font=("Georgia", 14), fg="#DBE2EF", bg="#3F72AF")
    button1.pack(anchor="ne")
    # Button to open an image
    open_image_button = tk.Button(app_bar, text="Show Signs",font=("Georgia", 14), fg="#DBE2EF", command=open_image, bg="#3F72AF")
    open_image_button.pack(side=tk.RIGHT, padx=10, pady=5)
    #open_image_button.grid(row=8, column=1, padx=10, pady=5)

    text_frame = tk.Frame(root)
    text_frame.pack(side=tk.TOP, padx=10, pady=10)

    # Create a label for displaying recognized text
    global text_label
    text_label = tk.Label(text_frame, text="Text: ", font = ("Georgia", 14), fg="#112D4E", bg="#DBE2EF")
    text_label.pack(side=tk.TOP, padx=6)
    text_label.pack(anchor="nw")
    #text_label.grid(row=9, column=1, padx=(0, 10))


    '''def backspace(event):
        # Get the current text in the label
        current_text = text_label.cget("text")
        # Remove the last character
        new_text = current_text[:-1]
        # Update the text label
        text_label.config(text=new_text)'''


    # Button to clear the text
    clear_button = tk.Button(text_frame, text="Clear", font=("Georgia", 14), fg="#DBE2EF", command=clear_text, bg="#3F72AF")
    clear_button.pack(side=tk.TOP, padx=10)
    clear_button.pack(anchor="nw")
    #clear_button.grid(row=10, column=0, padx=10, pady=10, sticky=tk.W)

    # Create a button to convert text to speech
    speech_button = tk.Button(root, text="Convert to Speech", command=convert_to_speech,font=("Georgia", 14), fg="#DBE2EF",bg="#3F72AF")
    speech_button.pack()


    button = tk.Button(root, text="Open Camera", command=open_camera, bg="#112D4E", fg="#DBE2EF", font=("Georgia",14))
    button.pack(side=tk.TOP, padx=10, pady=5)
    #button.grid(row=9, column=0, padx=10, pady=5, sticky=tk.W)
    # Function to process camera feed and recognize sign
    
    global output_label
    output_label = tk.Label(root, text="", font=("Georgia", 14))
    output_label.pack()

    camera_frame.pack(expand=False, padx=20, pady=20)

    # Start camera feed and sign recognition
    

    # Bind spacebar key press event to store recognized sign
    root.bind("<KeyPress>", lambda event: store_sign(event))

    # Run the GUI main loop
    root.mainloop()

    # Release the camera when the application is closed
    #cap.release()
    

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
