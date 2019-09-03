#!/usr/bin/env python3
# -*-coding: utf-8 -*-

import cv2
import csv
import os
import pandas as pd
import pathlib
from pathlib import Path

# pandasで読み込み元のCSVを指定
dict_csv = pd.read_csv('./backup/data.csv')
# imgsというリストを作り、http://hxn.blog.jp/archives/8923017.html このブログを参照してpandas.DataFrameの値を行ごとに取り出して処理
imgs = []
for index, item in dict_csv.iterrows():
# 以下は処理確認用のリミット
#    if index >= 10:
#        exit()
#    print(index, item['AMD'], item['RVO'], item['Gla'], item['MH'], item['DR'], item['RD']. item['RP'], item['AO'], item['DM'])
# cv2を使用してfilenameを取得
    img = cv2.imread('./backup/eye_image_raw/' +  item['filename'])
    print(0,item)
    if img is None:
        print(1,'None')
        continue
    save_dir = list()
# 複数の要素を同時にもつ可能性があるので、elifは使用せず全部if。save_dirをlistにすることで全ての要素を格納できるようになる
    if item['AMD'] == 1:
        save_dir.append(Path('./dataset_check2/0_AMD/'))
        print(2,item['filename'])
    if item['RVO'] == 1:
        save_dir.append(Path('./dataset_check2/1_RVO/'))
        print(3,item['filename'])
    if item['Gla'] == 1:
        save_dir.append(Path('./dataset_check2/2_Gla/'))
        print(4,item['filename'])
    if item['MH'] == 1:
        save_dir.append(Path('./dataset_check2/3_MH/'))
        print(5,item['filename'])
    if item['DR'] == 1:
        save_dir.append(Path('./dataset_check2/4_DR/'))
        print(6,item['filename'])
    if item['RD'] == 1:
        save_dir.append(Path('./dataset_check2/5_RD/'))
        print(7,item['filename'])
    if item['RP'] == 1:
        save_dir.append(Path('./dataset_check2/6_RP/'))
        print(8,item['filename'])
    if item['AO'] == 1:
        save_dir.append(Path('./dataset_check2/7_AO/'))
        print(9,item['filename'])
    if item['DM'] == 1:
        save_dir.append(Path('./dataset_check2/8_DM/'))
        print(10,item['filename'])
    if not save_dir:
        save_dir.append(Path('./dataset_check2/9_normal/'))
#        print(11,item['filename'])

#    checker = [i for i in save_dir if i == './dataset_check2/9_normal/']
#    print(checker)
# listを変換
    for s_dir in save_dir:

# 保存するfile pathが無ければ作成する
        if not s_dir.exists():
            s_dir.mkdir(parents=True)
    
        cv2.imwrite(str(s_dir / item['filename']), img)
        print(s_dir / item['filename'])