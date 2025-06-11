# Importing necessary functions
from keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.utils import array_to_img, img_to_array, load_img
import os

# Define the main directory containing subdirectories for each class
main_dir = "C:/Users/Sylvia/Documents/college stuff/sem 7/final year project stuff/SignLanguageDetectionUsingCNN-main/JU"

save_dir="augmented_JU"
# Initialize the ImageDataGenerator class with desired augmentation parameters
datagen = ImageDataGenerator(
    rotation_range=20,
    shear_range=0.1,
    zoom_range=0.1,
    horizontal_flip=True
)


# Specify the interval for data augmentation (e.g., every 100th image)
augmentation_interval = 5

# Counter variable to keep track of the number of images processed
image_count = 0

# Iterate over each class directory in the main directory
for class_name in os.listdir(main_dir):
    class_dir = os.path.join(main_dir, class_name)
    # Check if the item is a directory
    if os.path.isdir(class_dir):
        class_save_dir = os.path.join(save_dir, class_name)
        os.makedirs(class_save_dir, exist_ok=True)
        # Iterate over each image in the class directory
        for filename in os.listdir(class_dir):
            # Load the image
            img = load_img(os.path.join(class_dir, filename))
            
            # Convert the image to an array and reshape it
            x = img_to_array(img)
            x = x.reshape((1, ) + x.shape)
            
            if image_count % augmentation_interval == 0:
                # Generate and save augmented samples
                i = 0
                for batch in datagen.flow(x, batch_size=1, save_to_dir=class_save_dir, save_prefix='aug', save_format='jpg'):
                    i += 1
                    if i > 5:
                        break
            # Increment the image count
            image_count += 1





# Importing necessary functions
'''from keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.utils import array_to_img, img_to_array, load_img
import os
import cv2

root_dir = "C:/Users/Sylvia/Documents/college stuff/sem 7/final year project stuff/SignLanguageDetectionUsingCNN-main/PREPROCESSED IMAGES ALL COMBINED FINAL Copy"

# Path to the directory to save the segmented images
output_dir = "C:/Users/Sylvia/Documents/college stuff/sem 7/final year project stuff/SignLanguageDetectionUsingCNN-main/augmented_FINAL"


# Initialising the ImageDataGenerator class.
# We will pass in the augmentation parameters in the constructor.
datagen = ImageDataGenerator(
		rotation_range = 40,
		shear_range = 0.2,
		zoom_range = 0.2,
		horizontal_flip = True,
		brightness_range = (0.5, 1.5))


# Iterate through each folder in the root directory
for folder_name in os.listdir(root_dir):
    folder_path = os.path.join(root_dir, folder_name)
    if os.path.isdir(folder_path):
        # Create a subdirectory in the output directory for the current folder
        output_folder = os.path.join(output_dir, folder_name)
        os.makedirs(output_folder, exist_ok=True)

        for filename in os.listdir(folder_path):
            if filename.endswith('.jpg') or filename.endswith('.png'):
                # Load the image
                image_path = os.path.join(folder_path, filename)
                image = cv2.imread(image_path)

# Loading a sample image 
img = load_img('image.jpg') 
# Converting the input sample image to an array
x = img_to_array(img)
# Reshaping the input image
x = x.reshape((1, ) + x.shape) 

# Generating and saving 5 augmented samples 
# using the above defined parameters. 
i = 0
for batch in datagen.flow(x, batch_size = 1,
						save_to_dir ='preview', 
						save_prefix ='image', save_format ='jpeg'):
	i += 1
	if i > 5:
		break

'''