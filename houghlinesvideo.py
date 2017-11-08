import cv2
import numpy as np

def canny_edge(frame):
	canny = cv2.Canny(frame,50,150)
	return canny

def hough(canny):
	lines = cv2.HoughLines(canny,1,np.pi/180, 200)
	for i in range(1,2):	
		minLineLength = 10
		maxLineGap = 10
		lines = cv2.HoughLinesP(canny,1,np.pi/180,100,minLineLength,maxLineGap)
		if lines is None:
			break
		for x1,y1,x2,y2 in lines[0]:
		    cv2.line(original,(x1,y1),(x2,y2),(0,255,0),2)
	return canny

if __name__ == '__main__' :
 	video = cv2.VideoCapture(0)
  	k = cv2.waitKey(1) & 0xff
	while not k == 27:
		work, frame = video.read()
 		if not work:
			break
		original = frame
		canny = canny_edge(frame)
		houghy = hough(canny)
		original = cv2.flip(original,1)
		# Resize to fit 1080p display
		cv2.namedWindow("Video", 0);
		cv2.resizeWindow("Video", 1200,950);
		cv2.imshow("Video", original)
		# Exit if ESC pressed
		k = cv2.waitKey(1) & 0xff	