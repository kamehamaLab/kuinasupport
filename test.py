import cv2

path = "images/dataset/0/0-0"
for i in range(4):
    img = cv2.imread(path+".jpg") # pathは画像を置いている場所を指定
    img_blur = cv2.GaussianBlur(img, (3, 3), 4)
    cv2.imwrite(path +  "-g4-" + str(i) + ".jpg", img_blur)
print("ok")
