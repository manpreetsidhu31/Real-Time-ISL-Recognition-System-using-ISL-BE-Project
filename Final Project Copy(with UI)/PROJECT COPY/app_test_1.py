import tkinter as tk
import cv2
from PIL import Image, ImageTk

def open_camera():
    cap = cv2.VideoCapture(0)

    def update():
        ret, frame = cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            label.imgtk = imgtk
            label.configure(image=imgtk)
            label.after(10, update)

    update()

root = tk.Tk()
root.title("Camera Viewer")

button = tk.Button(root, text="Open Camera", command=open_camera)
button.pack()

label = tk.Label(root)
label.pack()

root.mainloop()



#import tkinter as tk

#root = tk.TK()


#root.mainloop()