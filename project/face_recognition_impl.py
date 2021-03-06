import face_recognition
from PIL import Image, ImageDraw
import numpy as np
import cv2
from IPython.display import display

TOLERANCE= 0.6
def check_if_known_face(file_path):
    image = face_recognition.load_image_file("known_faces/mahima.jpg")
    face_locations = face_recognition.face_locations(image)
    face_landmarks_list = face_recognition.face_landmarks(image)

    mahima = face_recognition.load_image_file("known_faces/mahima.jpg")
    mahima_face_encoding = face_recognition.face_encodings(mahima)[0]
    kamala = face_recognition.load_image_file("known_faces/Kamala1.jpg")
    kamala_face_encoding= face_recognition.face_encodings(kamala)[0]

    known_face_encodings = [mahima_face_encoding, kamala_face_encoding]
    known_face_names = ["Mahima" , "Kamala Harris"]
    print('CHECKING FOR MATCHES IN THE KNOWN IMAGES DATASET')
    unknown_image = face_recognition.load_image_file(file_path)
    face_locations = face_recognition.face_locations(unknown_image)
    face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

    pil_image = Image.fromarray(unknown_image)
    # Create a Pillow ImageDraw Draw instance to draw
    draw = ImageDraw.Draw(pil_image)
    print(face_locations)
    print(len(face_encodings[0]))

    matches = face_recognition.compare_faces(known_face_encodings, face_encodings[0], TOLERANCE)
    # Instead, use face_distance to calculate similarities
    face_distances = face_recognition.face_distance(known_face_encodings, face_encodings[0])
    best_match_index = np.argmin(face_distances)
    name = "Unknown"
    if matches[best_match_index]:
        name = known_face_names[best_match_index]
    # # # Draw a box around the face using the Pillow module
    (t,r,b,l)= face_locations[0]
    draw.rectangle(((l, t), (r, b)), outline=(0, 0, 255))
    # Draw a label with a name below the face 
    width, height = draw.textsize(name)
    draw.rectangle(((l, b - height - 10), (r, b)), fill=(0, 0, 255),     outline=(0, 0, 255))
    draw.text((l + 6, b - height - 5), name, fill=(255, 255, 255, 255))
    pil_image.save("./output/face_recognition.jpg") 
    if name == "Unknown":
        print('Match not found')
        return False
    return True

def main():
    check_if_known_face("unknown_faces/unknown.jpg")

if __name__ == "__main__":
    main()