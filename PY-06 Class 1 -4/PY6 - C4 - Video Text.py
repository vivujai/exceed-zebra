from exceedCV import google_CV as cv
import cv2
j_path = "vision-project-207707-f84d39ceed76.json"
cv.google_auth(j_path)
#pathlist = ["LP1.jpg",'LP2.jpg','LP3.jpg','lp4.jpg']
#for x in range(4):
pathlist = ['L1.png','L2.png']
for path in pathlist:
    img = cv2.imread(path, -1)
    (yD, xD, rgb) = img.shape
    sub_amount = yD/8
    new_bottom = yD - sub_amount
    new_top = sub_amount*3
    new_slice = img[int(new_top):int(new_bottom),0:xD]
    texts,refPt=cv.detect_text(new_slice)
    t = texts[0]
    if t.description[0].isalpha() ==  True and t.description[1].isalpha() == True and len(t.description) <= 7:
        print(f"{path} is valid")
        cv.display_allborders(refPt,path)
    else:
        print(f'{path} is not valid')


        #Lp2 abd lp1
        #3/8 fro top
        #1/8 from bottom












'''for i in range(4):
            if t.description[i].isalpha():
                pass
            else:
                valid = False
                break
        if valid:
            cv.display_allborders(refPt,path)
        print(t.description)
        n+=1

        #i+=1'''
