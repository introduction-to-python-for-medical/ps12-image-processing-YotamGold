from PIL import Image
import numpy as np
from scipy.signal import convolve2d

def load_image(path):
  image = Image.open(path)
  array_image = np.array(image)
  return array_image

def edge_detection(array_image):
  gray_image = np.mean(array_image, axis = 2)
  kernelY = np.array([[1, 2, 1],[0, 0, 0],[-1, -2, -1]])
  kernelX = np.array([[-1, 0, 1],[-2, 0, 2],[-1, 0, 1]])
  edgeY = convolve2d(gray_image, kernelY, mode = 'same')
  edgeX = convolve2d(gray_image, kernelX, mode = 'same')
  edgeMAG = np.sqrt(edgeX**2 + edgeY**2)
  return edgeMAG
