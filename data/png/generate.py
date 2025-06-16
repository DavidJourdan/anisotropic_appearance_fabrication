import cv2
import numpy as np

width=1024
height=1024
img_array = np.zeros((height, width))

lambda1 = 0.99
lambda2 = 0.94
radius = width/2
K_min = -4 * lambda1 / (lambda1 + lambda2) * (1 / lambda2**2 - 1 / lambda1 ** 2) / radius**2 + 1e-6
K_max = 4 * lambda2 / (lambda1 + lambda2) * (1 / lambda2**2 - 1 / lambda1 ** 2) / radius**2 - 1e-6

def director_angle(r, K, lambda1, lambda2):
  # print(-K / (1/lambda1**2 - 1/lambda2**2) * r**2 / 2 - (lambda2 - lambda1) / (lambda1 + lambda2))
  return 0.5 * np.acos(-K / (1/lambda1**2 - 1/lambda2**2) * r**2 / 2 - (lambda2 - lambda1) / (lambda1 + lambda2))


for i in range(height):
  for j in range(width):
    theta = np.atan2(i - height / 2, j - width / 2)
    theta += director_angle(np.sqrt((i - height / 2)**2 + (j - width / 2)**2), K_max, lambda1, lambda2)
    img_array[i, j] = (-theta * 256 / np.pi) % 256

cv2.imwrite('radial_pattern.png', img_array)

# cd data/png ; python generate.py ; cd ../..
# python3 tools/fill_2d_shape.py data/circle.json
# python3 tools/togcode.py data/circle.json Prusa_MK3S -nw 0.6 -s 70 -fm 0.95 -lc 3 -bt 0