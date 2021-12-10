from deepface import DeepFace
import face_recognition
import os, glob

image = "./picture.png"
image_db = glob.glob('./Images/*.*g')

def deep_face(known,unknown):
    result = DeepFace.verify(known,unknown, "ArcFace")
    a = list(result.values())[0]
    if a == True:
        name= known.split("\\")[-1]
        print(f'You are WELLCOME {name.split(".")[0]} ')
        print(result)
    return a

def face_recog():
        print('==============================')
        known_image = face_recognition.load_image_file(image)
        if face_recognition.face_encodings(known_image):
            biden_encoding = face_recognition.face_encodings(known_image)[0]
            for i in image_db:
                unknown_image = face_recognition.load_image_file(i)

                if face_recognition.face_encodings(unknown_image):
                    print(i)
                    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

                    results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
                    if results[0] == True:
                        print(f"You are Wellcome {i}")
                        break
                else:
                    print('========= deep+face_rec  ===========')
                    if deep_face(image,i):
                       break
            else:
                print('no image matched')

        else:# check with deepface
            print('========= deep  ===========')
            for i in image_db:
                if deep_face(image,i):
                    break
            else:
                print('no image matched')

face_recog()
