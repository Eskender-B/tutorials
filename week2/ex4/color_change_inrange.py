import numpy as np
import cv2 as cv
import argparse


def color_change(input_img, input_hex, input_range, output_hex, output_img):
    
    def HEX2HSV(hex):
        hd = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,
        '8':8,'9':9,'A':10,'a':10,'B':11,'b':11,'C':12,
        'c':12,'D':13,'d':13,'E':14,'e':14,'F':15,'f':15}
        try:
            if(len(hex)>6):
                raise KeyError
            r = hd[hex[0]]*16 + hd[hex[1]]
            g = hd[hex[2]]*16 + hd[hex[3]]
            b = hd[hex[4]]*16 + hd[hex[5]]
        except KeyError:
            exit('ERROR: Invalid HEX value')
        return cv.cvtColor(np.array([b,g,r], dtype=np.uint8).reshape(1,1,3), cv.COLOR_BGR2HSV).flatten()
    
    
    img = cv.imread(input_img, cv.IMREAD_UNCHANGED)
    hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)

    i_hsv = HEX2HSV(input_hex)
    o_hsv = HEX2HSV(output_hex)

    i_hsv = i_hsv.astype(np.int32)
    change = np.array(input_range, dtype=np.int32)
    i_hsv_L = i_hsv - change
    i_hsv_U = i_hsv + change
    i_hsv_L = i_hsv_L.clip(0,255).astype(np.uint8)
    i_hsv_U = i_hsv_U.clip(0,255).astype(np.uint8)

    thresh = cv.inRange(hsv, i_hsv_L, i_hsv_U)

    """
    ### Contour detection. 
    ## Accept contours that meet minimum area or minimum length criteria
    thresh2 = np.zeros(thresh.shape, np.uint8)
    contours, h = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cnts = []
    area_t = 500
    perim_t = 50
    for i in range(len(h[0])):
        
        if h[0][i][-1] == -1:
            area = cv.contourArea(contours[i])
            p = cv.arcLength(contours[i], False)
            #print(area, p)
            if area >= area_t or p > perim_t:
                cnts.append(contours[i])
                cv.drawContours(thresh2, [contours[i]], 0, 255,-1)

    thresh = cv.bitwise_and(thresh, thresh2)          
    #cv.drawContours(img, cnts, -1, [0,0,255],3)
    #cv.imwrite('contours.png', img)
    #cv.imwrite('contours_f.png', thresh2)
    """

    ####
    disc = cv.getStructuringElement(cv.MORPH_ELLIPSE,(17,17))
    cv.filter2D(thresh,-1,disc,thresh)

    # threshold
    ret,thresh = cv.threshold(thresh,50,255,0)

    # replace hue with chosen color
    hsv[:,:,0] = np.where(thresh==255, o_hsv[0] ,hsv[:,:,0])

    img_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)

    if img.shape[-1] == 4:
        img_bgr = np.dstack([img_bgr, img[:,:,3]])
    cv.imwrite(args.output, img_bgr)

    #cv.imwrite("mask.png", thresh)



parser = argparse.ArgumentParser()
parser.add_argument("input", type=str, help="Input image to change color")
parser.add_argument("--input_hex", default='00b274', type=str, help='color to change')
parser.add_argument("--output_hex", default='C17A00', type=str, help="target Hue value")
parser.add_argument("--output", "-o", default='output.png', type=str, help="Output image file")
args = parser.parse_args()
print(args)


# Call function
color_change(args.input, args.input_hex, [5,120,50], args.output_hex, args.output)