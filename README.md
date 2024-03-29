# DeepFloor: Floor Plan Recognition 

In collaboration with Gemeente Amsterdam in 2020, 
this project aims to extract structured features from floor plan images as inputs for their fire risk model. 
This core image recognition model was originated from [DeepFloorplan](https://github.com/zlzeng/DeepFloorplan). 
We incorporated the model backbone and built a Django website for demo purpose. 


## How to run the demo?
1. Install packages:
```
pip install -r requirements/requirements.demo.txt
```
2. Download the [pretrained model](https://drive.google.com/drive/folders/1t6lDv82NXPGEUdZSu7gxjn2mg00JAwd9?usp=sharing
) to deepfloor/pretrained folder.

3. Run the command: 
```
python manage.py runserver
```