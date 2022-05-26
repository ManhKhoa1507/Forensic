import cv2
from google.colab.patches import cv2_imshow

# load original image
original = cv2.imread('./pikachu.png', cv2.COLOR_BGR2RGB)

# loaded coded image
coded = cv2.imread('/pikachu_hide.png', cv2.COLOR_BGR2RGB)
 
# subtract two
diffrence = cv2.subtract(original, coded)

# get the result
cv2_imshow(diffrence)