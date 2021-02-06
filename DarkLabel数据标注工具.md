

# DarkLabel数据标注工具说明书V0.1

## 一、解压压缩包

### 1. **新建文件夹Darklabel用于存放标注软件：**

<img src="C:\Users\hyhyj\AppData\Roaming\Typora\typora-user-images\image-20210205083122351.png" alt="image-20210205083122351" style="zoom:50%;" />

<center>图1-1 DarkLable文件</center>

### 2. **右键解压当前压缩文件**

<img src="E:\标注\2.jpg" alt="2" style="zoom:50%;" />

<center>图1-2 解压该文件
</center>

### 3. **文件样例**

<img src="C:\Users\hyhyj\AppData\Roaming\Typora\typora-user-images\image-20210205083809673.png" alt="image-20210205083809673" style="zoom:50%;" />



<center>图1-3 解压后文件样例</center>

## 二、文件目录放置

### 1. 视频文件所需放置位置

​	1.1**新建文件夹，命名为：Videodata 将其放在Darklabel同目录下**

<img src="C:\Users\hyhyj\AppData\Roaming\Typora\typora-user-images\image-20210205092644963.png" alt="image-20210205092644963" style="zoom:50%;" />

<center>图2-1 创建Videodata文件夹</center>

​	1.2**将所需标注的视频放置于该目录下，如下图所示**

<img src="C:\Users\hyhyj\AppData\Roaming\Typora\typora-user-images\image-20210205093212663.png" alt="image-20210205093212663" style="zoom:50%;" />

<center>图2-2 Videodata内视频数据集样本     

### 2. **标注文件归类**

:heavy_exclamation_mark:例：需创建一个标注文件夹，并在该文件夹下创建与摄像头个数同等的文件夹，且同一摄像头的标注文件需要同一目录下

如下图所示(如若需标注3个摄像头) 

​	2.1 **创建位于Videodata同级目录下的Labelfile文件夹**



<img src="C:\Users\hyhyj\AppData\Roaming\Typora\typora-user-images\image-20210205095053227.png" alt="image-20210205095053227" style="zoom:50%;" />

<center> 图2-3 创建Labelfile 文件夹
</center>

​	2.2 **创建Labelfile目录下的不同摄像头标注文件**

​		命名规则如下如**cam+[id]**的命名形式，如下图所示，**如若多于3个，请依次对id增加1** 



<img src="C:\Users\hyhyj\AppData\Roaming\Typora\typora-user-images\image-20210205095442711.png" alt="image-20210205095442711" style="zoom:50%;" />

<center>图2-4 Labelfile内文件</center>

​	2.3 **内部标注文件会以视频文件名为命名的txt的文件，不需手动创建仅仅示例：:heavy_exclamation_mark:需后续确认是否生成的标注文件与视频文件名相同 **

<img src="C:\Users\hyhyj\AppData\Roaming\Typora\typora-user-images\image-20210205100124937.png" alt="image-20210205100124937" style="zoom:50%;" />

<center> 图2-5 cam文件夹下标注文件</center>

##  三、视频标注使用

### 1. **打开DarkLabel.exe文件**

<img src="C:\Users\hyhyj\AppData\Roaming\Typora\typora-user-images\image-20210205084041208.png" alt="image-20210205084041208" style="zoom:50%;" />

<center>图3-1 运行DarkLabel</center>

### 2. **标注工具界面**

打开后的运行界面如下图3-2所示：

<img src="C:\Users\hyhyj\AppData\Roaming\Typora\typora-user-images\image-20210205084850824.png" alt="image-20210205084850824" style="zoom:66%;" />

<center>图3-2 Darklabel运行界面</center>

### 3. **打开所需标注视频**

<img src="C:\Users\hyhyj\AppData\Roaming\Typora\typora-user-images\image-20210205085028193.png" alt="image-20210205085028193" style="zoom:50%;" />

<center>图3-3 打开所需标注的视频</center>

**选择所需要标注的视频文件**



<img src="C:\Users\hyhyj\AppData\Roaming\Typora\typora-user-images\image-20210205085221044.png" alt="image-20210205085221044" style="zoom:50%;" />

<center>图3-4 打开视频文件 </center>

### 4. **视频标注格式设定**

**打开视频后的界面如下图3-5所示**

<img src="C:\Users\hyhyj\AppData\Roaming\Typora\typora-user-images\image-20210205085543187.png" alt="image-20210205085543187" style="zoom:50%;" />

<center>图3-5 标注界面

**需对标注样式和格式进行选择，如下图所示：（以person为例子）**	

<img src="C:\Users\hyhyj\AppData\Roaming\Typora\typora-user-images\image-20210205085934383.png" alt="image-20210205085934383" style="zoom:50%;" />

<center>图3-6 标注格式选择 
</center>



**最后标注样式设置如下:需确认如下红框内设置如图**



<img src="C:\Users\hyhyj\AppData\Roaming\Typora\typora-user-images\image-20210205090520306.png" alt="image-20210205090520306" style="zoom:50%;" />

<center>图3-7 标注格式选择

### 5. **标注使用方法**

​	5.1**标注方式框选形式如LabelImg**

​		左键按住，框选目标，如下图3-8所示



<img src="C:\Users\hyhyj\AppData\Roaming\Typora\typora-user-images\image-20210205101311918.png" alt="image-20210205101311918" style="zoom:50%;" />

<center>图3-8 框选样式
</center>



​	5.2 **按下方向键→键，会进入下一帧/或者使用Enter键进行跟踪定位到下一帧如下图3-9**

如若按下→键，则需重新标注person和上一帧对应的personid，可选择跳过**5-10帧左右重新标注**。



<img src="C:\Users\hyhyj\AppData\Roaming\Typora\typora-user-images\image-20210205102841235.png" alt="image-20210205102841235" style="zoom:50%;" />

<center>图3-9 未进行跟踪的下一帧



如若按下Enter键，则会启用追踪模式，对标注样式进行跟踪，如红色箭头所示图3-10所示，可选择跟踪样式和手动按键Enter进行自动跟踪标注，如图3-11所示：



<img src="C:\Users\hyhyj\AppData\Roaming\Typora\typora-user-images\image-20210205104932210.png" alt="image-20210205104932210" style="zoom:50%;" />

<center>图3-10 设置跟踪模式和进行预测按键



<img src="C:\Users\hyhyj\AppData\Roaming\Typora\typora-user-images\image-20210205105439961.png" alt="image-20210205105439961" style="zoom:50%;" />

<center>图3-11 对目标进行跟踪后的样式



####  :heavy_exclamation_mark:跟踪丢失问题

**可能会出现跟踪丢失的过程需对齐进行重新标注或者进行手动微调，如下图3-12所示。**



<img src="C:\Users\hyhyj\AppData\Roaming\Typora\typora-user-images\image-20210205105611991.png" alt="image-20210205105611991" style="zoom:50%;" />

<center>图3-12 自动跟踪框选丢失



**如图中person3，person2，person1进行手动调整或者删除，删除的方式为：按住shift后右键空白处可全部移除/按住shift，移动至所要调整的边框，左键对边框进行调整或者右键直接移除目标框**

**一、调整目标框**

**使用方式如下：如图shift+鼠标左键至所需调整的边框处，则对该边框进行调整，如下图3-13**

<img src="C:\Users\hyhyj\AppData\Roaming\Typora\typora-user-images\image-20210205110518850.png" alt="image-20210205110518850" style="zoom:50%;" />

<center>图3-13 调整框选大小



**二、直接删除目标框**

**使用方式如下：按住shift移入目标框内约中心位置，出现全框后进行右键，后可进行删除，如下图3-14所示：**



<img src="C:\Users\hyhyj\AppData\Roaming\Typora\typora-user-images\image-20210205111443438.png /" alt="image-20210205111443438" style="zoom:50%;" />

<center>图3-14 删除框选或框线



**三、更改personid**

**使用方式如下：按住shift后进入目标框，左键双击即可更改person的id号。**

### 6. 标注文件保存

对标注好的视频进行确认后，可进行保存，保存时需确认该视频为几号摄像头，后对该标注文件放入几号标注目录下

步骤如下选择GT Save键，如图3-15所示：

<img src="C:\Users\hyhyj\AppData\Roaming\Typora\typora-user-images\image-20210205112033075.png" alt="image-20210205112033075" style="zoom:66%;" />

<center>图3-15 标注文件保存



在打开所需的保存目录中，假设该视频为摄像头2所拍摄，则所需保存的目录应当于/Labelfile/cam2/下，如图3-16所示：



<img src="C:\Users\hyhyj\AppData\Roaming\Typora\typora-user-images\image-20210205112630574.png" alt="image-20210205112630574" style="zoom:50%;" />

<center>图3-16 标注文件保存位置



**最后会生成以视频文件名一样的txt文件，保存完毕后确认文件目录和文件名即可。**



## 四、标注暂定要求

1.标准打标personid，对于肉眼可分辨的尽可能的打标，如下图所示，对于残缺的少于整体人的60%的样本可以不打标记，如图4-1所示



<img src="C:\Users\hyhyj\AppData\Roaming\Typora\typora-user-images\image-20210205130827840.png" alt="image-20210205130827840" style="zoom:50%;" />

<center>图4-1 打标样例

2.可漏标后补标，允许不是第一时间漏标后的后续补标，可存在漏标为5-10帧。

3.对于跨摄像头(不同摄像头下的同一个人)的person，务必保证标定id正确。

4.对于标定对象仅需标定特定对象即可。



