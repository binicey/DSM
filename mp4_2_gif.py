# from moviepy.editor import VideoFileClip
import os
# path_folder = "D:/nerfies.github.io-main/static/videos/"
# #读取文件夹下所有文件
# path_list = os.listdir(path_folder)
# for i in path_list:
#     if i.endswith('.mp4'):
#         video_path = path_folder + i
#         output_gif = path_folder + i[:-4] + ".gif"
#         os.system("ffmpeg -i " + video_path + " -vf \"fps=10,scale=480:-1:flags=lanczos\" " + output_gif)
#         print("Convert " + video_path + " to " + output_gif + " successfully!")
# print("All done!")
path_folder = "D:/nerfies.github.io-main/static/videos/"
i = "navigation_demo.mp4"
video_path = path_folder + i
output_gif = path_folder + i[:-4] + ".gif"
os.system("ffmpeg -i " + video_path + " -vf \"fps=10,scale=480:-1:flags=lanczos\" " + output_gif)
print("Convert " + video_path + " to " + output_gif + " successfully!")