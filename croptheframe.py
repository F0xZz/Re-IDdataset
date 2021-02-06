
"""
@author:  Fox
@contact: 
@basedcode: myconvert.py
@start-time : 2021-02-25 14:16
@finish-time : 2021-02-25 15:10
@use : use this script convert the label to Market1501 datasets but no shuffle
"""

import os 
import cv2 
import numpy as np
import shutil
import glob
import random
def processVideo(videopath):
    # this process will convert the video data to the frame
    cap = cv2.VideoCapture(videopath)
    fps = int(cap.get(5))
    sumframe = int(cap.get(7)) # get the sum of frames 
    savepath = os.path.join(os.getcwd(),(videopath.split('\\')[-1]).split('.')[0])
    # print(savepath)
    # print(savejpgpath)
    # i = 0
    # if not os.path.exists(savepath):
    #     os.makedirs(savepath)
    # while True:
    #     _, frame = cap.read()
    #     if i < sumframe:
    #         savejpgpath = os.path.join(savepath,str(i)+'.jpg')
    #         if(i %100 ==0):
    #             print("the video data is saving")
    #             print(savejpgpath)
    #         cv2.imwrite(savejpgpath,frame)
    #         i = i + 1
    return 0

def readlist(file): # 372,person,3,671,407,41,76 txt datafile and source bbox test
    frameid = []  # ['1005', 'person', '7', '270', '408', '101', '139']
    classid = [] 
    pid = []
    bbox = []
    f=open(file)
    # n = 0
    listlabel = f.readlines()
    for lines in listlabel:
        lines = lines.replace('\n','')
        sepmark = lines.split(',')
        # if(n<2):
        #     print(lines)
        #     n = n+1
        frameid.append(sepmark[0])
        classid.append(sepmark[1])
        pid.append(sepmark[2])
        bbox.append((sepmark[3],sepmark[4],sepmark[5],sepmark[6]))
        
    return frameid,classid,pid,bbox

def xywh (bboxs,width,height):
    box = []
    for bbox in bboxs:
        # print(bbox)
        x = bbox[0]
        y = bbox[1]
        w = bbox[2]
        h = bbox[3]
        x = int(max(int(x),1))
        y = int(max(int(y),1))
        if int(x+int(w))>int(width):
            # print("is out the boundary of the image")
            # print(x,w)
            w = int(width-x-1)
            # print("is refresh")
            # print(x,w)
        if int(y+int(h))>height:
            # print("is out the boundary of the image")
            # print(y,h)
            h = int(height - y -1)
            # print("is refresh")
            # print(y,h)
        box.append((x,y,w,h))
    return box

def crop_img (pid,cameraid,serid,frame_file,frameid,bboxs): # crop the image set in the same folder
    # n = 0
    for i in range(len(bboxs)):
        bbox = bboxs[i]
        
        x1 = int(bbox[0])
        y1 = int(bbox[1])
        w = int(bbox[2])
        h = int(bbox[3])
        x2 = x1 + w
        y2 = y1 + h
        # n= n+1
    # print(n)
        sourceimg = cv2.imread(os.path.join(frame_file,frameid[i]+".jpg"))
        # print(sourceimg.shape)
        afcrop_img = sourceimg[y1:y2, x1:x2]
        namepath = str(pid[i])+"_"+"c"+str(cameraid)+"s"+str(serid)+"_"+str(frameid[i])+"_"+"00"+".jpg"
        crop_save_path = os.path.join(os.getcwd(),"cropimage")
        if not os.path.exists(crop_save_path):
            os.makedirs(crop_save_path)
        crop_save_in_folder = os.path.join(crop_save_path,namepath)
        cv2.imwrite(crop_save_in_folder,afcrop_img)
        if (i - 20 == 0 ):
            print("is running")
            print(crop_save_path)
            break
    return 0

def crop_img_sep (pid,cameraid,serid,frame_file,frameid,bboxs): # crop the image set in the same folder
    # n = 0
    for i in range(len(bboxs)):
        bbox = bboxs[i]
        
        x1 = int(bbox[0])
        y1 = int(bbox[1])
        w = int(bbox[2])
        h = int(bbox[3])
        x2 = x1 + w
        y2 = y1 + h
        # n= n+1
    # print(n)
        sourceimg = cv2.imread(os.path.join(frame_file,frameid[i]+".jpg"))
        # print(sourceimg.shape)
        afcrop_img = sourceimg[y1:y2, x1:x2]
        namepath = str(pid[i])+"_"+"c"+str(cameraid)+"s"+str(serid)+"_"+str(frameid[i])+"_"+"00"+".jpg"
        crop_save_path = os.path.join(os.getcwd(),"sepimage")
        sep_img_path = os.path.join(crop_save_path,str(pid[i]),str(cameraid))
        if not os.path.exists(crop_save_path):
            os.makedirs(crop_save_path)
        if not os.path.exists(sep_img_path):
            os.makedirs(sep_img_path)

        crop_save_in_folder = os.path.join(sep_img_path,namepath)
        cv2.imwrite(crop_save_in_folder,afcrop_img)
        if (i % 20 == 0 ):
            print("is running")
            print(crop_save_in_folder)
            # break
    return 0


def read_frame (cameraid,serid,frame_file,label_file):
    framelist = os.listdir(frame_file) 
    imagepath = os.path.join(frame_file,framelist[0])
    labellist  = os.listdir(label_file)
    img = cv2.imread(imagepath)
    height,width = img.shape[:2]
    for file in labellist: #this is the folder and contain the label txt
        file = os.path.join(label_file,file)
        # print(file)
        frameid,classid,pid,bbox = readlist(file)
    # print(len(bbox[0]))
    bbox = xywh(bbox,width,height)    # print(type(frameid))
        # for id in frameid:
        #     # print(type(id))
        #     crop_img(id,pid,bbox)
    # crop_img(pid,cameraid,serid,frame_file,frameid,bbox) 
    #pid,cameraid,serid,frame_file,frameid,bboxs
    crop_img_sep(pid,cameraid,serid,frame_file,frameid,bbox)
    # if you wanna sep the id cameraid serial id 
    return 0    

if __name__=='__main__':
    Videodatasource = "Videodata" # this filename is the set of video file
    Labeldatafile = "Labelfile" # this folder saves the labelfile 
   
    root = os.getcwd() # get the root dir
   
    CamID = 0 # this is the pre set of camid
    SerID = 0 # this is the pre set of same camid and different serial  
   
    videolist = os.listdir(os.path.join(root,Videodatasource)) #return the list  of video's name
    
    cameralist = os.listdir(os.path.join(root,Labeldatafile)) #return the list of camera marklabel folder
     
    # for videoname in videolist:
    #     print(os.path.join(root,Videodatasource,videoname))
    #     processVideo(os.path.join(root,Videodatasource,videoname)) # write this video to frame
        # and this video's frame will save in the this folder root/videoname/
    for cameraID in cameralist: # this will return cameraID
        CamID = CamID+1 # return the number of camera id use to set the jpg's name
        # print(CamID) 
        # print(os.path.join(root,Labeldatafile,cameraID))
        label_folder = os.path.join(root,Labeldatafile,cameraID)
        print(label_folder)
        sam_Cam_serial_list = os.listdir(label_folder)
        # this will return the videoname.txt
        SerID = 0
        for sam_Cam_serial_Labelfile in sam_Cam_serial_list:
            SerID = SerID+1
            file = os.path.join(root,Labeldatafile,cameraID,sam_Cam_serial_Labelfile)
            video_frame_save_folder_name = (file.split('\\')[-1]).split('.')[0] 
            # this return the frame save data folder
            frame_data_file = os.path.join(root,video_frame_save_folder_name) 
            
            # this dir is contain the sum of frame
            read_frame(CamID,SerID,frame_data_file,label_folder)
            # f.open(file)