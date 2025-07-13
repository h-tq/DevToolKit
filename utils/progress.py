import datetime
import math
import time


def progress_bar(current_step, total_steps, start_time=0.0, title=None, width=40):
    """
    current_step: 当前进度
    total_steps: 总进程数
    start_time: 第一次开始时间
    title: 标题
    width: 进度条宽度
    \033[31m：设置文本颜色为红色。
    \033[32m：设置文本颜色为绿色。
    \033[36m：设置文本颜色为青色（青绿色）。
    \033[37m：设置文本颜色为白色。
    \033[97m：设置文本颜色为亮白色（一般比普通白色更亮）。

    文本属性：
    \033[0m：重置所有属性
    \033[1m：粗体
    \033[2m：暗色
    \033[3m：斜体
    \033[4m：下划线
    \033[5m：闪烁
    \033[7m：反显（背景和前景颜色交换）
    \033[8m：隐藏（不可见）
    \033[9m：删除线
    前景颜色：
    \033[30m：黑色
    \033[31m：红色
    \033[32m：绿色
    \033[33m：黄色
    \033[34m：蓝色
    \033[35m：洋红色
    \033[36m：青色
    \033[37m：白色
    \033[90m：亮黑色（灰色）
    \033[91m：亮红色
    \033[92m：亮绿色
    \033[93m：亮黄色
    \033[94m：亮蓝色
    \033[95m：亮洋红色
    \033[96m：亮青色
    \033[97m：亮白色
    背景颜色：
    \033[40m：黑色背景
    \033[41m：红色背景
    \033[42m：绿色背景
    \033[43m：黄色背景
    \033[44m：蓝色背景
    \033[45m：洋红色背景
    \033[46m：青色背景
    \033[47m：白色背景
    \033[100m：亮黑色（灰色）背景
    \033[101m：亮红色背景
    \033[102m：亮绿色背景
    \033[103m：亮黄色背景
    \033[104m：亮蓝色背景
    \033[105m：亮洋红色背景
    \033[106m：亮青色背景
    \033[107m：亮白色背景
    """
    progress_ratio = current_step / total_steps
    filled_length = int(width * progress_ratio)
    elapsed_time = max(time.time() - start_time, 1e-6)
    remaining_time = (elapsed_time / current_step) * (total_steps - current_step)
    if title:
        print(f'\r{title}', end=' ')
    else:
        print('\r', end='   ')
    if filled_length < width:
        print('\033[31m{}\033[37m╺{}\033[0m'.format("━" * filled_length, "━" * (width - filled_length - 1)), end=' ')
    else:
        print('\033[32m{}\033[0m'.format("━" * filled_length), end=' ')
    print('\033[32m{}/{} N\033[0m'.format(current_step, total_steps), end=' ')
    print('\033[31m{:.1f} n/s\033[0m'.format(current_step / elapsed_time), end=' ')
    print('eta \033[36m{}\033[0m'.format(datetime.timedelta(seconds=math.ceil(remaining_time))), end=' ')
    if current_step == total_steps:
        print()


class ProgressBar:
    def __init__(self, total_steps: int, title: str = "", bar_width=40, display_progress=True):
        self.total_steps = total_steps
        self.title = title
        self.bar_width = bar_width
        self.display_progress = display_progress
        self.current_step = 0
        self.start_time = time.time()
        time.sleep(0.001)

    @staticmethod
    def __format_time(seconds: float) -> datetime.timedelta:
        return datetime.timedelta(seconds=math.ceil(seconds))  # 向上取整

    def update(self, extra_info: str = "", step_increment: int = 1) -> None:
        self.current_step += step_increment
        progress_ratio = self.current_step / self.total_steps
        filled_length = int(self.bar_width * progress_ratio)
        empty_length = self.bar_width - filled_length

        print(f"\r{self.title} " if self.title else "\r   ", end='')
        if filled_length < self.bar_width:
            print("\033[31m{}\033[37m{}{}\033[0m".format("━" * filled_length, '╺', "━" * (empty_length - 1)), end=' ')
        else:
            print("\033[32m{}\033[0m".format("━" * filled_length), end=' ')
        print("\033[32m{}/{}\033[0m".format(self.current_step, self.total_steps), end=' ')

        elapsed_time = max(time.time() - self.start_time, 1e-6)  # not 0
        remaining_time = (elapsed_time / self.current_step) * (self.total_steps - self.current_step)

        print("\033[31m{:.1f}/s\033[0m".format(self.current_step / elapsed_time), end=' ')
        print("eta \033[36m{}\033[0m".format(self.__format_time(remaining_time)), end=' ')

        if self.display_progress:
            print(f"\033[3m\033[33m[Elapsed: {self.__format_time(elapsed_time)}]\033[0m", end=' ')
            print(f"\033[3m\033[34m[{int(progress_ratio * 100)}%]\033[0m", end=' ')

        if extra_info:
            print(f"[{extra_info}]", end=' ')

        if self.current_step == self.total_steps:
            print()


if __name__ == '__main__':
    print('capsule:1/15 - epoch:1/2')
    total_images = 219
    # 测试进度条 1
    start_time = time.time()
    for current_image_count in range(total_images):
        progress_bar(current_image_count + 1, total_images, start_time)

    # 测试进度条 2
    pbar = ProgressBar(total_images)
    for _ in range(total_images):
        time.sleep(0.001)
        pbar.update("epoch 0: loss={:.4f}".format(_ / 3.14))

    # 测试进度条 3
    pbar = ProgressBar(total_images, display_progress=False)
    for _ in range(total_images):
        time.sleep(0.001)
        pbar.update()
