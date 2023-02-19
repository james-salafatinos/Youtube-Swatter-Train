# Foreword

I often engage on side projects to design tools, frameworks, and methods to improve my productivity. Ironically, I spend alot of time on these side projects in lieu of actual work. 

Recently, I have come into the bad habit of mindlessly watching a lot of YouTube. Don't get me wrong, YouTube is a wonderful tool for learning and sharing the joy of funny videos. But, it is also an addictive drug, with vast quantities of garbage, waiting for my tired brain to go into low power mode and consume for far longer than I'd like.

The purpose of this side project is to try and "swat" YouTube away. If it comes on screen due to a brief lapse, **swat** it down.

# YouTube Swatter

The high level steps to make this `YouTube Swatter` are:
1. Create a dataset of images for the model to train on
2. Label the images with bounding boxes using `Label Studio`
3. Train a real-time object detection application with custom weights using `Ultralytics Yolo v8`
4. Implement app logic using the output of the model predictions
5. Package up and distribute app



## 1. Create a dataset of images for the model to train on
I made a quick program that just grabs a screenshot every second or so. But you can get your images anyway.
```
py capture_image_data.py

```

*...and then go about your daily life for a minute or two and let it capture the images*

## 2. Label the images with bounding boxes using `Label Studio`

1. Start the labeling tool: `py <yourpath>\label_studio\server.py` 
2. Label em... this takes a while...
3. Export with the YOLO settings


## 3. Train a real-time object detection application
All the hardwork was done by... [https://github.com/ultralytics/ultralytics](https://github.com/ultralytics/ultralytics)

#### You'll need these packages:

-  `py -m pip install --upgrade pip setuptools wheel` just in case
-  `py -m pip install ultralytics` for object detection
-  `py -m pip install --upgrade torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu117` for training on the GPU
-  `py -m pip install label-studio` for labeling
-  `py -m pip install pyautogui` for window and application logic


#### You'll need a custom_training.yaml file looks like this:
The `/train`/ and `/val` folders are where your images are stored
```
train: ./train
val: ./val
nc: 1
names : ["Youtube_logo"]
```

#### But you train your model like this:
```
model = YOLO("yolov8n.pt")
model.train(data="custom_training.yaml", epochs=150, imgsz=1920, batch=2)
metrics = model.val()
```


#### Then when it trains, you'll see this in the terminal:
It might take a few hours...
```
      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
     40/150      2.42G      1.087     0.6893     0.9597          5       1920:  15%|█▍        | 13/88 [00:04<00:25,  2.91it/s]
```

#### When it's done, check that the model actually did get trained, by looking at the validation set
HINT: You should see prediction boxes
```
.
└── runs/
    └── train/
        └── val/
            └── validation_batch0.png
            └── validation_batch1.png
            └── validation_batch2.png
            
```

#### After it's done training, you can go grab your trained model
```
.
└── runs/
    └── train/
        └── weights/
            └── best.pt
```


## 4. Implement app logic using the output of the model predictions
Basically just:
```
if YouTube_Logo_Detected():
    Close_Google_Chrome()
```

## 5. Package up and distribute app
The only things we need to distribute the repo so anyone can run it locally are:
```
#Save the requirements so people can pip install
py -m pip freeze > requirements.txt
```
keep the `best.pt` trained weights and a few of the files so a user can run:
```
train.py #for training...
predict.py #this is also basically app.run()
view.py #shows you what it's seeing
```



### This video was really helpful throughout the whole process. Ironically, its on YouTube.
https://www.youtube.com/watch?v=gRAyOPjQ9_s