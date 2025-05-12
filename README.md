# Cartoonify Your Image 🎨

A fun Python application that allows you to turn your photos into cartoon-style images with the help of OpenCV and Python libraries. With just a click, you can upload your photo, apply various filters, and save your cartoonified masterpiece!

## 📸 Features:

* **Upload Image**: Choose an image from your computer and upload it to the app.
* **Cartoonify**: Transform the image into a cartoon using edge detection and bilateral filtering techniques.
* **Save**: Save your cartoonified image to your computer.
* **Interactive GUI**: A simple and user-friendly interface powered by Tkinter for image upload and save options.

## 🚀 Installation & Setup:

To run this project on your local machine, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/Cartoonify-Your-Image.git
   ```

2. **Install dependencies**:
   You will need Python 3.x and the following libraries:

   * OpenCV
   * EasyGUI
   * NumPy
   * ImageIO
   * Tkinter (comes pre-installed with Python)
   * Pillow
   * Matplotlib

   Install them using `pip`:

   ```bash
   pip install opencv-python easygui numpy imageio Pillow matplotlib
   ```

3. **Run the application**:
   Simply run the Python script to launch the GUI application:

   ```bash
   python cartoonify_image.py
   ```

4. **Upload and Cartoonify**:

   * Click "Cartoonify an Image" to upload your image.
   * After processing, the cartoonified image will be displayed, and you can save it.

## 🎨 How it Works:

* The script uses OpenCV to process the image. It converts the image into grayscale, applies a median blur, and detects edges to create a cartoonish effect. The bilateral filter keeps the image sharp while reducing noise.
* The cartoonified image is then displayed and saved in the same directory as the original image.

## 💾 Save Your Work:

Once your image is cartoonified, click "Save cartoon image" to save the final result.

---

### Short Description:

A Python app that allows users to upload an image, apply a cartoon effect, and save the transformed image using OpenCV and a simple Tkinter GUI.
