import numpy as np
from tqdm import tqdm
import pandas as pd
import cv2
import os
import argparse

def list_ims(image_dir):
    return {im:os.path.join(image_dir, im) for im in os.listdir(image_dir)}

def get_annotations(annotations_csv):   
    df = pd.read_csv(annotations_csv).values
    return {i:j for [i, j] in df}

# def get_partitions(im_name, annotations):
#     output_im = np.zeros((len(annotations), 300, 300, 3), np.uint8)
#     im = cv2.imread(im_name)
#     for n,annotation in enumerate(annotations):
#         x, y, w, h = annotation
#         output_im[n, x:x+w, y:y+h, ] = 




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('image_dir')
    parser.add_argument('annotations_csv')