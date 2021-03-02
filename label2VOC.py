"""
@author:  Fox
@contact: 
@basedcode: myconvert.py
@start-time : 2021-03-01 13:33
@finish-time : 2021-03-01 
@use : use this script convert the label to VOC datasets and use to detect the object
"""
import os 
import glob 
import cv2
import numpy as np
import random
'''

using this convert to the YOLO labellist
input : The reid personlabel by the darklabel
input is txt frame num and with labelnum

output :
contain the data
datasets/images/im0.jpg
datasets/labels/im0.txt
'''
imgfolder =  "./oneevening/1300.jpg"
img = cv2.imread(imgfolder)
h,w = img.shape[:2] #wideth ,height
# w = 720
# h = 1280

print(w,h)
def processVideo(videopath,framelist,diclist):
    # this process will convert the video data to the frame
    i = 0
    cap = cv2.VideoCapture(videopath)
    fps = int(cap.get(5))
    sumframe = int(cap.get(7)) # get the sum of frames 
    savepath = os.path.join(os.getcwd(),"images")
    print(len(framelist))
    # print(sumframe)
    af_frame = random.sample(framelist,int(0.01*(len(framelist))))
    needed = []
    for f in af_frame:
        print(type(f))
        if f not in needed:
            needed.append(f)
        
    # print(len(needed))
    # print(len(af_frame))
    print(type(needed))
    print(needed)
    if not os.path.exists(savepath):
        os.mkdir(savepath)
    # savename = 0   
    # savepath = os.path.join(os.getcwd(),(videopath.split('\\')[-1]).split('.')[0])
    # print(savepath)
    # print(savejpgpath)
    # i = 0
    # if not os.path.exists(savepath):
    #     os.makedirs(savepath)
    while True:
        _, frame = cap.read()
        # print(type(needed))
        if str(i) in needed :
            savejpgpath = os.path.join(savepath,str(i)+'.jpg')
            print(savejpgpath)
            for j in range(len(diclist)):
                writeimgbool = 0
                frameid = diclist[j].get("frameid")
                if str(i) == str(frameid):
                    bbox = diclist[j].get("bbox")
                    # print(bbox)
                    # print(type(bbox))
                    cv2.imwrite(savejpgpath,frame)
                    write_label_file(str(i),bbox)
                    
                    
                    writeimgbool = 1
        if(i %100 ==0):
            print("the video data is saving")
            # print(savejpgpath)
        i = i + 1
        # print(i)
    return 0

def xywh (bbox,width,height):
    box = []
    # for bbox in bboxs:
        # print(bbox)
    x = int(bbox[0])
    y = int(bbox[1])
    w = int(bbox[2])
    h = int(bbox[3])
    ratiowidth = 1.0*w/width
    ratioheight = 1.0*h/height
    x = int(max(int(x),1))
    y = int(max(int(y),1))
    if int(x+int(w))>int(width):
        # print("is out the boundary of the image")
        # print(x,w)
        w = int(width-x-1)
        ratiowidth = 1.0*w / width
        # print("is refresh")
        # print(x,w)
    if int(y+int(h))>height:
        # print("is out the boundary of the image")
        # print(y,h)
        h = int(height - y -1)
        # print("is refresh")
        # print(y,h)
        ratioheight = 1.0*h / height
    cx = (x+int(w/2))/width
    cy = (y+int(h/2))/height
    # ratiowidth =  
    box.append((cx,cy,ratiowidth,ratioheight))
    # print(box[0][0])

    return box
def xywh_cxyrxy(frameid,bbox):
    '''
    input x y w h 
    output cx cy rw rh
    '''
    img = os.path.join(os.getcwd(),"images",str(frameid)+".jpg")
    # print(img)
    print(bbox)
    imgsource = cv2.imread(img)
    h,w = imgsource.shape[:2]
    box = xywh(bbox,w,h)
    x1 = int(box[0][0]*w)-int(0.5*box[0][2]*w)
    y1 = int(box[0][1]*h)-int(0.5*box[0][3]*h)
    x2 = int(box[0][0]*w)+int(0.5*box[0][2]*w)
    y2 = int(box[0][1]*h)+int(0.5*box[0][3]*h)
    print(x1,y1,x2-x1,y2-y1)
    cv2.rectangle(imgsource,(x2,y2),(x1,y1),(0,0,255),-1,cv2.LINE_AA)
    cv2.imshow("drawrect",imgsource)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return box
def write_label_file(frameid,bbox):
    '''
    input :
    frameid: is str or int
    bbox:x1,y1 ,w,h
    outpput:
    box:cx,cy,ratiow,ratioy
    '''
    save_label_path = os.path.join(os.getcwd(),'labels')
    if not os.path.exists(save_label_path):
        os.mkdir(save_label_path)
    save_txt_file_name = os.path.join(save_label_path,str(frameid)+".txt")
    box = xywh_cxyrxy(frameid,bbox)
    labeldoc = str(0)+' '+str(box[0][0])+' '+str(box[0][1])+' '+str(box[0][2])+' '+str(box[0][3])+'\n'
    print(labeldoc)
    with open(save_txt_file_name,'a',encoding = 'utf-8') as f:
        f.write(labeldoc)
        f.close()
        # f.write(labeldoc)

def readlist(file): # 372,person,3,671,407,41,76 txt datafile and source bbox test
    diclist = []
    frameid = []  # ['1005', 'person', '7', '270', '408', '101', '139']
    # dic ={}
    classid = [] 
    pid = []
    bbox = []
    f=open(file)
    # n = 0
    listlabel = f.readlines()
    for lines in listlabel:
        dic = {}
        lines = lines.replace('\n','')
        sepmark = lines.split(',')
        # if(n<2):
        #     print(lines)
        #     n = n+1
        # print(sepmark[0])
        frameid.append(sepmark[0])
        classid.append(sepmark[1])
        pid.append(sepmark[2])
        bbox.append((sepmark[3],sepmark[4],sepmark[5],sepmark[6]))
        dic["frameid"] = str(sepmark[0])
        dic["classid"] = sepmark[1]
        dic["pid"] = sepmark[2]
        dic["bbox"] = [sepmark[3],sepmark[4],sepmark[5],sepmark[6]]
        
        diclist.append(dic)
    return frameid,classid,pid,bbox,diclist
if __name__=="__main__":
    file = "./Labelfile/camera01/oneevening.txt"
    videopath = "./Videodata/oneevening.mp4"
    frameid,classid,pid,bbox,diclist = readlist(file)
    processVideo(videopath,frameid,diclist)
    # for i in range(100):
    #     print(frameid[i])
    #     print(diclist[i])

    # print(len(frameid),len(diclist))

'''
none for using 
'''
# def select_frame(framelist,classid,pid,bbox):
#     label_YOLO_save_path = os.path.join(os.getcwd(),"labels")
#     for i in range(len(framelist)):
#         if not os.path.exists(label_YOLO_save_path):
#             os.mkdir(label_YOLO_save_path)
#         label_txt_file = os.path.join(label_YOLO_save_path,str(i)+".txt")
#         with open(label_txt_file,'a',encoding='utf-8') as f:
#             # write_txt_label = id ,bbox
#             f.write(text)
#     return 0



# def crop_img (pid,cameraid,serid,frame_file,frameid,bboxs): # crop the image set in the same folder
#     # n = 0
#     for i in range(len(bboxs)):
#         bbox = bboxs[i]
        
#         x1 = int(bbox[0])
#         y1 = int(bbox[1])
#         w = int(bbox[2])
#         h = int(bbox[3])
#         x2 = x1 + w
#         y2 = y1 + h
#         # n= n+1
#     # print(n)
#         sourceimg = cv2.imread(os.path.join(frame_file,frameid[i]+".jpg"))
#         # print(sourceimg.shape)
#         afcrop_img = sourceimg[y1:y2, x1:x2]
#         namepath = str(pid[i])+"_"+"c"+str(cameraid)+"s"+str(serid)+"_"+str(frameid[i])+"_"+"00"+".jpg"
#         crop_save_path = os.path.join(os.getcwd(),"cropimage")
#         if not os.path.exists(crop_save_path):
#             os.makedirs(crop_save_path)
#         crop_save_in_folder = os.path.join(crop_save_path,namepath)
#         cv2.imwrite(crop_save_in_folder,afcrop_img)
#         if (i - 20 == 0 ):
#             print("is running")
#             print(crop_save_path)
#             break
#     return 0

# def crop_img_sep (pid,cameraid,serid,frame_file,frameid,bboxs): # crop the image set in the same folder
#     # n = 0
#     for i in range(len(bboxs)):
#         bbox = bboxs[i]
        
#         x1 = int(bbox[0])
#         y1 = int(bbox[1])
#         w = int(bbox[2])
#         h = int(bbox[3])
#         x2 = x1 + w
#         y2 = y1 + h
#         # n= n+1
#     # print(n)
#         sourceimg = cv2.imread(os.path.join(frame_file,frameid[i]+".jpg"))
#         # print(sourceimg.shape)
#         afcrop_img = sourceimg[y1:y2, x1:x2]
#         namepath = str(pid[i])+"_"+"c"+str(cameraid)+"s"+str(serid)+"_"+str(frameid[i])+"_"+"00"+".jpg"
#         crop_save_path = os.path.join(os.getcwd(),"sepimage")
#         sep_img_path = os.path.join(crop_save_path,str(pid[i]),str(cameraid))
#         if not os.path.exists(crop_save_path):
#             os.makedirs(crop_save_path)
#         if not os.path.exists(sep_img_path):
#             os.makedirs(sep_img_path)

#         crop_save_in_folder = os.path.join(sep_img_path,namepath)
#         cv2.imwrite(crop_save_in_folder,afcrop_img)
#         if (i % 20 == 0 ):
#             print("is running")
#             print(crop_save_in_folder)
#             # break
#     return 0


# def read_frame (cameraid,serid,frame_file,label_file):
#     framelist = os.listdir(frame_file) 
#     imagepath = os.path.join(frame_file,framelist[0])
#     labellist  = os.listdir(label_file)
#     img = cv2.imread(imagepath)
#     height,width = img.shape[:2]
#     for file in labellist: #this is the folder and contain the label txt
#         file = os.path.join(label_file,file)
#         # print(file)
#         frameid,classid,pid,bbox = readlist(file)
#     # print(len(bbox[0]))
#     bbox = xywh(bbox,width,height)    # print(type(frameid))
#         # for id in frameid:
#         #     # print(type(id))
#         #     crop_img(id,pid,bbox)
#     # crop_img(pid,cameraid,serid,frame_file,frameid,bbox) 
#     #pid,cameraid,serid,frame_file,frameid,bboxs
#     crop_img_sep(pid,cameraid,serid,frame_file,frameid,bbox)
#     # if you wanna sep the id cameraid serial id 
#     return 0    
# def convert(frameid,classid,bbox):
#     if classid =="person":
#         cid = 0
#     images_save_path = os.path.join(root,"VOC","images")
#     label_save_path = os.path.join(root,"VOC","labels")
#     if not os.path.exists(images_save_path):
#         os.makedirs(images_save_path)
#     if not os.path.exists(label_save_path):
#         os.makedirs(label_save_path)
#     rangelist = range(1,len(frameid))
#     # select_frame=random.sample(rangelist,int(len(frameid)/25))
#     select_frame = random.sample(rangelist,2)
#     for ilist in select_frame:
#         # print(ilist)
#         movepath = os.path.join(images_save_path,frameid[ilist]+".jpg")
#         img = cv2.imread(os.path.join(root,'oneevening',frameid[ilist]+".jpg"))
#         cv2.imwrite(movepath,img)
#         labelpath = os.path.join(label_save_path,frameid[ilist]+".txt")
#         # the string wanna to write in :
#         height,width = img.shape[:2]
#         ratioheight = int(bbox[ilist][3])/height
#         ratiowidth = int(bbox[ilist][2])/width
#         ratiox = int(bbox[ilist][0])/width
#         ratioy = int(bbox[ilist][1])/height
#         formatstring = str(0)+" "+str(ratioy)+" "+str(ratiox)+" "+str(ratiowidth)+" "+str(ratioheight)
#         with open(labelpath,"a") as f:
#             f.write(formatstring+"\n")
#             f.close()
#     return 0
# def convert2VOC(frame_file,label_file): # set the abs dir to frame_file
#     framelist = os.listdir(frame_file) 
#     imagepath = os.path.join(frame_file,framelist[0])
#     labellist  = os.listdir(label_file)
#     img = cv2.imread(imagepath)
#     height,width = img.shape[:2]
#     for file in labellist: #this is the folder and contain the label txt
#         file = os.path.join(label_file,file)
#         # print(file)
#         frameid,classid,pid,bbox = readlist(file)
#     # print(len(bbox[0]))
#     bbox = xywh(bbox,width,height)
#     convert(frameid,classid,bbox)
#         # print(type(frameid))
#     return 0

# if __name__=='__main__':
#     Videodatasource = "Videodata" # this filename is the set of video file
#     Labeldatafile = "Labelfile" # this folder saves the labelfile 
   
#     root = os.getcwd() # get the root dir
   
#     CamID = 0 # this is the pre set of camid
#     SerID = 0 # this is the pre set of same camid and different serial  
   
#     videolist = os.listdir(os.path.join(root,Videodatasource)) #return the list  of video's name
    
#     cameralist = os.listdir(os.path.join(root,Labeldatafile)) #return the list of camera marklabel folder
    
#     # for videoname in videolist:
#     #     print(os.path.join(root,Videodatasource,videoname))
#     #     processVideo(os.path.join(root,Videodatasource,videoname)) # write this video to frame
#         # and this video's frame will save in the this folder root/videoname/
#     for cameraID in cameralist: # this will return cameraID
#         CamID = CamID+1 # return the number of camera id use to set the jpg's name
#         # print(CamID) 
#         # print(os.path.join(root,Labeldatafile,cameraID))
#         label_folder = os.path.join(root,Labeldatafile,cameraID)
#         print(label_folder)
#         sam_Cam_serial_list = os.listdir(label_folder)
#         # this will return the videoname.txt
#         SerID = 0
#         for sam_Cam_serial_Labelfile in sam_Cam_serial_list:
#             SerID = SerID+1
#             file = os.path.join(root,Labeldatafile,cameraID,sam_Cam_serial_Labelfile)
#             video_frame_save_folder_name = (file.split('\\')[-1]).split('.')[0] 
#             # this return the frame save data folder
#             frame_data_file = os.path.join(root,video_frame_save_folder_name) 
            
#             # this dir is contain the sum of frame
#             # read_frame(CamID,SerID,frame_data_file,label_folder)

#             convert2VOC(frame_data_file,label_folder)
#             # f.open(file)