from utils.script_runner import install_packages


if __name__ == '__main__':
    pkgs = [
        "psutil",
        "gputil",
        "py-cpuinfo",

        "easydict",
        "opencv-python",
        "scikit-learn",
    ]
    USE_MIRROR = True
    install_packages(pkgs, use_mirror=USE_MIRROR)
