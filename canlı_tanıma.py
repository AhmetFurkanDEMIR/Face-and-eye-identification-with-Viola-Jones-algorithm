
#Çalıştırdıktan sonra programı kapatmak için "Q" tuşuna basın.


import cv2

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


# Webcam ile tanıma yapılıyor.
# Eğer bilgisayarınızda birden fazla kamera bağlıysa 0'ı 1 yapabilirsiniz.
video_capture = cv2.VideoCapture(0)
while True:
    _, frame = video_capture.read()
    canvas = detect(frame)
    cv2.imshow('Video', canvas)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()