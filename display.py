import tkinter as tk
import cv2
from PIL import Image, ImageTk

# Define width and height
width, height = 800, 600

# Initialize video capture
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

# Create Tkinter window
root = tk.Tk()
root.bind('<Escape>', lambda e: root.quit())

# Create label to display video feed
lmain = tk.Label(root)
lmain.pack()

# Function to update video feed
def show_frame():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)

# Start updating video feed
show_frame()
root.mainloop()

# Release video capture
cap.release()
