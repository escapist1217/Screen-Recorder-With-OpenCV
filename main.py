import numpy as np
import cv2
from PIL import ImageGrab

fourcc = cv2.VideoWriter_fourcc(*'XVID')
size=(ImageGrab.grab()).size
out = cv2.VideoWriter("OUTPUT1.avi", fourcc, 5.0, size)

while True:
    img = ImageGrab.grab()
    img_np = np.array(img)

    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    cv2.imshow("Screen", frame)
    out.write(frame)

    if cv2.waitKey(1) == 27:
     break

out.release()
cv2.destroyAllWindows()

now we need to press esc to stop this...