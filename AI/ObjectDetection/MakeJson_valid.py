import os
import json

origin_path1 = "/home/jiwon/Harbor_Data/VL/YT/"
origin_path2 = "/home/jiwon/Harbor_Data/VL/TwistLock/"

target_path = "/home/jiwon/Harbor_Data/valid/labels/"

yt_list = os.listdir(origin_path1) # 9129
tl_list = os.listdir(origin_path2) # 557
print(len(yt_list), len(tl_list), len(yt_list) + len(tl_list)) # 9686

# for index, path in enumerate(yt_list):
#     with open(origin_path1 + path, 'r', encoding='utf-8') as f:
#         json_data = json.load(f)
    
#     txt_file = open(target_path + json_data['images']['identifier'] + ".txt", 'w')
    
#     print(index, json_data['images']['identifier'] + ".txt")
    
#     for obj in json_data['annotations']: 
#         cName = obj['bbox']['classid']

#         if cName == "CONTAINER_20FT":       txt_file.write("0 ")
#         elif cName == "CONTAINER_40FT":     txt_file.write("1 ")
#         elif cName == "TANK_20FT":          txt_file.write("2 ")
#         elif cName == "YT_CHASSIS_EMPTY":   txt_file.write("3 ")
#         elif cName == "YT_CHASSIS_HALF":    txt_file.write("4 ")
#         elif cName == "YT_HEADER":          txt_file.write("5 ")
#         else:   print("error")
        
#         s_x = obj['bbox']['points'][0][0] / 1920
#         s_y = obj['bbox']['points'][0][1] / 1080
#         e_x = obj['bbox']['points'][2][0] / 1920
#         e_y = obj['bbox']['points'][2][1] / 1080
        
#         print(s_x, s_y, e_x, e_y)
        
#         txt_file.write("%f %f %f %f\n" % (s_x, s_y, e_x, e_y))
        
#     txt_file.close()
#     print()

# for index, path in enumerate(tl_list):
#     with open(origin_path2 + path, 'r', encoding='utf-8') as f:
#         json_data = json.load(f)
    
#     txt_file = open(target_path + json_data['images']['identifier'] + ".txt", 'w')
    
#     print(index, json_data['images']['identifier'] + ".txt")
    
#     for obj in json_data['annotations']: 
#         cName = obj['bbox']['classid']

#         if cName == "TWISTLOCK":       txt_file.write("6 ")
#         else:   print("error")
        
#         s_x = obj['bbox']['points'][0][0] / 1920
#         s_y = obj['bbox']['points'][0][1] / 1080
#         e_x = obj['bbox']['points'][2][0] / 1920
#         e_y = obj['bbox']['points'][2][1] / 1080
        
#         print(s_x, s_y, e_x, e_y)
        
#         txt_file.write("%f %f %f %f\n" % (s_x, s_y, e_x, e_y))
        
#     txt_file.close()
#     print()

print(len(os.listdir(target_path)))
print(len(os.listdir("/home/jiwon/Harbor_Data/valid/images")))

