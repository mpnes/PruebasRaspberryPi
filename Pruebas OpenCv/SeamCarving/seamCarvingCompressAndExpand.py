import cv2
import numpy as np

def compute_energy_matrix(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    sobel_x = cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=3)
    sobel_y = cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=3)

    abs_sobel_x = cv2.convertScaleAbs(sobel_x)
    abs_sobel_y = cv2.convertScaleAbs(sobel_y)
    return cv2.addWeighted(abs_sobel_x, 0.5, abs_sobel_y, 0.5, 0)
    
def find_vertical_seam(img, energy):

    rows, cols = img.shape[ : 2]
    seam = np.zeros(rows)
    dist_to = np.zeros((rows, cols))
    dist_to[0, : ] = np.zeros(img.shape[1])
    edge_to = np.zeros(img.shape[ : 2])

    for row in range(rows - 1):
        for col in range(cols):
            if col != 0:
                if dist_to[row+1, col-1] > dist_to[row, col] + energy[row+1, col-1]:
                    dist_to[row+1, col-1] = dist_to[row, col] + energy[row+1, col-1]
                    edge_to[row+1, col-1] = 1

            if dist_to[row+1, col] > dist_to[row, col] + energy[row+1, col]:
                dist_to[row+1, col] = dist_to[row, col] + energy[row+1, col]
                edge_to[row+1, col] = 0

            if col != cols-1:
                if dist_to[row+1, col+1] > dist_to[row, col] + energy[row+1, col+1]:
                    dist_to[row+1, col+1] = dist_to[row, col] + energy[row+1, col+1]
                    edge_to[row+1, col+1] = -1

    seam[rows-1] = np.argmin(dist_to[rows-1, :])
    for i in (x for x in reversed(range(rows)) if x > 0):
        seam[i-1] = seam[i] + edge_to[i, int(seam[i])]

    return seam

def overlay_vertical_seam(img, seam):
    img_seam_overlay = np.copy(img) 
    x_coords, y_coords = np.transpose([(i,int(j)) for i,j in enumerate(seam)])
    img_seam_overlay[x_coords, y_coords] = (0,255,0)

    return img_seam_overlay

def remove_vertical_seam(img, seam):
    rows, cols = img.shape[:2]
    for row in range(rows):
        for col in range(int(seam[row]), cols-1):
            img[row, col] = img[row, col+1]

    img = img[:, 0:cols-1]
    return img

def add_vertical_seam(img, seam, num_iter):
    seam = seam + num_iter
    rows, cols = img.shape[:2]
    zero_col_mat = np.zeros((rows,1,3), dtype=np.uint8)
    img_extended = np.hstack((img, zero_col_mat))

    for row in range(rows):
        for col in range(cols, int(seam[row]), -1):
            img_extended[row, col] = img[row, col-1]

        for i in range(3):
            v1 = img_extended[row, int(seam[row])-1, i]
            v2 = img_extended[row, int(seam[row])+1, i]
            img_extended[row, int(seam[row]), i] = (int(v1)+int(v2))/2

    return img_extended

if __name__ == "__main__":
    img_input = cv2.imread("/home/pi/Desktop/Milker_robot/image8.jpg")
    num_seams = int(1) #numero de columnas que se quieren eliminar
    img_overlay_seam = np.copy(img_input)

    img = np.copy(img_input)
    #Descomentar para expandir la imagen
##    img_expanded = np.copy(img_input) 

    energy = compute_energy_matrix(img)

    for i in range(num_seams):
        seam = find_vertical_seam(img, energy)
        img_overlay_seam = overlay_vertical_seam(img_overlay_seam, seam)
        img = remove_vertical_seam(img, seam)
##        img_expanded = add_vertical_seam(img_expanded, seam, i
        energy = compute_energy_matrix(img)
        print ('Number of seams removed =', i+1)

    cv2.imshow('Input', img_input)
    cv2.imshow('Seams', img_overlay_seam)
    cv2.imshow('Smaller', img)
##    cv2.imshow('Bigger', img)
    
    cv2.imwrite("/home/pi/Desktop/imgChiquita.jpg", img)
##    cv2.imwrite("/home/pi/Desktop/imgGrande.jpg", img_expanded)

    cv2.waitKey()
    cv2.destroyAllWindows()
