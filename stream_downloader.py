import cv2
import numpy as np

def download_stream(url, outpath, num_frames):
    
    #create the webcam capture
    capture = cv2.VideoCapture(url)
    
    if not capture.isOpened():
        print("Unable to read stream")
        return
    
    ret_initial, image_initial = capture.read()

    #get the shape of the numpy array for creating the video writer
    input_shape = image_initial.shape

    print("Video Size: " + str(input_shape))

    #create video writer
    video = cv2.VideoWriter(outpath, cv2.VideoWriter_fourcc('M','J','P','G'), 10, (input_shape[1], input_shape[0]))

    video.write(image_initial)

    i = 1

    #while loop since webcameras may run slower than the video can be encoded, will on increment on a successful
    #read of the capture
    while i < num_frames:
        ret, img = capture.read()
            
        if img is not None:
            print(i)
            video.write(img)

            i += 1
        else:
            print("Dropped Frame")


    #free up the captures and writers
    video.release()
    capture.release()
    cv2.destroyAllWindows()

    return
