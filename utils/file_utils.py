import os
import shutil


def setup_directory(path, delete_existing: bool = False):
    """
    创建一个新文件夹，或根据需要删除并重建现有文件夹。

    参数:
        path (str): 目标文件夹路径。
        delete_existing (bool): 是否删除现有文件夹，默认为 False。

    返回:
        None
    """
    if os.path.exists(path):
        if delete_existing:
            shutil.rmtree(path)  # 删除现有文件夹
            os.makedirs(path)  # 创建新的文件夹
            print(f"Directory '\033[97m{path}\033[0m' has been deleted and recreated successfully.")
        else:
            print(f"Directory '\033[97m{path}\033[0m' already exists. No action taken.")
    else:
        os.makedirs(path)  # 创建新的文件夹
        print(f"Directory '\033[97m{path}\033[0m' has been created successfully.")
