from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import messagebox

# Create the main window
root = Tk()
root.title("Image Uploader")
root.geometry("800x600")  # Set window size
root.configure(bg="lightblue") 

def validate_input(event=None):
    # Get the input value
    input_value = input_field.get()
    
    try:
        # Try converting the input to an integer
        value = int(input_value)
        
        # Check if the value is between 10 and 255
        if 10 <= value <= 255:
            messagebox.showinfo("Valid Input", f"Valid input: {value}")
        else:
            # If the value is not in the correct range, show an error message
            messagebox.showerror("Invalid Input", "Please enter a number between 10 and 255.")
    except ValueError:
        # If the input is not a valid number, show an error message
        messagebox.showerror("Invalid Input", "Please enter a valid number between 10 and 255.")


def show_input_field():
    if threshold_value.get() == "threshold_with_value":
        input_label.pack(padx=3,side="left")
        input_field.pack(pady=3,side="left")  # Show the input field when "Threshold with value" is selected
        # Bind Enter key to validate the input when pressed
        input_field.bind("<Return>", validate_input)
    else:
        input_field.pack_forget()  # Hide the input field for other options
        input_label.pack_forget()  # Hide the input field for other options
        
        
# Function to upload and display an image
def upload_image():
    # Open a file dialog to select an image
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *.gif")]
    )
    if file_path:
        # Open the image and resize it to fit the window
        img = Image.open(file_path)
        img = img.resize((800, 300), Image.Resampling.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)
        
        # Update the label to display the selected image
        image_label.config(image=img_tk, text="")  # Remove text and show the image
        image_label.image = img_tk  # Save a reference to avoid garbage collection


# Label to display the image
image_label = Label(root, text="Your image will appear here", font=("Arial", 14), bg="lightblue")
image_label.pack(expand=True, fill="both")


# Create a frame to hold the buttons
button_frame = Frame(root)
button_frame.pack(fill="x", side="bottom")  # Make the frame expandable

# Configure rows and columns to be responsive
for i in range(5):  # Assuming a 5x5 grid
    button_frame.grid_rowconfigure(i, weight=1, minsize=10)  # Make each row expandable
    button_frame.grid_columnconfigure(i, weight=1,  minsize=10)  # Make each column expandable

# Add 25 buttons using a loop
for i in range(25):
    # Create a button
    button = Button(button_frame, text=f"Button {i + 1}", bg="lightblue",relief="flat",width=5, height=1)
    # Place the button in a grid (5x5 layout)
    button.grid(row=i // 5, column=i % 5, padx=5, pady=5, sticky="nsew") 

# Create a frame to hold the radio buttons
radio_frame = Frame(root)
radio_frame.pack(side="bottom", fill="x" ,pady=5)  # Place the frame at the bottom

# Variable to hold the selected threshold option
threshold_value = StringVar(value="no_threshold")  # Default option is "no_threshold"

# Create the radio buttons
radio1 = Radiobutton(radio_frame, text="No Threshold", variable=threshold_value, value="no_threshold", command=show_input_field)
radio2 = Radiobutton(radio_frame, text="Default Threshold", variable=threshold_value, value="default_threshold", command=show_input_field)
radio3 = Radiobutton(radio_frame, text="Threshold with value", variable=threshold_value, value="threshold_with_value", command=show_input_field)


# Pack the radio buttons into the frame side by side
radio1.pack(padx=5,side="left")
radio2.pack(padx=5,side="left")
radio3.pack(padx=5,side="left")

# Create the label for the input field (hidden by default)
input_label = Label(radio_frame, text="Enter a valid threshold number:")
input_label.pack(side="left", padx=5)
input_label.pack_forget()  # Hide the label initially

# Create the input field for threshold value (hidden by default)
input_field = Entry(radio_frame)
input_field.pack(side="left", padx=5)
input_field.pack_forget()  # Hide the input field initially

# Button to trigger the upload function
upload_button = Button(root, text="Upload Image", command=upload_image, font=("Arial", 12))
upload_button.pack(pady=5 , side="bottom")

# Run the application
root.mainloop()


