import cv2
p=cv2.imread("test.png")
cv2.imshow("pop",p)
print(p)
cv2.waitKey(0)
cv2.destroyAllWindows()