# Data System Project: Fire Risk Profiles

### Image Recognition on Floor Plans as Input for a Fire Risk Model

The project is in collaboration with Gemeente Amsterdam.

- Model code in *floor_plan_model* folder. 

- Application code in *API* folder. 

- Minified JavaScript in *front_end* folder.


# Floor_Plan_Model
This repo contains a basic procedure to train the model suggested by the paper 'Deep Floor Plan Recognition using a Multi-task Network with Room-boundary-Guided Attention'. The code has been modified from TF2DeepFloorplan, which rewrites the original code from zlzeng/DeepFloorplan into newer versions of Tensorflow and Python.
<br>
Network Architectures from the paper, <br>
<img src="resources/dfpmodel.png" width="50%"><img src="resources/features.png" width="50%">

## Requirements
Install the packages stated in `requirements.txt`, including `matplotlib`,`numpy`,`opencv-python`,`pdbpp`, `tensorflow-gpu` and `tensorboard`. <br>
The code has been tested under the environment of Python 3.7.4 with tensorflow-gpu==2.3.0, cudnn==7.6.5.32 and cudatoolkit==10.1.243. Used Nvidia 16 GB GDDR5X, 80 epochs take approximately 1 hour to complete.


## How to run?
1. Install packages via `pip` and `requirements.txt`.
```
pip install -r requirements.txt
```
2. According to the original repo, please download r3d dataset and transform it to tfrecords `r3d.tfrecords`.
3. Run the `train.py` file  to initiate the training, 
```
- import train
- config = {'batchsize':1, 'lr':1e-4, 'wd':1e-5, 'max_epochs':1, 'step_size':50, 'gamma':0.3,'logdir':'./log/Feb7_TFR5', 'saveTensorInterval':50, 'saveModelInterval':20,'restore':None, 'outdir':'./outFeb7_TFR5', 'train':True}
- train.main(config)
```
4. Run Tensorboard to view the progress of loss and images via,
```
tensorboard --logdir=log/store
```

## Result
The following top left figure illustrates the result of the training image after 60 epochs, the first row is the ground truth (left:input, middle:boundary, right:room-type), the second row is the generated results. However, the result is not yet postprocessed, so the colors do not represent the classes, the edges are not smooth and the same area does not only show one class. <br>
The remaining figures are the graphs of total loss, loss for boundary and loss for room.
<img src="resources/epoch60.png" width="40%">
<img src="resources/Loss.png" width="40%">
<img src="resources/LossB.png" width="40%">
<img src="resources/LossR.png" width="40%">
