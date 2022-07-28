import pickle
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
import os, shutil
#import imshow as imshow
from PIL import Image, ImageTk
import tensorflow as tf
from tensorflow import keras
import keras
import numpy as np
from keras import models
from keras.preprocessing.image import ImageDataGenerator
import time
from tqdm import tqdm
import matplotlip as plt
import matplotlib.pyplot as plt
import cv2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
class Root:
    def __init__(self, title, bg_color, buttons_color, text_color, geometry):
        self.bg_color = bg_color
        self.buttons_color = buttons_color
        self.text_color = text_color
        self.class_root = tk.Tk()
        self.class_root.resizable(False, False)
        self.class_root.title(title)
        self.class_root.configure(background=bg_color)
        self.class_root.geometry(geometry)



    def Button(self, text, command, x, y, font=None, height=0, width=0):
        if font is None:
            button = tk.Button(self.class_root, text=text, background=self.buttons_color, foreground=self.text_color,
                               command=command, height=height, width=width)
        else:
            button = tk.Button(self.class_root, text=text, background=self.buttons_color, foreground=self.text_color,
                               command=command, height=height, width=width, font=("", font))
        button.place(x=x, y=y)

    def Destroy_window(self):
        for child in self.class_root.winfo_children():
            child.destroy()

    def Main_page_Button_action(self):
        self.Destroy_window()
        Main_page()

    def Forest_Live_Monitoring_page_Button_action(self):
        self.Destroy_window()
        Forest_Live_Monitoring_page()

    def Satellite_Image_Classification_page_Button_action(self):
        self.Destroy_window()
        Satellite_Image_Classification_page()

    def Drone_Image_Classification_page_Button_action(self):
        self.Destroy_window()
        Drone_Image_Classification_page()

    def Description_page_Button_action(self):
        self.Destroy_window()
        Description_page()

    def Setting_page_Button_action(self):
        self.Destroy_window()
        Setting_page()

    def Label(self, text, x, y, font):
        label = tk.Label(self.class_root, text=text, background=self.bg_color, fg=self.buttons_color, font=("", font))
        label.place(x=x, y=y)

    def Back_button(self, page):
        if page == "Main page":
            root.Button("<--", self.Main_page_Button_action, 20, 20, width=3, height=1)
        elif page == "loop through page":
            root.Button("<--", self.Forest_Live_Monitoring_page, 20, 20, width=3, height=1)
        elif page == "Import File page":
            root.Button("<--", self.Forest_Live_Monitoring_page, 20, 20, width=3, height=1)

    def Main_Loop(self):
        self.class_root.mainloop()

bg= "lightgray"
fg= "darkslategrey"
root = Root("The Eye of Horus", bg, fg, bg, "494x550")


global x, y, i,coordinates,coord,filename

def Main_page():
    print("main page")
    root.Label("The Eye of Horus", 65, 70, 34)
    root.Button("Forest Live Monitoring", root.Forest_Live_Monitoring_page_Button_action, 80, 200, 24)
    root.Button("Satellite Image Classification", root.Satellite_Image_Classification_page_Button_action, 83, 300, 18)
    root.Button("Drone Image Classification", root.Drone_Image_Classification_page_Button_action, 83, 380, 19)



def Forest_Live_Monitoring_page():
    print("loop through page")
    root.Back_button("Main page")
    root.Label("Description", 180, 130, 22)
    root.Button("Custom Coordinates", Custom_Coordinates_button_action, 80, 250, 25)
    root.Label("Forestes:", 30, 340, 22)
    root.Button("congo forest", congo_forest, 35, 400, 14)
    root.Button("Sundarbans", Sundarbans, 35, 473, 14)
    root.Button("Tongass National Forest", Tongass_National_Forest, 235, 400, 14)
    root.Button("Kinabalu National Park", Kinabalu_National_Park, 235, 473, 14)
def replace_pho_jpg():
    folder = 'drone_segementation_images'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    k = Image.open('img.jpg')
    j = os.path.join('drone_segementation_images', 'img.jpg')
    k.save(j)

def Satellite_Image_Classification_page():
    global coord
    print("Satellite_Image_Classification")
    global filename
    filename = filedialog.askopenfilenames()
    if (filename != ""):
        for x in filename:
            SI = Image.open(x)
            SI.save(f"pho.png")
            replace_pho()
            score= model()
    root.Destroy_window()
    Main_page()


def Drone_Image_Classification_page():
    print("Drone_Image_Segmentation")
    filename = filedialog.askopenfilenames()
    if (filename != ""):
        for x in filename:
            SI = Image.open(x)
            SI.save(f"pho.jpg")
            folder = 'drone_segementation_images'
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print('Failed to delete %s. Reason: %s' % (file_path, e))
            k = Image.open('pho.jpg')
            j = os.path.join('drone_segementation_images', 'pho.jpg')
            k.save(j)
            seg_model()
    Main_page()

def Description_page():
    print("description page")
    root.Back_button("Main page")
    root.Label("Description", 180, 130, 22)

def Setting_page():
    print("setting page")
    root.Back_button("Main page")

# Actions functions

def replace_pho():
    folder = 'test\\test'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    k = Image.open('pho.png')
    j = os.path.join('test\\test', 'pho.png')
    k.save(j)

def extracting_vid(vid_path):
    target_folder = 'drone_segementation_images'

    vidcap = cv2.VideoCapture(vid_path)
    count = 0
    while True:
        success,image = vidcap.read()
        if not success:
            break
        cv2.imwrite(os.path.join(target_folder,"frame{:d}.jpg".format(count)), image)
        count += 1
    print("{} images are extacted in {}.".format(count,target_folder))
def seg_model():
    dir_images='drone_segementation_images'

    def plot_segmentation_test(xval, ypred, num_samples):
        fig = plt.figure(figsize=(13, 6))
        for i in range(0, num_samples):
            plt.subplot(3, num_samples, (0 * num_samples) + i + 1)

            ix_val = i
            title = str(i + 1)
            plt.title(title)
            plt.imshow(xval[ix_val])
            plt.axis('off')

            plt.subplot(3, num_samples, (2 * num_samples) + i + 1)
            plt.imshow(np.squeeze(ypred[ix_val]))
            plt.title('Mask')
            plt.axis('off')
        plt.subplots_adjust(wspace=0.05, hspace=0.1)
        # /FigureObject/segmentation_test.fig.pickle
        # /Figures/segmentation_test.pdf
        file_figobj = 'Output.PNG' % ()
        file_pdf = 'Output.pdf' % ()
        pickle.dump(fig, open(file_figobj, 'wb'))
        fig.savefig(file_pdf, bbox_inches='tight')

    #dir_images = 'test'
    #dir_masks = 'seg mask'
    allfiles_image = sorted(
        [
            os.path.join(dir_images, fname)
            for fname in tqdm(os.listdir(dir_images))
            if fname.endswith(".jpg")
        ]
    )

    size = 512
    x_train = np.zeros((len(allfiles_image), 512, 512, 3), dtype=np.uint8)
    # y_train=np.zeros((len(allfiles_mask), 512, 512, 3), dtype=np.bool)
    for n, file_ in tqdm(enumerate(allfiles_image)):
        img = tf.keras.preprocessing.image.load_img(file_, target_size=(512, 512))
        x_train[n] = img

    seg = models.load_model('FireSegmentation.h5')
    tf.config.run_functions_eagerly(True)
    hist = seg.predict(x_train, verbose=1)
    preds_val_t = (hist > 0.5).astype(np.uint8)
    plot_segmentation_test(xval=x_train, ypred=preds_val_t, num_samples=1)
def model():

    model = models.load_model('my_final_model.h5')  # 7ot esm elmodel wbas, bas t'akad ykon 3ndk msayav bmalaf elmshroo3

    test_datagen = ImageDataGenerator(rescale=1 / 255.)

    test_generator = test_datagen.flow_from_directory('test'  # put elmlaf elkbeer directory
                                                      ,
                                                      # only read images from `test` directory
                                                      classes=['test'],
                                                      # don't generate labels
                                                      class_mode=None,
                                                      # don't shuffle
                                                      shuffle=False,
                                                      # use same size as in training
                                                      target_size=(256, 256))
    preds = model.predict(test_generator)
    score = preds[0]
    print("This image is %.2f percent Fire and %.2f percent No Fire." % (100 * (1 - score), 100 * score))
    if score > 0.5:
        print("NO_FIRE")
    else:
        print("fire")
    return score

def replace(str, num):
    i = 0
    new_str = ""
    if (num == 0):
        while (str[i] != '°'):
            new_str+=str[i]
            i+=1
    elif (num == 1):
        while (str[i] != ","):
            i+=1
        i+=1
        while (str[i] != "°"):
            new_str+=str[i]
            i+=1
    return float(new_str)

def Forest_button_action():
    print("forest")

def congo_forest():
    listr= [-5.8825301269767705,12.49969107247275,-5.892775477996132,12.713924467469573,-5.970292482728439,12.713237821972788,-6.0331176090122955,12.479091707569204]
    Nasa_bot(listr)

def Kinabalu_National_Park():
    listr= [6.576802925161246,117.1872561749915,6.111379729504727,117.35067780322623,6.085434861232265,116.63793977756374,6.489483054094449,116.6214602856409]
    Nasa_bot(listr)

def Tongass_National_Forest():
    listr= [56.95890063765958,-133.5976508396513,56.916702956142885,-133.59325922909792,56.91511886470219,-133.676449980631,57.00188096194036,-133.676449980631]
    Nasa_bot(listr)

def Sundarbans():
    listr= [22.125258104136844,89.46736868074314,21.790227253241042,89.45086060419453,21.79653887437188,89.07214590690342,22.165732344247147,89.1206990732228]
    Nasa_bot(listr)

def Nasa_bot(coordinates_list):
    if len(coordinates_list) == 8:
        if coordinates_list[1] > coordinates_list[3]:
            coordinates_list[1] = coordinates_list[3]
        elif coordinates_list[1] <= coordinates_list[3]:
            coordinates_list[3] = coordinates_list[1]

        if coordinates_list[0] > coordinates_list[4]:
            coordinates_list[0] = coordinates_list[4]
        elif coordinates_list[0] <= coordinates_list[4]:
            coordinates_list[4] = coordinates_list[0]

        if coordinates_list[5] > coordinates_list[7]:
            coordinates_list[7] = coordinates_list[5]
        elif coordinates_list[5] <= coordinates_list[7]:
            coordinates_list[5] = coordinates_list[7]

        if coordinates_list[2] > coordinates_list[6]:
            coordinates_list[6] = coordinates_list[2]
        elif coordinates_list[2] <= coordinates_list[6]:
            coordinates_list[2] = coordinates_list[6]
    global x, y, i, coordinates

    print(coordinates_list)
    Givin_y1= coordinates_list[1]
    Givin_x1= coordinates_list[0]
    Givin_y2= coordinates_list[3]
    Givin_x2= coordinates_list[2]
    Givin_y3= coordinates_list[5]
    Givin_x3= coordinates_list[4]
    Givin_y4= coordinates_list[7]
    Givin_x4= coordinates_list[6]
    x = Givin_x1
    y = Givin_y1
    i = 0
    s2 = (f'{y}°,{x}°')
    time_sleep= 4
    PATH = 'C:\SeleniumDrivers\chromedriver.exe'
    sleep_time = 1
    '''oop= webdriver.ChromeOptions()
    oop.headless= True
    driver = webdriver.Chrome(PATH, options=oop)'''
    driver = webdriver.Chrome(PATH)

    driver.get("https://worldview.earthdata.nasa.gov/")
    print("loading...")
    driver.maximize_window()


    def Search_with_coordinates(co):
        coordinates=(f"coo:{co}")
        username = driver.find_element(By.ID, "location-search-autocomplete")
        username.send_keys(co)
        username.send_keys(Keys.RETURN)
        xx = driver.find_element(By.XPATH, "//div[@class='input-group-prepend']/button[1]")
        xx.click()

    def Remove_Mark():
        mark = driver.find_element(By.XPATH, "//div[@class='fade show']/div[1]/span[1]")
        mark.click()

    def RIGHT():
        global x
        z = x + 1.5815
        z = z * 10000
        z = int(z) / 10000
        x = z
        Coordinates = (f'{y}°,{x}°')
        search = driver.find_element(By.XPATH, "//div[@id='location-search-wrapper']/button[1]")
        search.click()
        Search_with_coordinates(Coordinates)

    def LIFT():
        global x
        z = x - 1.5815
        z = z * 10000
        z = int(z) / 10000
        x = z
        Coordinates = (f'{y}°,{x}°')
        search = driver.find_element(By.XPATH, "//div[@id='location-search-wrapper']/button[1]")
        search.click()
        Search_with_coordinates(Coordinates)

    def UP():
        global y
        z = y + 0.8862
        z = z * 10000
        z = int(z) / 10000
        y = z
        Coordinates = (f'{y}°,{x}°')
        search = driver.find_element(By.XPATH, "//div[@id='location-search-wrapper']/button[1]")
        search.click()
        Search_with_coordinates(Coordinates)

    def Down():
        global y
        z = y - 0.8862
        z = z * 10000
        z = int(z) / 10000
        y = z
        Coordinates = (f'{y}°,{x}°')
        search = driver.find_element(By.XPATH, "//div[@id='location-search-wrapper']/button[1]")
        search.click()
        Search_with_coordinates(Coordinates)

    def Alert_Dismiss():
        command = ActionChains(driver)
        command.send_keys(Keys.ESCAPE)
        command.perform()


    def Process_image():
        im = Image.open('pho.png')
        x1, y1, x2, y2 = 452, 90, 1581, 690
        cropped = im.crop((x1, y1, x2, y2))
        cropped.save("pho.png")


    def Screenshot():
        driver.save_screenshot('pho.png')
        Process_image()


    def Zoomin():
        zoomin = driver.find_element(By.XPATH, "//div[@class='wv-zoom-buttons']/button[1]")
        zoomin.click()
        time.sleep(sleep_time)


    def Zoomout():
        zoomout = driver.find_element(By.XPATH, "//div[@class='wv-zoom-buttons']/button[2]")
        zoomout.click()
        time.sleep(sleep_time)


    def Press_UP_button():
        command = ActionChains(driver)
        command.send_keys(Keys.ARROW_UP)
        command.perform()


    def Press_RIGHT_button():
        command = ActionChains(driver)
        command.send_keys(Keys.ARROW_UP)
        command.perform()


    def Press_LEFT_button():
        command = ActionChains(driver)
        command.send_keys(Keys.ARROW_UP)
        command.perform()


    def Press_DOWN_button():
        command = ActionChains(driver)
        command.send_keys(Keys.ARROW_UP)
        command.perform()


    # start commands here
    time.sleep(9)
    Alert_Dismiss()
    time.sleep(7)
    Search_with_coordinates(s2)
    hide = driver.find_element(By.ID, 'hideCoastlines_15m')
    hide.click()
    time.sleep(6)
    Screenshot()
    replace_pho()
    score = model()
    time.sleep(time_sleep)
    while (x < Givin_x4):
        i += 1
        RIGHT()
        time.sleep(time_sleep)
        Screenshot()
        replace_pho()
        score = model()
    UP()
    time.sleep(time_sleep)
    while (y < Givin_y4):
        for _ in range(i):
            LIFT()
            time.sleep(time_sleep)
            Screenshot()
            replace_pho()
            score = model()
        if (y > Givin_y4):
            continue
        UP()
        time.sleep(time_sleep)
        for _ in range(i):
            RIGHT()
            time.sleep(time_sleep)
            Screenshot()
            replace_pho()
            score = model()
        if (y > Givin_y4):
            continue
        UP()
        time.sleep(time_sleep)
    driver.close()
    print("Done")

def Custom_Coordinates_button_action():
    print("Custom Coordinates button")
    root.Destroy_window()
    #root.Back_button("loop through page")

    root.Label("please enter coordinates\nin this form-(51.7724°,14.7445°)", 55, 90, 22)
    root.Label("First Coordinate", 16, 205, 13)
    root.Label("Second Coordinate", 16, 265, 13)
    root.Label("Third Coordinate", 16, 325, 13)
    root.Label("Fourth Coordinate", 16, 385, 13)
    text_box1 = tk.Entry(root.class_root, font=("", 15))
    text_box1.place(x=177, y=207)

    text_box2 = tk.Entry(root.class_root, font=("", 15))
    text_box2.place(x=177, y=267)

    text_box3 = tk.Entry(root.class_root, font=("", 15))
    text_box3.place(x=177, y=327)

    text_box4 = tk.Entry(root.class_root, font=("", 15))
    text_box4.place(x=177, y=387)
    error_label= tk.Label(root.class_root, "", bg=bg, fg= "red")
    error_label.place(x=185, y=437)
    def entry_action():
        if (text_box1.get()=="") or (text_box2.get()=="") or (text_box3.get()=="") or (text_box4.get()==""):
            error_label.configure(text="Pleas Enter All Coordinates")
        elif ("," not in text_box1.get()) or ("," not in text_box2.get()) or ("," not in text_box3.get()) or ("," not in text_box4.get()):
            error_label.configure(text="Pleas Enter Coordinates in the right form")
        elif ("°" not in text_box1.get()) or ("°" not in text_box2.get()) or ("°" not in text_box3.get()) or ("°" not in text_box4.get()):
            error_label.configure(text="Pleas Enter Coordinates in the right form")
        else:
            error_label.configure(text="")
            Coordinates_list= [replace(text_box1.get(), 0), replace(text_box1.get(),1), replace(text_box2.get(),0),replace(text_box2.get(),1),replace(text_box3.get(),0),replace(text_box3.get(),1),replace(text_box4.get(),0),replace(text_box4.get(),1)]

            root.Destroy_window()
            Main_page()
            Nasa_bot(Coordinates_list)

    entry_button = tk.Button(root.class_root, text="Enter", command=entry_action, font=("", 17), bg= bg)
    entry_button.place(x=215, y=467)
tf.config.run_functions_eagerly(True)
Main_page()
root.Main_Loop()
