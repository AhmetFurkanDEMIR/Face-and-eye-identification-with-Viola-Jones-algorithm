import cv2
import imageio

face_data = cv2.CascadeClassifier("face_data.xml") #Cascade leri dahil ettik

eye_data = cv2.CascadeClassifier("eye_data.xml")

# Tanıma yapacak fonksiyon, detayları video_tanıma.py de anlattım
def detect(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_data.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_data.detectMultiScale(roi_gray, 1.1, 3)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
    return frame

# Proje klasörü içerisindeki image.jpg dosyasında yüz ve göz tesbiti yapılıyor.
# Daha sonra output.jpg dosyasına yazılıyor.
image = imageio.imread('1.jpeg')
image = detect(frame=image)
imageio.imwrite('output.jpg', image)
