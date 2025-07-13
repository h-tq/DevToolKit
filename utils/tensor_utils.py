import torch


def is_binary_tensor(tensor: torch.Tensor):
    """
    判断一个张量是否只包含 0 和 1。

    参数：
        tensor (torch.Tensor): 待检查的张量。

    返回:
        bool: 如果张量只包含 0 和 1，返回 True；否则返回 False。
    """
    return torch.isin(tensor, torch.tensor([0, 1])).all().item()


def to_device(input: dict, device: torch.device = torch.device("cuda")) -> dict:
    for key, value in input.items():
        if torch.is_tensor(value):
            input[key] = input[key].to(device=device)

    return input
