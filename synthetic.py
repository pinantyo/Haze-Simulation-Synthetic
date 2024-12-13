import random
import os
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
from glob import glob
from PIL import Image

class HazyGenerator:
    def __init__(self, mode, size, dir_path='/kaggle/working/', is_test=False):
        self.mode = mode
        self.size = size
        self.dir_path = dir_path
        self.is_test = is_test
        
    def normalize(self, image):
        return image / 255.
    
    def augmentation(self, img):
        if random.random() > 0.5:
            k = random.randint(1, 3)
            img = np.rot90(img, k=k)
            
        if random.random() > 0.5:
            img = np.flipud(img)
            
        if random.random() > 0.5:
            img = np.fliplr(img)
        return img

    def transmission_estimation(self, haze):
        haze = self.augmentation(haze)
        w = 0.95
        t = 1.0 - w * haze
        return t
    
    def load(self, image_path, is_color=True):
        image = Image.open(image_path)

        if is_color:
            image = image.convert('RGB')

        image = np.asarray(image, dtype=np.float32)
        
        if (image.shape[0] != self.size) or (image.shape[1] != self.size) and (image.shape[0] == image.shape[1]):
            # Get min dimension
            max_dim = max(image.shape[0], image.shape[1])
            
            max_h_dim = image.shape[0]-self.size
            max_w_dim = image.shape[1]-self.size

            min_h_dim = random.randint(0, max_h_dim)
            min_w_dim = random.randint(0, max_w_dim)

            image = image[min_h_dim:min_h_dim+self.size, min_w_dim:min_w_dim+self.size]

        if len(image.shape) == 2 and is_color:
            image = np.stack((image,)*3, axis=-1)
       
        # Normalization 
        image = self.normalize(image) if is_color else (image / image.max()) # ((image - image.min()) / (image.max() - image.min()))
             
        # downsample for speedup
        return image, image_path.split("/")[-1].split(".")[0]
        
    def atmospheric_light_estimation(self, H_j):
        h, w = H_j.shape[:2]
        l = h * w

        # DCP
        DH_j = np.min(H_j, axis=-1)
        
        # BCP
        BH_j = np.max(H_j, axis=-1)
        
        # BDCP (Jackson et al., 2017)
        _H_j = (DH_j + BH_j) / 2
        _H_j = _H_j.flatten()

        # slice top 0.01% pixels
        numpx = l // 10000
        indices = np.argsort(_H_j)[-numpx:]
        sliced_H_j = _H_j[indices]
        return sliced_H_j
    
    def hazy_generator(self, clear, A, transmission):
        I = []
        
        # Channels
        for b in range(3):
            A_j = A[b+1]

            # Haze Simulation: Atmospheric Scattering Model
            I_j = clear[..., b] * transmission + A_j * (1 - transmission)   
            
            # Append channels
            I.append(I_j)
            
        # Concat as 3 channels
        I = np.stack(I, axis=-1)
        J = clear

        # Clip
        I = np.clip(I, 0, 1)
        J = np.clip(J, 0, 1)
        
        # Normalized [0, 255]
        I = (I * 255).astype(np.uint8)
        J = (J * 255).astype(np.uint8)
        
        return I, J
    
    def save_image(self, image, dir_path, modul, image_name):
        if not os.path.exists(os.path.join(dir_path, modul)):
            os.mkdir(os.path.join(dir_path, modul))
            
        image_name = f'{image_name}.png'
        file_name = os.path.join(dir_path, modul, image_name)
        plt.imsave(file_name, image)
        
    def __call__(self, cirrus_dir, clear_dir):
        for index, i in tqdm(enumerate(clear_dir)):
            # Pick random cirrus
            cirrus = cirrus_dir[random.randint(0, len(cirrus_dir)-1)]

            # Load Cirrus Image and Clear Image
            cirrus, _ = self.load(cirrus, is_color=False)
            clear, clear_name = self.load(i, is_color=True)

            # Transmission & Gamma Estimation
            t = self.transmission_estimation(
                haze=cirrus
            )

            # Atmospheric Light Estimation From Clear
            A = self.atmospheric_light_estimation(clear)
            
            # Generate hazy image
            I, J = self.hazy_generator(
                clear, 
                A, 
                transmission=t
            )

            # Save clear image
            """self.save_image(
                image=J, 
                dir_path=self.dir_path, 
                modul='clear', 
                image_name=clear_name
            )"""
            self.save_image(
                image=I, 
                dir_path=self.dir_path, 
                modul='hazy', 
                image_name=clear_name
            )
                

if __name__ == "__main__":
    default_dir = os.path.join('/kaggle/working', 'cirrus')
    if not os.path.exists(default_dir):
        os.mkdir(default_dir)
    
    haze_translation = HazyGenerator(
        mode=1, 
        size=256, 
        dir_path=default_dir
    )
    
    haze_translation(
        cirrus_dir=glob(os.path.join(default_dir, 'cirrus', '*')),
        clear_dir=glob(os.path.join(default_dir, 'landsat', '*')),
    )
