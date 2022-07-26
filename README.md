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

