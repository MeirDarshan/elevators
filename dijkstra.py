import cv2
import matplotlib.pyplot as plt
import numpy as np
import heapq as heap

#%%
file = '/home/mefathim/הורדות/KD_Mazes_ST_v1-18.jpg'
# file = '/home/mefathim-tech-25/Downloads/maze5.jpg'
#%%

img = cv2.imread(file) # read an image from a file using
cv2.circle(img,(5,220), 3, (255,0,0), -1) # add a circle at (5, 220)
cv2.circle(img, (25,5), 3, (0,0,255), -1) # add a circle at (5,5)
plt.figure(figsize=(7,7))
plt.imshow(img) # show the image
img = cv2.imread(file)
plt.show()
#%%
# print(type(img))
# print(img.shape)
# w,h, _ = img.shape
# print (f"width: {w}")
# print (f"height: {h}")
# print(img[344, 445, 2])

#%%
# Your Code Should Be Here


path = ...

def drawPath(img,path, thickness=1):
    '''path is a list of (x,y) tuples'''
    x0,y0=path[0]
    for vertex in path[1:]:
        x1,y1=vertex
        cv2.line(img,(y0,x0),(y1,x1),(255,0,0),thickness)
        x0,y0=vertex
#%%
drawPath(img,path)
plt.figure(figsize=(7,7))
plt.imshow(img) # show the image on the screen 
plt.show()

def lock():
    img[425:428,:470] = [0,0,0]
    img[:410,497:500] = [0,0,0]

def get_distance(node, other):
    x1, y1 = node
    x2, y2 = other
    return ((x1 - x2) **2 + (y1 - y2) ** 2 ) ** 0.5
        

def get_neighbors (node, img):
    neighbors = []
    x, y =node
    w, h = img.shepe
    for dx, dy in [(1, - 1), (1, 0), (1, 1), (0, 1), (0, 0), (0, - 1), (- 1, 1), (- 1, 0), (- 1, - 1)]:
        i, j = x + dx, y + dy
        if 0 <= i < w and 0 <= j < h and img [i, j] > 200:
          neighbors.append((i, j)) 
        return neighbors

def construct_path(parnt, start, end):
    path = [end]
    curent_node = end
    while curent_node != start:
        path.append(parnt[curent_node])
        curent_node = parnt[curent_node]
    return path[::-1]    



def find_shorest_path(img, start, end):
    visited = set()
    distance = {start: 0}
    priority_queue = []
    parnt = {}
    current_node = start
    
    while current_node != end:
        visited.add(current_node)
        
        for neighbor in get_neighbors(current_node, img):
            if neighbor not in visited:
                new_dist = distance[current_node] + get_distance(current_node, neighbor)
                if neighbor not in visited or new_dist < distance[current_node]:
                    distance[neighbor] = new_dist
                    parnt[neighbor] = current_node
                    heap.heappush(priority_queue, (distance[neighbor,neighbor]))
        current_node = heap.heappop(priority_queue)[1]
    
    path = construct_path(parnt, start, end)    
    return distance[end], path

    
    
    
    
    
    