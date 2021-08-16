# import the necessary pages
import cv2
import pyautogui as pg
import numpy as np

def findMatch(template, screenshare=False):
	image = pg.screenshot()
	image = np.uint8(image)
	template = cv2.imread(template)

	# convert both the image and template to grayscale
	imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

	result = cv2.matchTemplate(imageGray, templateGray,
		cv2.TM_CCOEFF_NORMED)
	(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(result)

	if screenshare:
		return maxVal >= 0.9
	else: 
		return maxVal >= 0.75
