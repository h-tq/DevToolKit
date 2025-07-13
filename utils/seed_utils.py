import os
import random

import numpy as np
import torch


def set_random_seed(seed, reproduce: bool = False):
    """
    设置随机种子以确保实验的可重复性。

    Args:
        seed (int): 随机种子。
        reproduce (bool): 是否启用确定性复现模式 (默认为 False)。

    Returns: None
    """
    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed)
    random.seed(seed)

    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)  # 多GPU设定种子

    # 设置CuDNN后端的行为，确保确定性
    if reproduce:  # 重现性优先
        torch.backends.cudnn.benchmark = False  # 禁用自动优化
        torch.backends.cudnn.deterministic = True  # 确保算法确定性
    else:  # 性能优先
        torch.backends.cudnn.benchmark = True  # 启用优化
        torch.backends.cudnn.deterministic = False


if __name__ == "__main__":
    set_random_seed(42, True)