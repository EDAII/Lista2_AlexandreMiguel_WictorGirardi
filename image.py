import cv2
import random
import numpy as np



img = cv2.imread('arya.jpeg')
cv2.imshow('Arya, The Cat', img)
linhas = len(img)
colunas = len(img[0])
new_image = np.empty([linhas, colunas, 3], dtype="uint8")
img_tuples = []
img_random_tuples = []
for i in range(linhas):
    line_tuple = []
    for j in range(colunas):
        line_tuple.append((j, img[i][j]))
    img_tuples.append(line_tuple)

for i in range(linhas):
    line_tuple = img_tuples[i]
    random.shuffle(line_tuple)
    img_random_tuples.append(line_tuple)

for i in range(linhas):
    line = np.empty([colunas, 3], dtype="uint8")
    for j in range(colunas):
        line[j] = img_random_tuples[i][j][1]
    new_image[i] = line


# print('linhas: ' + str(linhas) + '\ncolunas: ' + str(colunas))
# print(img)
# print(new_image)
cv2.imshow('Something', new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()



def selection_sort(rand_tuples):
    return
