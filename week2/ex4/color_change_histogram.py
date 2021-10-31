import numpy as np
import cv2 as cv
import argparse


def change_color(input_image, target_hex, output_image):
    hd = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,
      '8':8,'9':9,'A':10,'a':10,'B':11,'b':11,'C':12,
      'c':12,'D':13,'d':13,'E':14,'e':14,'F':15,'f':15}

    def HEX2HSV(hex):
        try:
            if(len(hex)>6):
                raise KeyError
            r = hd[hex[0]]*16 + hd[hex[1]]
            g = hd[hex[2]]*16 + hd[hex[3]]
            b = hd[hex[4]]*16 + hd[hex[5]]
        except KeyError:
            exit('ERROR: Invalid HEX value')
        return cv.cvtColor(np.array([b,g,r], dtype=np.uint8).reshape(1,1,3), cv.COLOR_BGR2HSV).flatten()

    o_hsv = HEX2HSV(target_hex)

    # Read image
    img = cv.imread(input_image, cv.IMREAD_UNCHANGED)
    hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)

    # Read the same samples for every input image
    img = cv.imread('roi1.png')
    roi_hsv1 = cv.cvtColor(img,cv.COLOR_BGR2HSV)
    img = cv.imread('roi2.png')
    roi_hsv2 = cv.cvtColor(img,cv.COLOR_BGR2HSV)


    # calculating object histogram
    roihist1 = cv.calcHist([roi_hsv1],[0, 1], None, [180, 256], [0, 180, 0, 256] )
    roihist2 = cv.calcHist([roi_hsv2],[0, 1], None, [180, 256], [0, 180, 0, 256] )
    roihist = roihist1 + roihist2

    # normalize histogram and apply backprojection
    cv.normalize(roihist,roihist,0,255,cv.NORM_MINMAX)
    dst = cv.calcBackProject([hsv],[0,1],roihist,[0,180,0,256],1)

    # Now convolute with circular disc
    disc = cv.getStructuringElement(cv.MORPH_ELLIPSE,(21,21))
    cv.filter2D(dst,-1,disc,dst)

    # threshold
    ret,thresh = cv.threshold(dst,50,255,0)

    # replace hue with chosen color
    hsv[:,:,0] = np.where(thresh==255, o_hsv[0], hsv[:,:,0])

    img_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)

    if img.shape[-1] == 4:
        img_bgr = np.dstack([img_bgr, img[:,:,3]])
    cv.imwrite(output_image, img_bgr)



parser = argparse.ArgumentParser()
parser.add_argument("input", type=str, help="Input image to change color")
parser.add_argument("--output_hex", "-H", default='C17A00', type=str, help="target Hue value")
parser.add_argument("--output", "-o", default='output.png', type=str, help="Output image file")
args = parser.parse_args()
print(args)

# Call the function
change_color(args.input, args.output_hex, args.output)        