import cv2
import numpy as np

def download_stream(url, outpath, num_frames):
    
    cam = cv2.VideoCapture(url)
    
    good_stream = False

    while not good_stream:
        
        ret_1, image_1 = cam.read()
        if image_1 is not None:
            good_stream = True
            input_shape = image_1.shape
        else:
            print("Unable to read stream")
            cap.release()
            return

    print(input_shape)

    capture = video = cv2.VideoWriter(outpath, cv2.VideoWriter_fourcc('M','J','P','G'), 10, (input_shape[1], input_shape[0]))

    i = 0

    while i < num_frames:
        ret, img = cam.read()
            
        if img is not None:
            print(i)
            video.write(img)

            i += 1
        else:
            print("Dropped Frame")


    video.release()
    cam.release()
    cv2.destroyAllWindows()

    return
