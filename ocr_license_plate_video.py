import cv2
from anpr import PyImageSearchANPR

def cleanup_text(text):
	# strip out non-ASCII text so we can draw the text on the image
	# using OpenCV
	return "".join([c if ord(c) < 128 else "" for c in text]).strip()

cap = cv2.VideoCapture('a.mp4')
anpr = PyImageSearchANPR(minAR=3.5,maxAR=6)

while (cap.isOpened()):
    ret,img = cap.read()

    if ret == True:
        # cv2.imshow('Orginal Video', img)

        if(cv2.waitKey(25) & 0xFF == ord('q')):
            break
        (lpText, lpCnt) = anpr.find_and_ocr(img)
	    
        if lpText is not None and lpCnt is not None:
            box = cv2.boxPoints(cv2.minAreaRect(lpCnt))
            box = box.astype("int")
            cv2.drawContours(img, [box], -1, (0, 255, 0), 2)

            (x, y, w, h) = cv2.boundingRect(lpCnt)
            cv2.putText(img, cleanup_text(lpText), (x, y - 15),
                cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

        # show the license number in the original video    
        cv2.imshow('Video', img)
    
    else:
        break


cap.release()
cv2.destroyAllWindows()