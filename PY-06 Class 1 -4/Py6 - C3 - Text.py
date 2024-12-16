from exceedCV import google_CV as cv
#from google.cloud import vision_v1
#from google.cloud.vision_v1 import types
import cv2

#google auth
j_path = "vision-project-207707-f84d39ceed76.json"
cv.google_auth(j_path)
path = 'stopsign.jpg'
p = cv.detect_properties(path)
texts,refPT = cv.detect_text(path)
i = 0
for t in texts:
    if t.description == 'STOP':
        print('There is a stop sign')
    print(t.description)
cv.display_allborders(refPT, path)

for info in p.dominant_colors.colors:
    color = cv.get_colorInfo(info)
print(p.dominant_colors.colors)
