from SimpleGraphics import*
# from cvsaver import*
import numpy as np
import cv2
bg=loadImage("spritesheet.gif")
bgW=int(getWidth(bg)) #calculate the width of the background
bgH=int(getHeight(bg))
resize(bgW,bgH)
bgX = int(getWidth() / 2 - bgW / 2) #x coordinate for it to be centered
bgY = int(getHeight() / 2 - bgH / 2)#y coordinate for it to be centered
drawImage(bg, bgX,bgY)

run=True
a=[]
sno=0
array=[]
click=False
while run:
	if leftButtonPressed() and click==False:
		x1,y1=mousePos()
		print(x1,y1)
		a=[]
		sno+=1
	if leftButtonPressed()==False and click==True:
		x2,y2=mousePos()
		print(x2,y2)

		for y in range(y1, y2):
			for x in range(x1, x2):
				r, g, b = getPixel(bg, x, y)
				array.append([b,g,r])
			a.append(array)
			array=[]
		rect(x1,y1,(x2-x1),(y2-y1))
		aa =cv2.UMat(np.array(a, dtype=np.uint8))
		cv2.imwrite(('sprite/sprite'+str(sno)+'.jpg'), aa.get())
		print(aa.get())
		cv2.imshow('Image', aa.get())
	click=leftButtonPressed()
	update()
if run==False:
	sys.exit()
