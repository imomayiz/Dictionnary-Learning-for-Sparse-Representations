import glob
import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread, imshow
from skimage.color import rgb2gray

def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

result_data = np.zeros(1024)
result_labels = []

for file in glob.glob('/media/talesmarra/9C8E-AD88/cifar-10-python/*'):
    dictionary = unpickle(file)
    data = dictionary[b'data']
    R = data[:,0:1024]
    G = data[:,1024:2048]
    B = data[:,2048:3072]
    rgb = np.dstack((R,G,B))
    R = data[:,0:1024]*0.2125
    G = data[:,1024:2048]*0.7154
    B = data[:,2048:3072]*0.0721
    gray = R+G+B
    result_data = np.vstack((result_data,gray))
    result_labels += dictionary[b'labels']

np.savetxt('/home/talesmarra/Desktop/Courses/Recent Advances ML/CIFAR10_data.dlm',result_data[1:])
np.savetxt('/home/talesmarra/Desktop/Courses/Recent Advances ML/CIFAR10_labels.dlm',result_labels)
