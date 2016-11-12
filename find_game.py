# import the necessary packages
# import numpy as np
import cv2
import imutils



# load the games image
vid = cv2.VideoCapture('traffic_video.mp4')
cv2.startWindowThread()

try:
	i = 0
	while True:
		grabbed, frame = vid.read()
		print(i)

		if not grabbed:
			break

		cv2.imshow('image', frame)
		cv2.waitKey(0)
		cv2.destroyAllWindows()

		frame = imutils.resize(frame, width=500)
		cv2.imshow('image', frame)
		cv2.waitKey(0)
		cv2.destroyAllWindows()

		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		cv2.imshow('image', gray)
		cv2.waitKey(0)
		cv2.destroyAllWindows()

		gray = cv2.GaussianBlur(gray, (21, 21), 0)
		cv2.imshow('image', gray)
		cv2.waitKey(0)
		cv2.destroyAllWindows()

		name = str(i) + 'test.png'
		i += 1
except KeyboardInterrupt:
	cv2.destroyAllWindows()


#
# # find the red color game in the image
# upper = np.array([65, 65, 255])
# lower = np.array([0, 0, 200])
# mask = cv2.inRange(image, lower, upper)
#
# # find contours in the masked image and keep the largest one
# (_, cnts, _) = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
# 	cv2.CHAIN_APPROX_SIMPLE)
# c = max(cnts, key=cv2.contourArea)
#
# # approximate the contour
# peri = cv2.arcLength(c, True)
# approx = cv2.approxPolyDP(c, 0.05 * peri, True)
#
# # draw a green bounding box surrounding the red game
# cv2.drawContours(image, [approx], -1, (0, 255, 0), 4)
# cv2.imshow("Image", image)
# cv2.waitKey(0)
