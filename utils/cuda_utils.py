import sys
import subprocess

import torch


def cuda_info():
    print(torch.__version__)  # PyTorch库的版本号
    print(torch.cuda.is_available())  # 检查CUDA是否可用
    # print(torch.cuda_version)  # CUDA版本（ubuntu不兼容）
    print(torch.version.cuda)  # CUDA版本
    print(torch.cuda.device_count())  # CUDA设备数量
    print(torch.backends.cudnn.is_available())  # 是否支持cudnn
    print(torch.backends.cudnn.version())  # cudnn版本

    device = torch.device('cuda:0')

    print()
    print(torch.cuda.get_device_name())  # GPU名称
    print(torch.cuda.get_device_capability(0))  # 主要版本号（major）和次要版本号（minor）
    print(torch.cuda.get_device_properties(0))  # 设备属性

    with torch.cuda.device(device):
        print(device, end='\n\n')


def cuda_info2():
    print('+' + '-' * 153 + '+')
    print("| Python version:", sys.version)  # Python版本
    print("| PyTorch version:", torch.__version__)  # PyTorch库的版本号
    print("| CUDA available:", torch.cuda.is_available())  # 检查CUDA是否可用
    # print("| CUDA version:", torch.cuda_version)  # CUDA版本（ubuntu不兼容）
    print("| CUDA version:", torch.version.cuda)  # CUDA版本
    print("| CUDA device count:", torch.cuda.device_count())  # CUDA设备数量
    print("| cuDNN available:", torch.backends.cudnn.is_available())  # 是否支持cudnn
    print("| cuDNN version:", torch.backends.cudnn.version())  # cudnn版本

    if torch.cuda.is_available():
        device = torch.device('cuda:0')
        print("| ")
        print("| GPU name:", torch.cuda.get_device_name())  # GPU名称
        print("| Device capability:", torch.cuda.get_device_capability(0))  # 主要版本号（major）和次要版本号（minor）
        print("| Device properties:", torch.cuda.get_device_properties(0))  # 设备属性

        with torch.cuda.device(device):
            print("| Current device:", device)
    print('+' + '-' * 153 + '+\n')


def cuda_info3():
    width = 27

    def print_line(content1, content2, b_w='\033[97m', red='\033[31m', white='\033[0m'):
        print(f"| {b_w}{content1}{red}{content2}{' ' * (width - 4 - len(content1 + content2))}{white} |")

    print('+' + '-' * (width - 2) + '+')
    print_line("Python version: ", f"{sys.version.split()[0]}")  # 仅打印版本号
    print_line("PyTorch version: ", f"{torch.__version__}")  # PyTorch库的版本号
    print_line("CUDA available: ", f"{torch.cuda.is_available()}")  # 检查CUDA是否可用
    # print_line("CUDA version: ", f"{torch.cuda_version}")  # CUDA版本（ubuntu不兼容）
    print_line("CUDA version: ", f"{torch.version.cuda}")  # CUDA版本
    print_line("CUDA device count: ", f"{torch.cuda.device_count()}")  # CUDA设备数量
    print_line("cuDNN available: ", f"{torch.backends.cudnn.is_available()}")  # 是否支持cudnn
    print_line("cuDNN version: ", f"{torch.backends.cudnn.version()}")  # cudnn版本

    if torch.cuda.is_available():
        width = 155
        device = torch.device('cuda:0')
        print(f"|{'=' * (27 - 2)}+{'=' * (width - 27 - 1)}+")
        print_line("GPU name: ", f"{torch.cuda.get_device_name()}")  # GPU名称
        print_line("Device capability: ", f"{torch.cuda.get_device_capability(0)}")  # 主要版本号（major）和次要版本号（minor）
        print_line("Device properties: ", f"{torch.cuda.get_device_properties(0)}")  # 设备属性
        print_line("Current device: ", f"{device}")  # 当前设备
    print('+' + '-' * (width - 2) + '+', end='\n\n')


def cuda_info4():
    lines = [
        ("Python version: ", f"{sys.version.split()[0]}"),
        ("PyTorch version: ", f"{torch.__version__}"),
        ("CUDA available: ", f"{torch.cuda.is_available()}"),
        ("CUDA version: ", f"{torch.version.cuda}"),
        ("CUDA device count: ", f"{torch.cuda.device_count()}"),
        ("cuDNN available: ", f"{torch.backends.cudnn.is_available()}"),
        ("cuDNN version: ", f"{torch.backends.cudnn.version()}")
    ]
    width = max(len(k) + len(v) for k, v in lines) + 4

    def print_line(content1, content2, b_w='\033[97m', red='\033[31m', white='\033[0m'):
        line = f"| {b_w}{content1}{red}{content2}{' ' * (width - 4 - len(content1 + content2))}{white} |"
        print(line)

    print('+' + '-' * (width - 2) + '+')
    for content1, content2 in lines:
        print_line(content1, content2)

    if torch.cuda.is_available():
        lines.extend([
            ("GPU name: ", f"{torch.cuda.get_device_name()}"),
            ("Device capability: ", f"{torch.cuda.get_device_capability(0)}"),
            ("Device properties: ", f"{torch.cuda.get_device_properties(0)}"),
            ("Current device: ", str(torch.device('cuda:0')))
        ])
    else:
        print('+' + '-' * (width - 2) + '+', end='\n\n')
        return
    width_origin = width
    width = max(len(k) + len(v) for k, v in lines[7:]) + 4
    line_str = '+' + '=' * (max(width_origin, width) - 2) + '+'
    line_list = list(line_str)
    line_list[min(width_origin, width) - 1] = '+'
    line_str = ''.join(line_list)
    print(line_str)
    for content1, content2 in lines[7:]:
        print_line(content1, content2)
    print('+' + '-' * (width - 2) + '+', end='\n\n')


def nvidia_smi_info():
    result = subprocess.run(['nvidia-smi'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    print(result.stdout)


def nvidia_smi_info2():
    subprocess.check_call('nvidia-smi')
    print()


if __name__ == '__main__':
    cuda_info()
    cuda_info2()
    cuda_info3()
    cuda_info4()
    nvidia_smi_info()
    nvidia_smi_info2()
