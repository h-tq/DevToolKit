import pprint

from easydict import EasyDict


def dict_to_easydict(source_dict, should_pretty_print=False):
    """
    将传统字典转换为 EasyDict，并根据需要格式化打印。

    参数:
        source_dict (dict): 要转换的传统字典。
        should_pretty_print (bool): 如果为 True，则格式化打印 EasyDict；否则不打印。默认为 False。

    返回:
        EasyDict: 转换后的 EasyDict 对象。
    """
    easydict_obj = EasyDict(source_dict)  # 将传统字典转换为 EasyDict

    if should_pretty_print:
        # print(pprint.pformat(easydict_obj))
        pprint.pprint(easydict_obj)  # 格式化打印 EasyDict

    return easydict_obj  # 返回转换后的 EasyDict
