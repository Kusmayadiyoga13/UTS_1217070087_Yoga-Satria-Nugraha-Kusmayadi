import cv2

image = cv2.imread('kucing.jpg')
height, width = image.shape[:2]
print("Resolusi Gambar (Lebar x Tinggi):", width, "x", height)
file_size = image.size
print("Ukuran Data Media Penyimpanan (bytes):", file_size)
image_type = image.dtype
print("Tipe Data Gambar:", image_type)
