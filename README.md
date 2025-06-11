# Real-Time-ISL-Recognition-System-using-ISL-BE-Project

Our dataset:- https://drive.google.com/drive/folders/1v3csyNcM7FyCsy6oaD9tLnYoPwD_57vi?usp=drive_link

This is a Final Year BE Project in Machine Learning titled "Real Time Indian Sign Language Recognition using Convolutional Neural Network". We created our own dataset of 40,000 images for our project. Created a ISL prediciton and recognition system using a 4 layer CNN Model that I engineered myself. The dataset for all 26 letters A-Z was captured by me and my team and was preprocesses by us before being fed into the network. Here is our model specifics:- Our CNN consists fof 4 layers, 4 convolutional layers and 3 dense layers. the layers went from 32, 64, 128, 256 filters respectively. This model for us yielded the best results and accuracies for all letters. We made use of Adam Optimizer. Real time prediction was done using tkinter package.

![image](https://github.com/user-attachments/assets/999d9ba0-85c3-4a43-af8f-5cd51ccac68c)


Here are the accuracies for all letters:

![Screenshot 2025-06-11 104121](https://github.com/user-attachments/assets/321e462b-a53a-4640-bbcd-3df119c05cae)
![Screenshot 2025-06-11 104134](https://github.com/user-attachments/assets/5e7abddf-bddc-43e0-8d6e-54b55aee10a1)
![Screenshot 2025-06-11 104144](https://github.com/user-attachments/assets/f4478a09-91ca-4922-87eb-adbd11f49d1a)
![Screenshot 2025-06-11 104210](https://github.com/user-attachments/assets/f518c402-d4e3-4a96-8e9a-a0ccf2a2072f)


Further, i added screenshots for our UI for this project. After the letters our predicted, you press a button to display the letter and hence create a word. Accuracies are shown as well. Text to speech button converts the displayed txt to speech and the clear button clears the text.

![Screenshot 2025-06-11 103135](https://github.com/user-attachments/assets/e1dc4c1a-4b1e-4a50-b767-8bae0bf4cdb7)

![screengrab of prject for git](https://github.com/user-attachments/assets/5c93e9a5-17b1-44de-9291-2382ed52ab6d)


Here are our accuracies for our testing and validation dataset:

![Screenshot 2025-06-11 104507](https://github.com/user-attachments/assets/2ff7459f-503c-4aae-af76-d865d8e761e2)

Our Training and Validation Loss and Accuracy graphs graphs.

![Screenshot 2025-06-11 104617](https://github.com/user-attachments/assets/fcd5eeb1-4d97-4eba-987d-b9ebf2b9f454)
![Screenshot 2025-06-11 104631](https://github.com/user-attachments/assets/7cc2c6dc-2cb5-492c-8ff5-b2546bf2c4c1)
![image](https://github.com/user-attachments/assets/e2bad22c-28fb-4041-8a10-b74a621c01ae)

The goal of this project is to use neural networks to develop a real-time sign language recognition system that is specifically designed for the Indian Sign Language (ISL). We display our experimentation and approach to recognize Indian sign language input in real time using Convolutional Neural Network with an overall accuracy of the model being above 99\%. Our model provides quality and favorable recognition for both one-handed and two-handed signs done by user with limited real time delay and can be expanded to work with larger datasets. It can be determined that multiple layers of Convolutional Neural Networks provide better accuracy for larger datasets, as it did for our custom created dataset. CNN proves to be very competent and useful to work with image dataset and extracts relevant features, good enough to predict proficiently in real time. Thus through our research we can establish that using Neural network technologies like CNN can help create systems for deaf, mute and disabled communities which help make communication easier for them through such technological advancements. ![image](https://github.com/user-attachments/assets/586e3ab8-ade8-49dd-b902-32c76d29417a)



