# Ask user to input an image and convert it into grey coloured image also ask the user whether it want to resize the image or not and then save that image

# Importing the library

import cv2

path = input("Input the path of the image: ")
print("Do you want to resize the image (Y/N): ")
opt = input()

# Reading the image in grayed color form
img = cv2.imread(path, 0)

# Based on condition
if(opt == "Y"):
    width = int(input("Width: "))
    height = int(input("Height: "))
    cv2.resize(img, (width, height))
elif(opt == "N"):
    cv2.resize(img, (300, 300))

# Show image
cv2.imshow("Grayed color image", img)

# Save the image
key = cv2.waitKey(0)
if(key == ord("s")):
    cv2.imwrite("F:\SYB.Sc.IT\Data Structures\Image processing\output.png", img)
else:
    cv2.destroyAllWindows()
