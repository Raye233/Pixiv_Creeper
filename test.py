import os
import shutil

os.chdir(r'F:\Rayedata2\Creeper\Pixiv\realesrgan-ncnn-vulkan-20211212-windows')
retval = os.getcwd()

print("目录修改成功 %s" % retval)
# os.startfile(r"F:\Rayedata2\Creeper\Pixiv\realesrgan-ncnn-vulkan-20211212-windows\output")

path = r'F:\Rayedata2\Creeper\Pixiv\realesrgan-ncnn-vulkan-20211212-windows\input'


def del_file(filepath):
    """
    删除某一目录下的所有文件或文件夹
    :param filepath: 路径
    :return:
    """
    del_list = os.listdir(filepath)
    for f in del_list:
        file_path = os.path.join(filepath, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    print('已删除原input文件夹的所有文件')


del_file(path)
