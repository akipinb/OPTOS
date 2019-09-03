import cv2
import pandas as pd
import pathlib
from pathlib import Path

dict_csv = pd.read_csv('./backup/data.csv')

imgs = []
for index, item in dict_csv.iterrows():
    if index >= 1000:
        exit()
    img = cv2.imread('./backup/eye_image_raw/' +  item['filename'])
    if img is None:
        continue
    save_dir = list()
    if item['AMD'] == 1:
        save_dir.append(Path('./dataset_mini_reduce_types/0_AMD'))
    if item['RVO'] == 1:
        save_dir.append(Path('./dataset_mini_reduce_types/1_other'))
    if item['Gla'] == 1:
        save_dir.append(Path('./dataset_mini_reduce_types/2_Gla'))
    if item['MH'] == 1:
        save_dir.append(Path('./dataset_mini_reduce_types/3_MH'))
    if item['DR'] == 1:
        save_dir.append(Path('./dataset_mini_reduce_types/4_DR'))
    if item['RD'] == 1:
        save_dir.append(Path('./dataset_mini_reduce_types/1_other'))
    if item['RP'] == 1:
        save_dir.append(Path('./dataset_mini_reduce_types/1_other'))
    if item['AO'] == 1:
        save_dir.append(Path('./dataset_mini_reduce_types/7_AO/'))
#    if item['DM'] == 1:
#        save_dir.append(Path('./dataset/8_DM/'))
    if not save_dir:
        save_dir.append(Path('./dataset/9_normal/'))
    
    for s_dir in save_dir:
        if not s_dir.exists():
            s_dir.mkdir(parents=True)
    
        cv2.imwrite(str(s_dir / item['filename']), img)
        print(s_dir / item['filename'])