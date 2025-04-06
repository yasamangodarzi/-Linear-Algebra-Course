import numpy as np
import PIL.Image as Image

L = 50


class match_histogram:
    def __init__(self,path_1,path_2):
        self.path_1 = path_1
        self.path_2 = path_2

    def Calculate_histogram(self):
        # load img
        img_1 = np.array(Image.open(self.path_1))
        img_2 = np.array(Image.open(self.path_2))
        if len(img_1.shape) == 3:
            imag_Matrix_for_picture_1 = np.mean(img_1, axis=-1)
        else:
            imag_Matrix_for_picture_1 = img_1
        Histogram_for_image_1 = np.zeros([256])
        for XP in range(imag_Matrix_for_picture_1.shape[0]):
            for YP in range(imag_Matrix_for_picture_1.shape[1]):
                colorValue = int(imag_Matrix_for_picture_1[XP, YP])
                Histogram_for_image_1[colorValue] += 1
        Histogram_for_image_1 /= (imag_Matrix_for_picture_1.shape[0] * imag_Matrix_for_picture_1.shape[1])

        # equalize
        equalize_histogram_img_1 = np.zeros_like(Histogram_for_image_1)
        for i in range(len(Histogram_for_image_1)):
            equalize_histogram_img_1[i] = int(49 * np.sum(Histogram_for_image_1[0:i]))


        if len(img_2.shape) == 3:
            imag_Matrix_for_picture_2 = np.mean(img_2, axis=-1)
        else:
            imag_Matrix_for_picture_2 = img_2
        Histogram_for_image_2 = np.zeros([256])
        for XP in range(imag_Matrix_for_picture_2.shape[0]):
            for YP in range(imag_Matrix_for_picture_2.shape[1]):
                colorValue = int(imag_Matrix_for_picture_2[XP, YP])
                Histogram_for_image_2[colorValue] += 1
        Histogram_for_image_2 /= (imag_Matrix_for_picture_2.shape[0] * imag_Matrix_for_picture_2.shape[1])
        # equalize
        equalize_histogram_img_2 = np.zeros_like(Histogram_for_image_2)
        for i in range(len(Histogram_for_image_2)):
            equalize_histogram_img_2[i] = int(49 * np.sum(Histogram_for_image_2[0:i]))



        # match_histogram
        imag_match_histogram = np.zeros_like(imag_Matrix_for_picture_1)
        tran_hist = np.zeros_like(equalize_histogram_img_1)
        for i in range(256):
            if np.where(equalize_histogram_img_1[i] == i) >= 1:
             tran_hist[i] = equalize_histogram_img_2 [i]
        for XP in range(imag_Matrix_for_picture_1.shape[0]):
            for YP in range(imag_Matrix_for_picture_1.shape[1]):
                pixel_val = int(imag_Matrix_for_picture_1[XP, YP])
                imag_match_histogram[XP, YP] = tran_hist[pixel_val]

if __name__ == '__main__':
    img=match_histogram("./1/Reference.jpg","./1/Source.jpg")
    img.Calculate_histogram()
