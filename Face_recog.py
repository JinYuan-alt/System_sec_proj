import cv2

vid = cv2.VideoCapture(0)


while (True):

    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    user=input("type 1 to escape: ")
    if user == '1':
        cv2.destroyAllWindows()# Destroy all the windows
        vid.release()# After the loop release the cap object
        break

