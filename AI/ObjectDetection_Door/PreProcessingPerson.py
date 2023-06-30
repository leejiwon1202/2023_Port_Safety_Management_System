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



# 2) annotation
import cv2
src_path = "/home/jiwon/OD_Gate/WiderPerson/Annotations/"

# 2-1) train annotation
# org_path_train_images = "/home/jiwon/OD_Gate/train/images/"
# dst_path_train = "/home/jiwon/OD_Gate/train/labels/"
# for train_image in train_list:
#     train_image = train_image[:-1]
#     s_path = src_path + train_image + ".jpg.txt"
#     content = open(s_path, 'r', encoding="UTF8")
#     content_list = content.readlines()
    
#     i_path = org_path_train_images + train_image + ".jpg"
#     shape = cv2.imread(i_path).shape
#     height = shape[1]
#     width = shape[0]

#     d_path = dst_path_train + train_image + ".txt"
#     f = open(d_path, "w", encoding="UTF8")
#     for bbox in content_list[1:]:
#         p = bbox.split(" ")[1:]
#         x1, y1, x2, y2 = int(p[0]), int(p[1]), int(p[2]), int(p[3])
#         cx, cy, w, h = (x1+x2)/2, (y1+y2)/2, x2-x1, y2-y1

#         row = "0 {} {} {} {}\n".format(cx/height, cy/width, w/width, h/height)
#         f.write(row)
#     f.close()
# print(len(os.listdir(dst_path_train))) # 8,000

# 2-2) valid annotation
# org_path_valid_images = "/home/jiwon/OD_Gate/valid/images/"
# dst_path_valid = "/home/jiwon/OD_Gate/valid/labels/"
# for valid_image in valid_list:
#     valid_image = valid_image.replace("\n", "")
#     s_path = src_path + valid_image + ".jpg.txt"
#     content = open(s_path, 'r', encoding="UTF8")
#     content_list = content.readlines()
    
#     i_path = org_path_valid_images + valid_image + ".jpg"
#     shape = cv2.imread(i_path).shape
#     height = shape[1]
#     width = shape[0]

#     d_path = dst_path_valid + valid_image + ".txt"
#     f = open(d_path, "w", encoding="UTF8")
#     for bbox in content_list[1:]:
#         p = bbox.split(" ")[1:]
#         x1, y1, x2, y2 = int(p[0]), int(p[1]), int(p[2]), int(p[3])
#         cx, cy, w, h = (x1+x2)/2, (y1+y2)/2, x2-x1, y2-y1

#         row = "0 {} {} {} {}\n".format(cx/height, cy/width, w/width, h/height)
#         f.write(row)
#     f.close()
# print(len(os.listdir(dst_path_valid))) # 1,000