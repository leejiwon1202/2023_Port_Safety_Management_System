import os

# 0) 데이터 갯수 확인
print("Images :", len(os.listdir('/home/jiwon/OD_Gate/WiderPerson/Images'))) # 13,382
print("Annotations :", len(os.listdir('/home/jiwon/OD_Gate/WiderPerson/Annotations'))) # 9,000

train_txt = open("/home/jiwon/OD_Gate/WiderPerson/train.txt", 'r', encoding="UTF8")
train_list = train_txt.readlines()

valid_txt = open("/home/jiwon/OD_Gate/WiderPerson/val.txt", 'r', encoding="UTF8")
valid_list = valid_txt.readlines()

test_txt = open("/home/jiwon/OD_Gate/WiderPerson/test.txt", 'r', encoding="UTF8")
test_list = test_txt.readlines()

# print("train :", len(train_list)) # 8,000
# print("valid :", len(valid_list)) # 1,000
# print("test :", len(test_list)) # 4,382



# 1) image
# import shutil
# src_path = "/home/jiwon/OD_Gate/WiderPerson/Images/"

# 1-1) train image
# dst_path_train = "/home/jiwon/OD_Gate/train/images/"
# for train_image in train_list:
#     s_path = src_path + train_image[:-1] + ".jpg"
#     d_path = dst_path_train + train_image[:-1] + ".jpg"
#     shutil.copyfile(s_path, d_path) 

# 1-2) valid image
# dst_path_train = "/home/jiwon/OD_Gate/valid/images/"
# for valid_image in valid_list:
#     s_path = src_path + valid_image[:-1] + ".jpg"
#     d_path = dst_path_train + valid_image[:-1] + ".jpg"
#     shutil.copyfile(s_path, d_path) 

# print("train image :", len(os.listdir('/home/jiwon/OD_Gate/train/images'))) # 8,000
# print("valid image :", len(os.listdir('/home/jiwon/OD_Gate/valid/images'))) # 1,000



# 2) labels
src_path = "/home/jiwon/OD_Gate/WiderPerson/Annotations/"
