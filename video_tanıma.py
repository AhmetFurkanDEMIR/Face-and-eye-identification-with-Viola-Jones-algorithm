import cv2
import imageio #videoları resimlere böler.

face_data = cv2.CascadeClassifier("face_data.xml") #Cascade leri dahil ettik

eye_data = cv2.CascadeClassifier("eye_data.xml")
 
# bu iki Cascade sayesinde hem yüz hemde göz tesbiti yapacağız.

def detect(frame): # girdi olarak resim alır. çıktı olarak kare çizer
    
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # aldığımız resmi siyah beyaza çevirdik.
    
    faces = face_data.detectMultiScale(gray, 1.3, 5) # burada resmi verdik ve resmi ne kadar küçülteceğimizi verdik, birde minumum komşu sayısı
    # geri dönen değer ise 4 elemanlı tuple, dikdörtgen çizmek için gerekli olan kordinatlar.
    
    for(x, y, w, h) in faces:
        
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2) #dikdörtgen çizme aşaması.
        # ilk olarak orjinal resmi verdik, 2. olarak dikdörtgenin sol üst noktası, 3. olarak dikdörtgenin sağ aşağı noktalarının kordinantlarını verdik. 
        # 4. parametre ise çizilen dikdörtgenin rengi. 5. paremetre ise dikdörtgenin kalınlığı, pixel sayısı
        
        gray_face = gray[y:y + h, x:x + w] #siyah beyaz resim üzerindeki yüzün boyutunu aldık
        color_face = gray[y:y+h, x:x+w] #renkli resim üzerindeki yüzün boyutunu aldık
        
        eyes = eye_data.detectMultiScale(gray_face, 1.1, 3) #14. satırda yaptığımız işlevi burdada yaptık
        
        for (ex, ey, ew, eh) in eyes:
            
            cv2.rectangle(color_face, (ex,ey), (ex+ew, ey+ew), (0,255,0), 1) #19. satırda yaptığımız işlevi burdada yaptık
            
            
    return frame


reader = imageio.get_reader("1.mp4") #videoyu çağırdık

fps = reader.get_meta_data()['fps'] # videomuzdaki fps

writer = imageio.get_writer("output.mp4", fps=fps) # ilk paremetre çıkış videosu, 2. parametre fps

for i, frame in enumerate(reader): #2 değişken alır. 1. si sayaç yani i. 2. si işlenecek olan değişkenin kendisi
    
    frame = detect(frame)
    
    writer.append_data(frame) # dikdötenlerin çizilmiş halini output videosuna ekledik
    
    print(i)
    
writer.close()
    
    






            
        
        
        