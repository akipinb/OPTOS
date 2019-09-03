import cv2
import pandas as pd
import pathlib
from pathlib import Path
import random

def classification(j, save_dir):
    if j % 9 != 0:
        return save_dir / 'train'
    else:
        return save_dir / 'valid'

#exit()
def main():
    dict_csv = pd.read_csv('./backup/data.csv')
    key = ['AMD', 'RVO', 'Gla', 'MH', 'DR', 'RD', 'RP', 'AO']
    imgs = dict()
    norms = list()
    for elem in key:
    #    print(f'{i}_{elem}')
        imgs[elem] = list()
    #print(imgs)
            
    for index, item in dict_csv.iterrows():
        sub_dir = ['train', 'valid']
        if index >= 3200:
            break
        img_path = Path('./backup/eye_image_raw/' +  item['filename'])
        print(img_path)

        norm = True
        for elem in key:
            if item[elem] == 1:
                print(elem)
                norm = False
                imgs[elem].append(img_path)

        if norm:
            print('NORM')
            norms.append(img_path)

    save_dir = Path('./dataset_mini_weak/')
    for i,(key,item) in enumerate(imgs.items()):
        print(key,item)
        for j,it in enumerate(item):
            buf_dir = classification(j, save_dir)
#            print(it)
#            print(buf_dir / f'{i}_{key}' / it.name)
            img = cv2.imread(str(it))
            if img is None:
                continue
            save_path = buf_dir / f'{i}_{key}' / it.name
            if not save_path.parent.exists():
                save_path.parent.mkdir(parents=True)
#                print('hoge')
        
            print(str(save_path))
            cv2.imwrite(str(save_path), img)

    for j, it in enumerate(norms):
        buf_dir = classification(j, save_dir)
        img = cv2.imread(str(it))
        if img is None:
            continue
        save_path = buf_dir / '9_normal' / it.name
        if not save_path.parent.exists():
            save_path.parent.mkdir(parents=True)
        
        print(str(save_path))
        cv2.imwrite(str(save_path), img)
#        print(it / item['filename'])
if __name__ == '__main__':
    main()
    


"""
for index, item in dict_csv.iterrows():
#    if img_path is None:
#        continue
#    save_dir = dict()
    if item['AMD'] == 1:
        imgs.append(Path('./dataset_mini_weak(AMD, MH, AO)/'))
    if item['RVO'] == 1:
        save_dir.append(Path('./dataset_mini_weak(AMD, MH, AO)/'))
    if item['Gla'] == 1:
        save_dir.append(Path('./dataset_mini_weak(AMD, MH, AO)/'))
    if item['MH'] == 1:
        save_dir.append(Path('./dataset_mini_weak(AMD, MH, AO)/'))
    if item['DR'] == 1:
        save_dir.append(Path('./dataset_mini_weak(AMD, MH, AO)/'))
    if item['RD'] == 1:
        save_dir.append(Path('./dataset_mini_weak(AMD, MH, AO)/'))
    if item['RP'] == 1:
        save_dir.append(Path('./dataset_mini_weak(AMD, MH, AO)/'))
    if item['AO'] == 1:
        save_dir.append(Path('./dataset_mini_weak(AMD, MH, AO)/'))
#    if item['DM'] == 1:
#        save_dir.append(Path('./dataset/8_DM/'))
    if not save_dir:
        save_dir.append(Path('./dataset_mini_weak(AMD, MH, AO)/9_normal'))
    
    for s_dir in save_dir:
        if not s_dir.exists():
            s_dir.mkdir(parents=True)
    
        cv2.imwrite(str(s_dir / item['filename']), img)
        print(s_dir / item['filename'])
"""