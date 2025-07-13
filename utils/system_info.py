import os
import platform

import GPUtil
import psutil
from cpuinfo import get_cpu_info


def sys_info(title=''):
    """
    import GPUtil
    import psutil
    from cpuinfo import get_cpu_info

    pip install gputil -i https://pypi.tuna.tsinghua.edu.cn/simple
    pip install psutil -i https://pypi.tuna.tsinghua.edu.cn/simple
    pip install py-cpuinfo -i https://pypi.tuna.tsinghua.edu.cn/simple
    """
    width = 89
    separator = '+' + '-' * (width - 2) + '+'

    def print_line(c1, c2='', c3='', c4='',
                   b_w='\033[97m', r='\033[31m', g='\033[32m', b='\033[36m', w='\033[0m',
                   underline='\033[4m', bold='\033[1m'):
        if c2 and c3 and c4:
            padding = ' ' * (width - 10 - len(c1 + c2 + c3 + c4))
            print(f"| {b_w}{c1}{r}{c2}{b_w}/ {g}{c3}{b_w}/ ({b}{c4}{b_w}){w}{padding} |")
        else:
            padding = ' ' * (width - 4 - len(c1))
            print(f"| {b_w}{bold}{c1}{w}{padding} |")

    print(separator)
    if title:
        print_line(title)
        print(f"|{'=' * (width - 2)}|")
    # 获取CPU信息
    cpu_info = get_cpu_info()  # 获取详细的CPU信息
    cpu_name = cpu_info['brand_raw']  # 获取CPU的品牌和型号
    cpu_cores = os.cpu_count()  # 获取CPU核心数
    # 获取内存信息
    memory_info = psutil.virtual_memory()
    total_memory = memory_info.total / (1024 ** 3)  # 转换为GB
    used_memory = memory_info.used / (1024 ** 3)  # 转换为GB
    memory_percentage = memory_info.percent  # 占比
    # 打印CPU核心和内存信息
    print_line(f"CPU ({cpu_name}, {cpu_cores} cores): ",
               f"{used_memory:.2f} GB ",
               f"{total_memory:.2f} GB ",
               f"{memory_percentage:.2f}%")
    # 获取GPU信息
    gpus = GPUtil.getGPUs()
    for gpu in gpus:
        total_gpu_memory = gpu.memoryTotal / 1024  # 转换为GB
        used_gpu_memory = gpu.memoryUsed / 1024  # 转换为GB
        gpu_memory_percentage = (gpu.memoryUsed / gpu.memoryTotal) * 100
        print_line(f"GPU [{gpu.id}] ({gpu.name}): ",
                   f"{used_gpu_memory:.2f} GB ",
                   f"{total_gpu_memory:.2f} GB ",
                   f"{gpu_memory_percentage:.2f}%")
    print(separator, end='\n\n')


def get_os_name(display: bool = False):
    os_name = platform.system()
    print(os_name)
    return os_name


if __name__ == '__main__':
    sys_info()
    get_os_name()