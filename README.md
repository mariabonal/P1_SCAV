# Lab 1 SCAV 
#### Maria Bonal ✨
In this repository you can find the scripts ``rgb_yuv.py``, ``run-length.py`` and ``dct.py``, that are the scripts forthe exercises 1, 4 and 5 respectively. The code of these exercises is commented inside the script. You can also find a folder _images_ which contain the resulting images for exercises 2 and 3 as well as the command lines executed.  We will comment here the results for these exercises.

#### Exercise 2
The ffmpeg allows us to resize the image Lenna, which has a size of 512x512, to any other size. We decided to change it to 320x240. The command line can be found in image resize\_commandlines. The result looks pretty good, it can be found in the folder _images_ and it is called Lenna_320x240.png. 

#### Exercise 3 
The ffmpeg allows us to transform the image Lenna into b/w. To do this, we execute the command line that can be found in bw\_commandlines and we get the image Lenna\_bw.png. Then, we need to apply the hardest compression to it. We apply the command lines that can be found in compress\_commandlines.png and the result can be seen in Lenna\_bw\_compressed.png. The Lenna.png image weights 474KB. After applying the transformation to Black and White and compressing it, the final image weights 214KB. 
