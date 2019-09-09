import pandas as pd
import requests

def read_df(filename):
    return pd.read_csv(filename)

def read_images(directory):
    return {path.stem for path in directory.glob('*.png')}

def get_image(url):
    return requests.get(url).content

def save_image(img, filename):
    '''Saves image in the given filename.'''
    with open(filename, 'wb') as f:
        f.write(img)
