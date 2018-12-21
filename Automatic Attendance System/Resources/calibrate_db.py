import sys
sys.path.insert(0,'./Resources/')
import os
import cv2
import numpy as np
from PIL import Image
import done

def main():    
    recognizer=cv2.face.LBPHFaceRecognizer_create();
    path='resources/dataset'

    def getimageswithid(path):
        imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
        faces=[]
        ids=[]
        for imagePath in imagePaths:
            faceImg=Image.open(imagePath).convert("L");
            faceNp=np.array(faceImg,'uint8')
            ID=int(os.path.split(imagePath)[-1].split('.')[1])
            faces.append(faceNp)
            ids.append(ID)
            #cv2.imshow("Calibrating", faceNp)
            cv2.waitKey(10)
        return np.array(ids), faces

    ids,faces=getimageswithid(path)
    recognizer.train(faces,ids)
    recognizer.save('/Resources/recognizer/trainingData.yml')
    cv2.destroyAllWindows()
    done.main()
    
