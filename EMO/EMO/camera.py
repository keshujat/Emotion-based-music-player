

# from tensorflow.python.keras.models import load_model
# from tensorflow.python.keras.preprocessing.image import img_to_array
# from time import sleep
# from tensorflow.python.keras.preprocessing import image
# import cv2
# import numpy as np

# face_classifier = cv2.CascadeClassifier(f'{cv2.data.haarcascades}haarcascade_frontalface_default.xml')
# classifier =load_model(r'E:\music_emo\EMO\EMO\model.h5')

# emotion_labels = ['Angry','Disgust','Fear','Happy','Neutral', 'Sad', 'Surprise']

# cap = cv2.VideoCapture(0)

# emotion_count = [0,0,0,0,0,0,0]

# while True:
#     _, frame = cap.read()
#     labels = []
#     gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     faces = face_classifier.detectMultiScale(gray)

#     for (x,y,w,h) in faces:
#         cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
#         roi_gray = gray[y:y+h,x:x+w]
#         roi_gray = cv2.resize(roi_gray,(48,48),interpolation=cv2.INTER_AREA)



#         if np.sum([roi_gray])!=0:
#             roi = roi_gray.astype('float')/255.0
#             roi = img_to_array(roi)
#             roi = np.expand_dims(roi,axis=0)

#             prediction = classifier.predict(roi)[0]
#             label=emotion_labels[prediction.argmax()]
#             label_position = (x,y)
#             cv2.putText(frame,label,label_position,cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
#         else:
#             cv2.putText(frame,'No Faces',(30,80),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
#     cv2.imshow('Emotion Detector',frame)
#     if cv2.waitKey(1)  == ord('q'):
#         print(label)
#         break
       

# cap.release()
# cv2.destroyAllWindows() 


from tensorflow.python.keras.models import load_model
from tensorflow.python.keras.preprocessing.image import img_to_array
from time import sleep
from tensorflow.python.keras.preprocessing import image
import cv2
# import imutils
from imutils.video import VideoStream

from django.conf import settings
import numpy as np

face_classifier = cv2.CascadeClassifier(f'{cv2.data.haarcascades}haarcascade_frontalface_default.xml')
classifier =load_model(r'E:\music_emo\EMO\EMO\model.h5')

emotion_labels = ['Angry','Disgust','Fear','Happy','Neutral', 'Sad', 'Surprise']

cap = cv2.VideoCapture(0)

emotion_count = [0,0,0,0,0,0,0]

class VideoCamera(object):
	def __init__(self):
		self.video = cv2.VideoCapture(0)

	def __del__(self):
		self.video.release()

	def get_frame(self):         
            _, frame = cap.read()
            labels = []
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            faces = face_classifier.detectMultiScale(gray)

            for (x,y,w,h) in faces:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
                roi_gray = gray[y:y+h,x:x+w]
                roi_gray = cv2.resize(roi_gray,(48,48),interpolation=cv2.INTER_AREA)



                if np.sum([roi_gray])!=0:
                    roi = roi_gray.astype('float')/255.0
                    roi = img_to_array(roi)
                    roi = np.expand_dims(roi,axis=0)

                    prediction = classifier.predict(roi)[0]
                    label=emotion_labels[prediction.argmax()]
                    label_position = (x,y)
                    cv2.putText(frame,label,label_position,cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
                else:
                    cv2.putText(frame,'No Faces',(30,80),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
            cv2.imshow('Emotion Detector',frame)
            if cv2.waitKey(1)  == ord('q'):
                return label
            else:
                frame_flip = cv2.flip(frame,1)
                ret,jpeg = cv2.imencode('.jpg',frame_flip)
                return jpeg.tobytes()
            cap.release()
            cv2.destroyAllWindows() 
    
