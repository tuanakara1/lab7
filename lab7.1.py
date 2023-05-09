import cv2

img = cv2.imread('your_image.jpg')


blue_channel, green_channel, red_channel = cv2.split(img)


cv2.imshow('Blue Channel', blue_channel)
cv2.imshow('Green Channel', green_channel)
cv2.imshow('Red Channel', red_channel)
cv2.waitKey(0)
cv2.destroyAllWindows()

green_channel[:] = 0
red_channel[:] = 255

modified_img = cv2.merge((blue_channel, green_channel, red_channel))

cv2.imshow('Modified Image', modified_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
