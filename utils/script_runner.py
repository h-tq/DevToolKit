import sys
import subprocess
import subprocess


def install_packages(packages, use_mirror=True):
    mirror = " -i https://pypi.tuna.tsinghua.edu.cn/simple" if use_mirror else ""

    for pkg in packages:
        command = f"pip install {pkg}{mirror}"
        try:
            subprocess.check_call(command, shell=True)
            print(f"✅ Successfully installed: {pkg}\n")
        except subprocess.CalledProcessError as e:
            print(f"❌ Error occurred while executing: {pkg}")
            print(e, end='\n\n')


class ScriptRunner:
    def __init__(self, scripts: list, max_epochs: int = 1):
        self.scripts = scripts
        self.max_epochs = max_epochs

    @staticmethod
    def print_(message, end="\n"):
        print(f"\033[3m\033[30m\033[47m{message}\033[0m", end=end)

    def run_script(self, script):
        try:
            result = subprocess.run(["python", script], check=True, text=True)
            if result.stdout:
                self.print_(f"脚本输出: {result.stdout}")
        except subprocess.CalledProcessError as e:
            self.print_(f"脚本运行出错: {e.stderr}")

    def run_all(self):
        for script in self.scripts:
            if script in sys.argv[0]:
                self.print_(f"禁止调用自身脚本: {sys.argv[0]}")
                continue
            for epoch in range(self.max_epochs):
                self.print_(f"[{script}]: Starting training for epoch {epoch + 1}...")
                self.run_script(script)
                self.print_(f"[{script}]: Training for epoch {epoch + 1} completed.", end='\n\n')
