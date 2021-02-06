"""
@author:  Fox
@contact: 
@basedcode: None
@start-time : 2021-02-25 15:50
@pre-edited : 2021-02-26 08:57
@finish-time : 2021-02-26 09:31
@use : use this to shuffle the data and select the data
"""
#wanna to return the train ,gallery,query data the ratio is 0.35:0.55:0.1

import os 
import cv2 
import numpy as np
import shutil
import glob
import random
import shutil

def remove_same_list(person_ID,train_ID):
    for i in train_ID:
        person_ID.remove(i) 
    return person_ID
def get_selected_img(personID,mixdatapath,keywords):
    get_slt_img = []
    select_num = 30
    if keywords =="query":
        select_num = 6
    for ID in personID:
        frame_path = os.path.join(mixdatapath,ID)
        # this will return the /root/sepimage/personID
        Camera_list_dir = os.listdir(frame_path)
        # this will return the /root/sepimage/personID/CamID/
        for Camera_ID in Camera_list_dir:
            seq = int(select_num/len(Camera_list_dir))
            abs_path_frame = os.path.join(frame_path,Camera_ID)
            # print(abs_path_frame)
            list_frame = os.listdir(abs_path_frame)
            if (len(list_frame)<=seq):
                selected_frame_list = random.sample(list_frame,0.6*(len(list_frame))) 
                print("the label dataset is too smaller ")
            if (len(list_frame)>seq):     
                print("there is normal datasets ")
                selected_frame_list = random.sample(list_frame,seq)

                for selected_frame in selected_frame_list:
                    selected_dir_list = os.path.join(frame_path,Camera_ID,selected_frame)
                    get_slt_img.append(selected_dir_list)
            # get_slt_img = get_slt_img+selected_frame_list
    return get_slt_img
def save_img_path(person_frame_list,keywords):
    # for
    save_name = [] 
    for img_list in person_frame_list:
        save_name=img_list.split('\\')[-1]
        save_path = os.path.join(os.getcwd(),keywords)
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        save_file_dir = os.path.join(save_path,save_name)
        shutil.copyfile(img_list,save_file_dir)
        # cv2.imwrite(save_path,)
    return 0
def get_query_from_gallerypath(afterpath,mixdatapath):

    return 0

if __name__=='__main__':
    mixdataname = "sepimage"
    mixdatapath = os.path.join(os.getcwd(),mixdataname)
    trainwords = "train"
    gallerywords = "gallery"
    querywords = "query"
    # print(mixdatapath)
    personidlist = os.listdir(mixdatapath) # get the pid list
    train_person_ID = random.sample(personidlist,int(0.35*(len(personidlist)))) 
    # this will return the train personID 
    af_person_ID = remove_same_list(personidlist,train_person_ID)
    # this will return remove the train_person_ID from the sourceID  
    back_get_img = get_selected_img(train_person_ID,mixdatapath,trainwords)
    # this method will return the imglist path
    save_img_path(back_get_img,trainwords)
    # this will save image
    back_get_gallery_img = get_selected_img(af_person_ID,mixdatapath,gallerywords)
    # print(len(back_get_gallery_img))
    save_img_path(back_get_gallery_img,gallerywords)
    # get the list of frame
    back_get_query_img = get_selected_img(af_person_ID,mixdatapath,querywords)
    save_img_path(back_get_query_img,querywords)
    
    
    '''
    this can solve to get the train label
    '''
    
    