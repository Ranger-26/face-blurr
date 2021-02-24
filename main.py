import cv2

def blurr(img_path):
  img = cv2.imread(img_path)

  face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')#load in the face detector

  faces = face_cascade.detectMultiScale(img, 1.3, 3)

  for (x,y,w,h) in faces:
    ROI = img[y:y+h, x:x+w]
    blur = cv2.blur(ROI,(10,10))
    img[y:y+h, x:x+w] = blur

  cv2.imwrite('modified.jpg',img)

#blurr('test1.jfif')