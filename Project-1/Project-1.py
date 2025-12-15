import numpy as np
import cv2
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog, messagebox

root = tk.Tk()
root.title("Project")
root.geometry("500x600")

tk.Label(root, text="Image Processing Project", font=("Times New Roman", 16, "bold")).pack(pady=20)

label = tk.Label(root)
label.pack()

cv_image = None
photo = None
processed_image = None

def Input_image():
    global photo, cv_image, processed_image
    try:
        file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
        )
        if file_path:
            cv_image = cv2.imread(file_path)
            con_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
            display_image = cv2.resize(con_image, (320, 350))
            
            img = Image.fromarray(display_image)
            photo = ImageTk.PhotoImage(img)
            label.config(image=photo)
            label.image = photo
            
    except Exception as e:
        print("Error:", e)

def Contrust_adjustment():
    global photo, cv_image, processed_image
    
    if cv_image is not None:
        
        cl = 1
        gs = (5,5)
        img_clahe = cv2.createCLAHE(cl, gs)
        gray_image = cv2.cvtColor(cv_image,cv2.COLOR_RGB2GRAY)
        clahe_img = img_clahe.apply(gray_image)

        processed_image = cv2.resize(clahe_img, (320, 350))
            
        img = Image.fromarray(processed_image)
        photo = ImageTk.PhotoImage(img)
        label.config(image=photo)
        label.image = photo
    else:
        messagebox.showwarning("Warning", "Select Image first !!!")

def Brightness():
    global photo, cv_image, processed_image
    
    if cv_image is not None:

        gamma = 1.5
        inverse = 1/gamma
        
        table = np.array([((i / 255.0) ** inverse) * 255 for i in np.arange(0, 256)]).astype("uint8")
        B_image = cv2.LUT(cv_image, table)

        processed_image = cv2.resize(B_image, (320, 350))
        img = Image.fromarray(cv2.cvtColor(processed_image, cv2.COLOR_BGR2RGB))
        photo = ImageTk.PhotoImage(img)
        label.config(image=photo)
        label.image = photo
    else:
        messagebox.showwarning("Warning", "Select Image first !!!")

def Save_image():
    if processed_image is not None:
        file_path = filedialog.asksaveasfilename(
            defaultextension=".jpg",
            filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png")]
        )
        if file_path:
            cv2.imwrite(file_path, processed_image)
            messagebox.showinfo("Saved", "Image saved successfully!")
    else:
        messagebox.showwarning("Warning", "No image is processed!")


tk.Button(root, text='Input Image', command=Input_image).pack(pady=10)
tk.Button(root, text='Brightness', command=Brightness).pack(pady=5) 
tk.Button(root, text='Contrast Adjustment', command=Contrust_adjustment).pack(pady=5)
tk.Button(root, text='Save Image', command=Save_image).pack(pady=5)


root.mainloop()
