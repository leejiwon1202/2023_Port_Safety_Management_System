import os
import json
import random
import shutil

# 0)
src_path_images = "/home/jiwon/OD_Gate/Door/images/"
src_path_label = "/home/jiwon/OD_Gate/Door/labels/"

label_list = os.listdir(src_path_label)
use_list = random.sample(label_list, 24000)
train_list = use_list[:16000]
valid_list = use_list[16000:]
print(len(label_list), len(use_list), len(train_list), len(valid_list)) # 


# 1)
dst_path_train = "/home/jiwon/OD_Gate/Door/test/train/images"
dst_path_valid = "/home/jiwon/Harbor_Data/test/valid/images"

#dst_path_train = "/home/jiwon/OD_Gate/train/images"
#dst_path_valid = "/home/jiwon/OD_Gate/valid/images"

# 1-1) train image
# for train_image in train_list:
#     s_path = src_path_images + train_image[:-1] + ".jpg"
#     d_path = dst_path_train + train_image[:-1] + ".jpg"
#     shutil.copyfile(s_path, d_path) 

# 1-2) valid image
# for valid_image in valid_list:
#     s_path = src_path_images + valid_image[:-1] + ".jpg"
#     d_path = dst_path_valid + valid_image[:-1] + ".jpg"
#     shutil.copyfile(s_path, d_path) 

# print("train image :", len(os.listdir(dst_path_train))) #
# print("valid image :", len(os.listdir(dst_path_valid))) # 


# 2)
dst_path_train = "/home/jiwon/OD_Gate/Door/test/train/labels"
dst_path_valid = "/home/jiwon/Harbor_Data/test/valid/labels"

#dst_path_train = "/home/jiwon/Harbor_Data/train/labels"
#dst_path_valid = "/home/jiwon/Harbor_Data/valid/labels"

# for index, path in enumerate(train_list):
#     with open(src_path_label + path, 'r', encoding='utf-8') as f:
#         json_data = json.load(f)
    
#     txt_file = open(dst_path_train + json_data['images']['identifier'] + ".txt", 'w')
    
#     print(index, json_data['images']['identifier'] + ".txt")
    
#     for obj in json_data['annotations']: 
#         cName = obj['bbox']['classid']

#         if cName == "DOOR":       txt_file.write("1 ")
#         else:   print("error")
        
#         s_x = obj['bbox']['points'][0][0]
#         s_y = obj['bbox']['points'][0][1]
#         e_x = obj['bbox']['points'][2][0]
#         e_y = obj['bbox']['points'][2][1]

#         c_x = ((s_x + e_x) / 2) / 1920
#         c_y = ((s_y + e_y) / 2) / 1080
#         width = (e_x - s_x) / 1920
#         height = (e_y - s_y) / 1080

#         print(c_x, c_y, width, height)
        
#         txt_file.write("%f %f %f %f\n" % (c_x, c_y, width, height))
#     txt_file.close()
#     print()

# for index, path in enumerate(valid_list):
#     with open(src_path_label + path, 'r', encoding='utf-8') as f:
#         json_data = json.load(f)
    
#     txt_file = open(dst_path_valid + json_data['images']['identifier'] + ".txt", 'w')
    
#     print(index, json_data['images']['identifier'] + ".txt")
    
#     for obj in json_data['annotations']: 
#         cName = obj['bbox']['classid']

#         if cName == "DOOR":       txt_file.write("1 ")
#         else:   print("error")
        
#         s_x = obj['bbox']['points'][0][0]
#         s_y = obj['bbox']['points'][0][1]
#         e_x = obj['bbox']['points'][2][0]
#         e_y = obj['bbox']['points'][2][1]

#         c_x = ((s_x + e_x) / 2) / 1920
#         c_y = ((s_y + e_y) / 2) / 1080
#         width = (e_x - s_x) / 1920
#         height = (e_y - s_y) / 1080

#         print(c_x, c_y, width, height)
        
#         txt_file.write("%f %f %f %f\n" % (c_x, c_y, width, height))
#     txt_file.close()
#     print()