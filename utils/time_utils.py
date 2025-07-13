import datetime


def get_current_time(display: bool = False):
    """
    获取当前时间并格式化输出。

    参数:
    - display (bool): 如果为 True，则在控制台打印当前时间；否则不打印。

    返回:
    - str: 格式化后的时间字符串，用于文件命名。
    """
    current_time = datetime.datetime.now()

    if display:  # 检查是否需要输出时间
        print(f'\033[97m{current_time.strftime("%Y/%m/%d %H:%M:%S")}\033[0m')  # 可视化输出时间

    return current_time.strftime("%Y-%m-%d_%H-%M-%S")  # 用于文件命名


if __name__ == '__main__':
    current_time = get_current_time(True)
    print(current_time)