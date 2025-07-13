

[TOC]

## 📘 技术与科研常用 Emoji 对照表

| Emoji | 主题/含义       | 备注/适用场景                  |
| ----- | --------------- | ------------------------------ |
| 🔣     | 符号/编码       | 特殊字符、编码、字符集相关     |
| 📌     | 固定/重点       | 重点标记、固定内容、待办事项   |
| 🚫     | 禁止/不可用     | 禁止操作、禁用状态、不可访问   |
| 🧪     | 实验            | 实验过程、实验室、科研测试     |
| 🔬     | 显微镜          | 细节观察、科学实验、分析       |
| 🧬     | DNA             | 生命科学、生物信息学、基因研究 |
| 📊     | 数据分析        | 统计、数据可视化、图表         |
| 📈     | 上升趋势        | 进展、性能提升、增长           |
| 📉     | 下降趋势        | 退步、性能下降、减少           |
| 💻     | 计算机/编程     | 代码开发、计算机工作           |
| 🐍     | Python          | Python 编程语言                |
| 🐧     | Linux           | Linux 操作系统                 |
| 🧠     | 人工智能/思考   | 机器学习、AI、智能算法         |
| 🤖     | 机器人          | 自动化、机器人学、智能系统     |
| 🔧     | 工具/调试       | 配置、修复、开发工具           |
| 📁     | 文件夹/项目管理 | 数据文件、项目组织             |
| 📦     | 软件包/部署     | 软件打包、版本发布             |
| 📝     | 记录/笔记       | 实验笔记、写作、文档           |
| 📚     | 书籍/文献       | 学习、论文、文献               |
| 🔥     | 热门/性能好     | 流行技术、优秀成果             |
| ⚠️     | 警告/风险       | 注意事项、安全提示             |
| ✅     | 完成/正确       | 任务完成、结果验证             |
| ❌     | 错误/失败       | 错误提醒、测试失败             |
| ⏳     | 时间/进度       | 进度等待、时间消耗             |
| 💡     | 灵感/创意       | 创新点、想法                   |
| 🧩     | 组件/模块       | 模块化设计、拼图、组合         |
| 📡     | 通信/信号       | 数据传输、网络连接             |
| 🌡️     | 测量/环境       | 温度测量、实验环境             |
| 🖼️     | 图像/视觉       | 图像处理、视觉相关             |
| 🔊     | 声音/音频       | 音频信号、声学                 |

------

## 🛠️ 查看 NVIDIA 驱动版本

```bash
nvidia-smi
```


------

## 🔧 Python pip 安装镜像源

🌐 清华大学：https://pypi.tuna.tsinghua.edu.cn/simple

🔬 中国科学技术大学：https://pypi.mirrors.ustc.edu.cn/simple

☁️ 阿里云：http://mirrors.aliyun.com/pypi/simple

📖 豆瓣：http://pypi.doubanio.com/simple

☁️ 腾讯云：https://mirrors.cloud.tencent.com/pypi/simple

🌐 百度（不可用）：https://mirror.baidu.com/pypi/simple ❌

🏭 华为云（不可用）：https://repo.huaweicloud.com/repository/pypi/simple ❌

------

## 🛠️ Conda 镜像配置指南

🔍 查看已有镜像源

```bash
conda config --show channels
```

🌐 添加清华镜像源

```bash
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/linux-64/
```

📋 显示通道地址配置

```bash
conda config --set show_channel_urls yes  # 配置文件路径：C:\Users\用户名\.condarc
```

❌ 删除镜像源命令

```bash
conda config --remove channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/  # 删除单个镜像源
conda config --remove-key channels                                                       # 恢复默认配置
```

------

## 🔧 Anaconda 环境管理指南

🔍 查看已配置的环境

```bash
conda env list
conda info --envs
```

🚀 创建、激活、停用虚拟环境

```bash
conda create -n env-name python=3.8
conda activate env-name
conda deactivate
```

🧪 测试 PyTorch 安装

```bash
python
import torch
print(torch.__version__)
print(torch.cuda.is_available())
print(torch.version.cuda)
print(torch.cuda.device_count())
print(torch.backends.cudnn.is_available())
print(torch.backends.cudnn.version())
quit()
```


------

## 🐍 Python 与 Conda 包管理清理指南

✅ 检查已安装 Python 包的依赖关系是否存在问题

```bash
pip check
```

📦 通过 pip 查看 PyPI 上某个包的可用版本

```bash
pip index versions torch
```

🧹 删除 Conda 虚拟环境

```bash
conda remove -n env-name --all
conda env remove -n env-name
```

♻️ 删除 Conda 环境后清理遗留缓存

```bash
conda clean -a          # 清理所有 Conda 缓存（推荐）：删除索引缓存、锁文件、未使用的包、下载的旧 tar 包
conda clean -i          # 仅清理 Conda 的索引缓存（从服务器下载的仓库索引信息）
```

📦 Pip 缓存相关操作

```bash
pip cache dir           # 查看 Pip 默认缓存目录的路径
pip cache purge         # 清理 Pip 缓存文件（全面清理）
pip cache info          # 查看缓存统计信息（如缓存大小）
pip cache list          # 列出所有已缓存的安装包
```

------

## DREAM

| 💻 Windows | 🐍 Python 3.12 | 🔥 PyTorch 2.4.1 | 🧠 CUDA 12.4 |
| --------- | ------------- | --------------- | ----------- |

✅ Conda Setup

```bash
conda create -n DRAEM python=3.8
conda activate DRAEM
conda install pytorch==1.10.0 torchvision==0.11.0 torchaudio==0.10.0 cudatoolkit=11.3 -c pytorch -c conda-forge
```

📦 Install Dependencies

```bash
pip install opencv-python -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install opencv-python-headless -i https://pypi.tuna.tsinghua.edu.cn/simple

pip install imgaug -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install tensorboard -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install setuptools==59.5.0 -i https://pypi.tuna.tsinghua.edu.cn/simple  # AttributeError: module 'distutils' has no attribute 'version'
pip install scikit-learn -i https://pypi.tuna.tsinghua.edu.cn/simple

pip install PyQt5 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install tqdm -i https://pypi.tuna.tsinghua.edu.cn/simple
```

⚠️ Known Issues

❌ qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.

❌ This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.

❌ Available platform plugins are: eglfs, linuxfb, minimal, minimalegl, offscreen, vnc, wayland-egl, wayland, wayland-xcomposite-egl, wayland-xcomposite-glx, webgl, xcb.
sudo apt install libxcb-xinerama0

------

## Informer

| 💻 Windows／🐧 Ubuntu | 🐍 Python 3.8 | 🔥 PyTorch 1.10.0 | 🧠 CUDA 11.3 |
| ------------------- | ------------ | ---------------- | ----------- |

✅ Conda Setup

```bash
conda create -n Informer python=3.8
conda activate Informer
conda install pytorch==1.10.0 torchvision==0.11.0 torchaudio==0.10.0 cudatoolkit=11.3 -c pytorch -c conda-forge
```


📦 Install Dependencies

```bash
pip install matplotlib -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install pandas -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install scikit-learn -i https://pypi.tuna.tsinghua.edu.cn/simple
```


⚠️ Known Issues



------

## t-PatchGNN

| 💻 Windows | 🐍 Python 3.12 | 🔥 PyTorch 2.4.1 | 🧠 CUDA 12.4 |
| --------- | ------------- | --------------- | ----------- |

✅ Conda Setup

```bash
conda create -n t-PatchGNN python=3.12
conda activate t-PatchGNN
conda install pytorch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1 pytorch-cuda=12.4 -c pytorch -c nvidia
```


📦 Install Dependencies

```bash
pip install reformer-pytorch==1.4.4 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install scikit-learn -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install tqdm -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install pandas -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install psycopg2-binary -i https://pypi.tuna.tsinghua.edu.cn/simple
```


⚠️ Known Issues



------

## AdaPTS


| 💻 Windows／🐧 Ubuntu | 🐍 Python 3.11 | 🔥 PyTorch 2.4.1 | 🧠 CUDA 12.4 |
| ------------------- | ------------- | --------------- | ----------- |

✅ Conda Setup

```bash
conda create -n AdaPTS python=3.11
conda activate AdaPTS
conda install pytorch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1 pytorch-cuda=12.4 -c pytorch -c nvidia
conda install pytorch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1 pytorch-cuda=12.1 -c pytorch -c nvidia
```


📦 Install Dependencies

```bash
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install momentfm==0.1.4 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install uni2ts==1.2.0 -i https://pypi.tuna.tsinghua.edu.cn/simple
```


⚠️ Known Issues

❌ ModuleNotFoundError: No module named 'momentfm' (Available versions: 0.1.4, 0.1.3, 0.1.1, 0.1)

❌ ModuleNotFoundError: No module named 'uni2ts' (Available versions: 1.2.0, 1.1.1, 1.1.0)

⚠️ momentfm 0.1.4 has requirement numpy==1.25.2, but you have numpy 1.26.4.

------

