import cv2
import random
import numpy as np
from threading import Thread







def convert_image(img_tuple, lines, columns):
    new_image = np.empty([lines, columns, 3], dtype="uint8")
    for i in range(lines):
        line = np.empty([columns, 3], dtype="uint8")
        for j in range(columns):
            line[j] = img_tuple[i][j][1]
        new_image[i] = line
    return new_image

def convert_line(original_line):
    size = len(original_line)
    new_line = np.empty([size, 3], dtype="uint8")
    for i in range(size):
        new_line[i] = original_line[i][1]
    return new_line

def selection_sort(rand_tuples):
    size = len(rand_tuples)
    for i in range(size):
        for j in range(i+1, size):
            if rand_tuples[j][0] < rand_tuples[i][0]:
                aux = rand_tuples[i]
                rand_tuples[i] = rand_tuples[j]
                rand_tuples[j] = aux

    return rand_tuples

def bubble_sort(rand_tuples):
    #subtraimos por um para sempre compararmos com os proximos valores
    size = len(rand_tuples) - 1
    #realiza o calculo de quantas vezes vai ser necessaria
    #a passagem pelo tamanho do vetor
    for i in range(size):
        #realiza a troca de posicoes dentro dos vetores
        for j in range(size -i):
            if rand_tuples[j][0] > rand_tuples[j+1][0]:
                rand_tuples[j], rand_tuples[j+1] = rand_tuples[j+1], rand_tuples[j]
    return rand_tuples

# Como se a cada elemento encontrado, o algorítmo percorre o vetor do fim pro começo para encontrar a posição adequada de inserção
def insertion_sort(rand_tuples):
    size = len(rand_tuples)
    for index in range(1,size): # Considering that the fist element is in the right position
        current = rand_tuples[index][0] #Stablish fixed element for comparison [(**id**, RGB)]
        current_tuple = rand_tuples[index] # [**(id, RGB)**]
        position = index
        #comparing one element to the one that is behind the current element
        while  position > 0 and rand_tuples[position-1][0] > current:
           # Doing the swaping
           rand_tuples[position] = rand_tuples[position-1]
           position -= 1
        rand_tuples[position] = current_tuple #Tuple being swapped from current_tuple
    # return the sorted tupl
    return rand_tuples

# # We define our 3 arrays
#  less = []
#  equal = []
#  greater = []
#
#  # if the length of our array is greater than 1
#  # we perform a sort
#  if len(array) > 1:
#      # Select our pivot. This doesn't have to be
#      # the first element of our array
#      pivot = array[0]
#
#      # recursively go through every element
#      # of the array passed in and sort appropriately
#      for x in array:
#          if x < pivot:
#              less.append(x)
#          if x == pivot:
#              equal.append(x)
#          if x > pivot:
#              greater.append(x)
#
#      # recursively call quicksort on gradually smaller and smaller
#      # arrays until we have a sorted list.
#      return quicksort(less)+equal+quicksort(greater)
#
#  else:
#      return array

# [(id, RGB),
#  (id, RGB),
#  ...
#  (id, RGB),
#  (id, RGB)]

class Sel(Thread):

    def __init__(self, random_tuple, new_image):
        Thread.__init__(self)
        self.random_tuple = random_tuple
        self.new_image = new_image

    def run(self):
        random_tuple = self.random_tuple
        size = len(random_tuple)
        for i in range(size):
            for j in range(i+1, size):
                if random_tuple[j][0] < random_tuple[i][0]:
                    aux = random_tuple[i]
                    random_tuple[i] = random_tuple[j]
                    random_tuple[j] = aux
                    other_aux = self.new_image[i]
                    self.new_image[i] = self.new_image[j]
                    self.new_image[j] = other_aux
                    cv2.imshow('Selection Sort', self.new_image)
                    cv2.waitKey(1)



# class Bub(Thread):
#
#     def __init__(self, random_tuples):
#         Thread.__init__(self)
#         self.random_tuples = random_tuples
#
#     def run(self):
#         random_tuples = self.random_tuples
#         lines = len(random_tuples)
#         columns = len(random_tuples[0])
#         new_image = convert_image(random_tuples, lines, columns)
#         for i in range(lines-1, -1, -1):
#             tuple_line = bubble_sort(random_tuples[i])
#             converted_line = convert_line(tuple_line)
#             new_image[i] = converted_line
#             cv2.imshow('Bubble Sort', new_image)
#             cv2.waitKey(1)
#
#
# class In(Thread):
#
#     def __init__(self, random_tuples):
#         Thread.__init__(self)
#         self.random_tuples = random_tuples
#
#     def run(self):
#         random_tuples = self.random_tuples
#         lines = len(random_tuples)
#         columns = len(random_tuples[0])
#         new_image = convert_image(random_tuples, lines, columns)
#         for i in range(lines):
#             tuple_line = insertion_sort(random_tuples[i])
#             converted_line = convert_line(tuple_line)
#             new_image[i] = converted_line
#             cv2.imshow('Insertion Sort', new_image)
#             cv2.waitKey(1)



if __name__ == "__main__":
    img = cv2.imread('arya.jpeg')
    cv2.imshow('Arya, The Cat', img)

    linhas = len(img)
    colunas = len(img[0])
    new_image = np.empty([linhas, colunas, 3], dtype="uint8")
    img_tuples = []
    img_random_tuples = []

    #Create img vector with tuples information
    for i in range(linhas):
        line_tuple = []
        for j in range(colunas):
            line_tuple.append((j, img[i][j]))
        img_tuples.append(line_tuple)

    #Randomiz vector with tuples
    for i in range(linhas):
        line_tuple = img_tuples[i]
        random.shuffle(line_tuple)
        img_random_tuples.append(line_tuple)

    new_image = convert_image(img_random_tuples, linhas, colunas)
    threads = []
    for i in range(linhas):
            t = Sel(img_random_tuples[i], new_image)
            threads.append(t)

    for i in range(linhas):
        threads[i].start()
    #     tuple_line = insertion_sort(img_random_tuples[i])
    #     converted_line = convert_line(tuple_line)
    #     if i == 1:
    #         print(tuple_line)
    #     new_image[i] = converted_line
    #     cv2.imshow('Something', new_image)
    #     cv2.waitKey(1)
    #     # print('passou')

    # t1 = Sel(img_random_tuples)
    # t1.start()
    # t2 = Bub(img_random_tuples)
    # t2.start()
    # t3 = In(img_random_tuples)
    # t3.start()


    cv2.waitKey(0)
