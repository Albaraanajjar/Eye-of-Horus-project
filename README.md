# Abstract
Wildfires are one of the most serious issues we face in our modern era due to climate change, causing damage to millions of hectares of forest resources and threatening the lives of people and animals. Of particular importance are risks to ecosystems and local communities as well as firefighters. which shed the light on the importance of leveraging technology and AI in monitoring and minimizing the risks in case of natural disasters. Eye of Horus project introduces an automated procedure to regularly check and monitor major forests around the world via computer vision technologies and automation technologies such as classification and segmentation to help authorities and firefighters in their responsibilities, provide scientists with visual data and research data for better understanding of this phenomena, as well as helping spread awareness around the world regarding the importance of preserving the environment.
the project dealt with multiple datasets for construction which were divided into ordinary fire or no fire visual data, ariel images, annotated ariel images for segmentation, and satellite collected images. This project also highlights multiple techniques in deep learning such as 1) transfer learning from a similar task model which managed successfully to generate an accuracy of 97% on training and validation as well as testing dataset, 2) Fire detection using segmentation methods to precisely determine fire borders. A deep learning method is designed based on the U-Net up-sampling and down-sampling approach to extract a fire mask from the video frames which managed successfully to get a precession of 92%. Moreover, our project utilized many mechanism to automate data collection and entry such as 1) automated sellenuim bot to collect visual data for wanted coordinates or places, 2) automated machnesim to lunch drone flights and collect data of the trips, 3) GUI User interface to enable the user to control key points of the process with a wide variety of customizable options and to show results of the procedure.

Keywords: Aerial imaging, fire monitoring dataset, fire detection and
segmentation, deep learning, automation, data collection

# Introduction: Scope, significance, and problem definition
Wildfires have caused severe damage to major forests and their surrounding ecosystems, local communities, transportation operations, tourism, and habitats around the globe. Based on statistics collected by our team it indicates that 2021 was a record year for wildfires, with 58,985 wildfires in 2021 affecting 7.1 million acres in the USA alone, with more than 17% increase from 2019 to 2021 in U.S. wildfires and a 223% increase since 1983, it’s estimated that 6.2 million people were affected directly between 1998-2017 with 2400 attributable deaths worldwide from suffocation, injuries, and burns. Moreover, economic losses due to wildfires are also countless with an average of 2 billion dollars spent alone to suppress wildfires in California alongside total damage of 16.5 billion dollars in 2020 in the USA, its worth mentioning that these figures represent only direct damages and not indirect damage which is estimated to be around 150 billion as per Yale Climate Connections.
![wildfires_download3_2021](https://user-images.githubusercontent.com/103533931/181112523-797a69b1-e548-4a04-91b1-aa4a4bbbfcdb.png)
![Average-size-of-US-wildfires-by-decade-](https://user-images.githubusercontent.com/103533931/181112630-800b8f6f-145a-41d1-8578-2ca97b45af75.jpg)

traditional approaches in most countries is manned routine monitoring which is expensive or using helicopters or fixed-wing aircraft to surveil
fires with visual and infrared imaging. Moreover, many wildfires happen in areas that are very deep in the forests which cant be detected by people early because of their distance from the nearest residential area like Amazon rainforest wildfires. Considering the challenges and issues of these methods, our project offers unmanned monitoring with the ability to locate fires in deep forests via unmanned viechles. Recent advances in artificial intelligence (AI) and machine learning have
made image-based modeling and analysis (e.g., classification, real-time prediction, and image segmentation) even more successful in different applications. Also, with the advent of nanotechnology semiconductors, a new generation of Tensor Processing Units (TPUs) and Graphical Processing Units (GPUs) can provide an extraordinary computation capability for data-driven methods and magnificent results. Moreover, drones and satellites collected data can be processed easily and passed into CNNs to predict the existence of fire and classifying.
Most supervised learning methods rely on large training datasets to train areasonably accurate model. most studies used a fire dataset from publicsources to perform fire detection based on pre-trained ANN architectures such as MobileNet and AlexNet. However, that dataset was based on terrestrial images of the fire.

# about the data used in this project

To the best of our knowledge, there are no satalite images datset for fire analysis, something in urgent need to develop fire modeling and analysis
tools for space visual monitoring systems. Note that space satalliete imagery exhibits different properties such as low resolutions, and top-view perspective, substantially different than images taken by ground cameras or drones.
In this project we introduce a new dataset of manually collected 2000 satallite images of wildfires around the world in the last 10 years, we hope this new dataset will benefit data scientsts around the world who work in researching fire processing and to add a new prespective of fire images to the community, and in this project we will focus on the potiential of providing scientsts with this kind of data and how our procedure help in making this kind of data available for those who are intrested.

# requirments
there is ```requirment.txt``` file which contains all packages and versions that must be in your machine to run our project. In addition you will have to install mission planner and must update neseccery file paths according to your machine
this project runs succesfully on paython 3.7

# project design
The project was designed to collect data of satellite visual images of a chosen criteria by the user (e.g. forests which the user wants to monitor, custom coordinates given by the user, images or datasets by the user) then process it to a classification model and this model outputs the predicted percentages of Fire vs No_fire and its class to the user, then if there is a fire the software will plan a drone trip via mission planner to validate the predictions of the first model, recording its trip in video format the software will split this video to frames and input it into an AI model which will check for fire frame by frame and determine specifically where the fire is to help identify fires at an early stage.
![Flowcharts (1)](https://user-images.githubusercontent.com/103533931/181237798-6901d516-309c-4551-8c28-5a824d021a10.png)
# methedology
This section contains the technical explanation of the technologies and methods we used to implement our project.

[explanation about data collection by selenium bot(to be written by Yaman)]

The image classification problem is one of the challenging tasks in the image processing domain. In the past, traditional image processing techniques utilized RGB channel comparison to detect different objects such as fire in frames or videos. These traditional methods are not free of errors and are not fully reliable. For instance, RGB value comparison methods that usually consider a threshold value to detect fire may detect sunset and sunrise as a false positive outcome. However, training a DNN to perform this image classification task helps to learn elements not germane to the fire. Also, some studies such as perform pixel-based classification and segmentation based on the HSV (Hue, Saturation, Value) format. The binary classification model which was used in this project is the Xception network proposed by Google-Keras1. The Xception model is a deep Convolutional Neural Network (DCNN). The structure of the DCNN. The Xception model has three main blocks: 1) the input layer, 2) the hidden layers, and 3) the output layer. The size of the input layer depends on the image size and the number of channels which in our case is (256 × 256 × 3). Then the value of RGBs in different channels are scaled to a float number between 0 and 1.0. The hidden layers rely on depth-wise separable convolutions and shortcut between the convolution blocks (ResNet ). Since the fire-detection is a binary classification task (Fire/No Fire), the activation function for the output layer is a Sigmoid function. Then from this trained model on a sufficient amount of drone images data. drone data was chosen because there is a sufficient amount of it and because its many similarities with satellite images like ariel angle of viewing and low resolution and many other attributes. Data augmentation and piecewise scheduler were used to deal with overfitting.

the second problem is image segmentation for frames labeled as ”fire” by the fire classification algorithm. Studying the fire segmentation problem is useful for scenarios like detecting small fires . Also, fire segmentation helps fire managers localize different discrete places of active burning for the purpose of fire monitoring. These segmentation problems were handled differently in the past using image processing and RGB threshold values to segment different data batches which exhibits relatively high error rates. To accomplish this task, a DCNN model is implemented to predict the label of each pixel based on the imported data. This segmentation problem can be recast as a binary pixel-wise classification problem, where each pixel can take two labels: ”fire” and ”non-fire” (background). The model was trained on labeled data by different technologies such as Labellmg, Django Labeller and many others. Luckily for us this was provided in FLAME dataset. The DCNN utilizes a dropout method to avoid the overfitting issue in the FLAME dataset analysis and realize a more efficient regularization noting the small number of ground truth data samples. The utilized loss function is the binary cross entropy. The Adam optimizer is used to find the optimal value of weights for the neurons. The evaluation of the FLAME-trained model with the ground truth data.

For the part of the drone mission, if we acquire coordinates and the image has been classified as fire, an automated bot by pywinauto and pyautogui libraries will choose the right vehicle for the job and set coordinates of the potential fire and launch a drone flight. Moreover, our procedure records the video of the drone and shows it, and extracts it into frames for processing it by the segmentation model, the procedure is supposed to continue after the record to segmentation but due to tense regulation our procedure will stop at the video, but we have enabled for you a place in the application to test segmentation model for yourself on image or on video.
# user interface

Regarding user interface, we know tkinter is not the most beautiful gui design API in the world and we know that our user interface is not perfect as our project depends heavily on the procedure so it was our priority to focus on process integrity and its smoothness as well as giving User results and control over the process more than the external appearance of the application, so the user interface is just a tool we use to demonstrate the process and to control it.

# AI models diagrams
model used for fire segementation:
![image](https://user-images.githubusercontent.com/103533931/181243052-1f39cabf-b9bf-491e-84a3-86d3f5d701f4.png)
model used in fire classidfication task:
![WhatsApp Image 2022-07-27 at 3 52 21 PM](https://user-images.githubusercontent.com/103533931/181253231-44a5caee-d45f-4327-a247-96176023189b.jpeg)

#results

# disclaimer regarding drone procedure
Unfortunately in Jordan, we have very tense regulations limiting any use of drones and UAV’s, so there will be no way to actually test the processing video into the model procedure, we have automated the process of launching drone flight to the desired location which will be virtual flight hence virtual video, not real one, but this process is implemented clearly in the code and there is a test video within FLAME dataset if you want to see the segmentation model for yourself so you will see in the code mechanism for extracting video from the drone and converting it to frames and inserting it in the model.


# results
In the original training of the transferred model of classification the amount of images used was 39,375 which includes 25,018 frames of type ”fire” and 14,357 frames of type ”non-fire”. The training dataset is further split to 80% training and 20% validation sets. All frames are shuffled before feeding into the network. Then the new model which held the weights of the previous one trained 5090 images which were divided into 3500 non fire images and 1590 of fire class which was further split into 80% training set and 20% validation set then we tested it on 410 fire images and 959 non fire images.
The classification model got us an accuracy of accuracy: 0.9737 when training and a similar percentage while testing it.
While the fire segmentation model generated in getting precision of 92% and recall of 83.88%

fire segementation model performence relative to labels:

![Screenshot 2022-07-27 164831](https://user-images.githubusercontent.com/103533931/181265057-81e0331e-0f23-4070-8d0c-bbc7cd2d901b.png)
# variety of options introduced to the user

The user has a wide variety of options at hand which enables him/her to have a big aamount of control over the process and enhance the user experience:

•	Ability to choose specific places to conduct a routine scan on

•	Ability to input custom coordinates

•	Ability to upload single or multiple images manually through file dialog

•	Ability to cancel drone flight in case of fire detection

•	Ability to control threshold of fire detecting

•	Ability to send optional drone flight even in the case of no fire



# potential for improvement and ideas

•	Linking the project to a real drone

•	Expanding variety of options to the user

•	Using smoother mechnesims for data collection like scrapy

•	Better user interface

•	Automated daily monitoring a specific fire and collecting organized data

# business potential
"Data is the oil of 21st century"
This project can be used mainly to sell datasets that are completly different from other datasets provided to scientsts regarding wildfires, as this software can aqquire satellite data linked with ariel images taken by drones. testing with this kind of data in researching might help humanity predict wildfires patterns or early detect fires to minimize damage due to wildfires.

this software can also provide clear data to dicision makers and students to raise awarness of this matter.

# conclusion
Afterall, this project was built in three days and there is much room for improvment and much better tools to implement tasks in this project, but we tried to take advantege of the tools we already know how to deal with taking in considrration this narrow window of time and trying to coordinate time with our university and with study pressure, we hope that you had a fun read and we hope this project can push even if little our industry or spread awarness to preserve the environment.

