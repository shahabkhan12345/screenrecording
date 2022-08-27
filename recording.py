#screen recoding ----

import cv2 as c
import pyautogui as p
import numpy as np

#create resolution
rs = p.size()

#filename in which we store recording
fn = input("Please Enter any file name and path")
#fix the frame rate
fps = 60.0

fourcc = c.VideoWriter_fourcc(*'XVID')
output = c.VideoWriter(fn,fourcc,fps,rs)


#create recording module
c.namedWindow("Live_Recording",c.WINDOW_NORMAL)
c.resizeWindow("Live_Recording",(600,400))

while True:
    img = p.screenshot()
    f = np.array(img)
    f = c.cvtColor(f,c.COLOR_BGR2RGB)
    output.write(f)
    c.imshow("Live_Recording",f)
    if c.waitKey(1) == ord("q"):
        break
    
output.release()
c.destroyAllWindows()
    