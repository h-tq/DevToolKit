import os
from typing import Union, List

import cv2
import numpy as np
import torch


def save_images_to_folder(image: Union[np.ndarray, List[np.ndarray]], output_dir: str = "images",
                          prefix: str = "image"):
    os.makedirs(output_dir, exist_ok=True)
    existing_files_count = len(os.listdir(output_dir))

    if isinstance(image, np.ndarray) and (image.ndim == 2 or image.ndim == 3):
        image = [image]

    for idx, img in enumerate(image):
        filename = os.path.join(output_dir, f"{prefix}_{existing_files_count + idx + 1}.png")
        cv2.imwrite(filename, img)

    print(f"Saved {len(image)} image(s) to {output_dir}")


def show_tensor_images(tensor_images: torch.Tensor, convert_channels: bool = False, vertical: bool = False,
                       display: bool = True,
                       prefix: str = None):
    images_np = tensor_images.permute(0, 2, 3, 1).detach().cpu().numpy()  # (b c h w) -> (b h w c)

    images_np = (images_np * 255.0).astype(np.uint8)  # 归一化到0-255范围
    if convert_channels and images_np.shape[-1] == 3:
        images_np = [cv2.cvtColor(img, 4) for img in images_np]

    if prefix:
        save_images_to_folder(images_np, prefix=prefix)

    if vertical:
        concatenated_image = cv2.vconcat(images_np)
    else:
        concatenated_image = cv2.hconcat(images_np)

    if display:
        cv2.imshow("Displayed Images", concatenated_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return concatenated_image


def display_images(winname: str, images: list, vertical: bool = False):
    """
    显示多张图片，根据水平或垂直模式拼接。

    参数：
        winname (str): 窗口名称。
        images (list): 包含待显示图片的列表。
        vertical (bool): 拼接模式，False 表示水平拼接，True 表示垂直拼接。
    """
    if vertical:
        concatenated_image = cv2.vconcat(images)
    else:
        concatenated_image = cv2.hconcat(images)

    cv2.imshow(winname, concatenated_image)
    key_val = cv2.waitKey(0)
    cv2.destroyAllWindows()
    return key_val
