# Open Source Computer Vision

# import library open cv
import cv2

# load image (simpan image dalam 1 folder dengan source sode)
img = cv2.imread('template.png', 0) # kode 0 GrayScale
# tampilkan dalam 1 windows utama
cv2.imshow('gambar saya 1', img)
# tunggu action dari user
cv2.waitKey(0)
# hapus semua windows(form) yang ada
cv2.destroyAllWindows()

# load image (simpan image dalam 1 folder dengan source sode)
img = cv2.imread('template.png', 1) # Kode 1 Color
# tampilkan dalam 1 windows utama
cv2.imshow('gambar saya 2', img)
# tunggu action dari user
cv2.waitKey(0)
# hapus semua windows(form) yang ada
cv2.destroyAllWindows()
