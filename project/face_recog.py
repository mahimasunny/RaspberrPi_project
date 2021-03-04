import face_recognition
import os
import cv2

KNOWN_FACES_DIR = "./known_faces"
UNKNOWN_FACES_DIR = "./unknown_faces"
TOLERANCE = 0
FRAME_THICKNESS = 3
FONT_THICKNESS = 2
MODEL = "cnn"   #hog for cpu, cnn works slow on cpu

print("Loading known faces")

known_faces = []
known_names = []

for name in os.listdir(KNOWN_FACES_DIR):
    print(name,KNOWN_FACES_DIR)
    for filename in os.listdir(KNOWN_FACES_DIR):
        image = face_recognition.load_image_file(f"{KNOWN_FACES_DIR}/{filename}")
        # Assume the whole image is the location of the face
        height, width, _ = image.shape
        # location is in css order - top, right, bottom, left
        face_location = (0, width, height, 0)
        encoding = face_recognition.face_encodings(image, known_face_locations=[face_location])
        known_faces.append(encoding)
        print(len(encoding[0]))
        known_names.append(name)
        print(known_names)
print(len(known_faces), len(known_faces[0]))
print("processing unknown faces ")
for filename in os.listdir(UNKNOWN_FACES_DIR):
    print(filename)
    image = face_recognition.load_image_file(f"{UNKNOWN_FACES_DIR}/{filename}")
    # Assume the whole image is the location of the face
    height, width, _ = image.shape
    # location is in css order - top, right, bottom, left
    face_location = (0, width, height, 0)
    face_encoding = face_recognition.face_encodings(image, known_face_locations=[face_location])
    print(len(face_encoding[0]), len(encoding[0]))
    # print(type(face_encoding), type(known_faces))
    results = face_recognition.compare_faces(known_faces, face_encoding[0], TOLERANCE)
    print(len(results), len(results[0]))
    match = None
    print(results)
    cv2.imwrite('./output/1.jpg',image)
    res= False
    for r in results[0]:
        if r:
            res= True
            break
    if res:
        match = known_names[0]
        print(f"Match Found : {match}")
        image_out= cv2.imread('./unknown_faces/mahi2.2.jpg') 
        # font 
        font = cv2.FONT_HERSHEY_SIMPLEX 
        
        # org 
        org = (50, 200) 
        
        # fontScale 
        fontScale = 1
        
        # Blue color in BGR 
        color = (0, 0, 255) 
        
        # Line thickness of 2 px 
        thickness = 2
        
        # Using cv2.putText() method 
        image_out = cv2.putText(image_out, 'Mahima', org, font,  
                        fontScale, color, thickness, cv2.LINE_AA)
        # #Load a cascade file for detecting faces
        # face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')
        # #Convert to grayscale
        # gray = cv2.cvtColor(image_out,cv2.COLOR_BGR2GRAY)

        # #Look for faces in the image using the loaded cascade file
        # faces = face_cascade.detectMultiScale(gray, 1.1, 5)

        # print("Found "+str(len(faces))+" face(s)")

        # #Draw a rectangle around every found face
        # for (x,y,w,h) in faces:
        #     cv2.rectangle(image_out,(x,y),(x+w,y+h),(255,255,0),2)
    else:
        match = known_names[0]
        print(f"Match Found : {match}")
        image_out= cv2.imread('./unknown_faces/mahi2.2.jpg') 
        # font 
        font = cv2.FONT_HERSHEY_SIMPLEX 
        
        # org 
        org = (50, 200) 
        
        # fontScale 
        fontScale = 2
        
        # Blue color in BGR 
        color = (0, 0, 255) 
        
        # Line thickness of 2 px 
        thickness = 2
        
        # Using cv2.putText() method 
        image_out = cv2.putText(image_out, 'Unknown', org, font,  
                        fontScale, color, thickness, cv2.LINE_AA)
        #Load a cascade file for detecting faces
        face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')
        #Convert to grayscale
        gray = cv2.cvtColor(image_out,cv2.COLOR_BGR2GRAY)

        #Look for faces in the image using the loaded cascade file
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)

        print("Found "+str(len(faces))+" face(s)")

        #Draw a rectangle around every found face
        for (x,y,w,h) in faces:
            cv2.rectangle(image_out,(x,y),(x+w,y+h),(255,255,0),2)

    #Save the result image
    cv2.imwrite('./output/face_recognition.jpg',image_out)
    cv2.waitKey(0)
    # cv2.destroyWindow(filename)