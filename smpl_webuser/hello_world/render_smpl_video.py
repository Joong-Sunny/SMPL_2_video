'''
Copyright 2015 Matthew Loper, Naureen Mahmood and the Max Planck Gesellschaft.  All rights reserved.
This software is provided for research purposes only.
By using this software you agree to the terms of the SMPL Model license here http://smpl.is.tue.mpg.de/license

More information about SMPL is available here http://smpl.is.tue.mpg.
For comments or questions, please email us at: smpl@tuebingen.mpg.de


Please Note:
============
This is a demo version of the script for driving the SMPL model with python.
We would be happy to receive comments, help and suggestions on improving this code 
and in making it available on more platforms. 


System Requirements:
====================
Operating system: OSX, Linux

Python Dependencies:
- Numpy & Scipy  [http://www.scipy.org/scipylib/download.html]
- Chumpy [https://github.com/mattloper/chumpy]
- OpenCV [http://opencv.org/downloads.html] 
  --> (alternatively: matplotlib [http://matplotlib.org/downloads.html])


About the Script:
=================
This script demonstrates loading the smpl model and rendering it using OpenDR 
to render and OpenCV to display (or alternatively matplotlib can also be used
for display, as shown in commented code below). 

This code shows how to:
  - Load the SMPL model
  - Edit pose & shape parameters of the model to create a new body in a new pose
  - Create an OpenDR scene (with a basic renderer, camera & light)
  - Render the scene using OpenCV / matplotlib


Running the Hello World code:
=============================
Inside Terminal, navigate to the smpl/webuser/hello_world directory. You can run 
the hello world script now by typing the following:
>	python render_smpl.py


'''
import cv2
import numpy as np
from opendr.renderer import ColoredRenderer
from opendr.lighting import LambertianPointLight
from opendr.camera import ProjectPoints
import pickle
import sys
sys.path.append('/home/sunny/python_project/SMPL/SMPL_python_v.1.0.0/smpl/')
from smpl_webuser.serialization import load_model


## Assign attributes to renderer
rn = ColoredRenderer()
w, h = (640, 480)

## Load SMPL model (here we load the female model)
m = load_model('./models/basicModel_f_lbs_10_207_0_v1.0.0.pkl') #male? female? fat? old? here

## Load aist dance model
with open('./models/dance.pkl','rb') as fr:                     #put dance motion pkl in here
    data2 = pickle.load(fr)
for key, value in data2.items():
    print(key)
pose = data2['smpl_poses']

#ready to write video
fps = 60
size = (w,h)
pathOut = './dancedance2.mp4'
# out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'MPEG'), fps, size)
out = cv2.VideoWriter(pathOut, cv2.VideoWriter_fourcc(*'mp4v'), fps, size)

#adding pose!!!
for i in range(len(pose)):
    m.pose[:] = pose[i]
    m.betas[:] = np.random.rand(m.betas.size) * .03
    m.pose[0] = np.pi

    rn.camera = ProjectPoints(v=m, rt=np.zeros(3), t=np.array([0, 0, 2.]), f=np.array([w,w])/2., c=np.array([w,h])/2., k=np.zeros(5))
    rn.frustum = {'near': 1., 'far': 10., 'width': w, 'height': h}
    rn.set(v=m, f=m.f, bgcolor=np.zeros(3))

    ## Construct point light source
    rn.vc = LambertianPointLight(
        f=m.f,
        v=rn.v,
        num_verts=len(m),
        light_pos=np.array([-1000,-1000,-2000]),
        vc=np.ones_like(m)*.9,
        light_color=np.array([1., 1., 1.]))
    
    temp_copy = np.uint8(rn.r *255)

    out.write(temp_copy)

    print(i, 'is done...')

out.release()

## Show it using OpenCV
# import cv2
# cv2.imshow('render_SMPL', rn.r)
# print ('..Print any key while on the display window')
# cv2.waitKey(0)
# cv2.destroyAllWindows()


## Could also use matplotlib to display
# import matplotlib.pyplot as plt
# plt.ion()
# plt.imshow(rn.r*255)
# plt.show()
# import pdb; pdb.set_trace()