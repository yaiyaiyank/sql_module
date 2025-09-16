import subprocess
from subprocess import CompletedProcess
from pathlib import Path


def execute_cmd(command, console_display=True) -> CompletedProcess:
    if console_display:
        # コンソールに文字を出す
        result = subprocess.run(
            command, shell=True, text=True, encoding="utf8", stdin=subprocess.PIPE, stdout=subprocess.PIPE
        )
    else:
        # コンソールに文字を出さない
        result = subprocess.run(command, shell=True, capture_output=True, text=True, encoding="utf8")
    return result


def get_top_modules_path_for_current_name(dir_name: str) -> Path | None:
    """トップモジュールが含まれるパスを返す"""
    search_path = Path().cwd()
    for _ in range(20):
        search_path = search_path.parent
        top_modules_path = search_path / "yai"
        if top_modules_path.exists():
            print(f"トップモジュールが見つかりました。パス: {top_modules_path}")
            return search_path
    else:
        return None


def is_init_making_main_py(main_py: Path) -> bool:
    """初期生成のmain.pyがあるかどうか"""
    # ruffによって改行とかインデントが自由に行われるのでreplace
    judge_main_script = f"""def main():
        print("Hello from {Path().cwd().name.replace("_", "-")}!")

    if __name__ == "__main__":
        main()""".replace("\n", "").replace(" ", "")

    if not main_py.exists():
        return False

    with main_py.open("r", encoding="utf-8") as f:
        main_script = f.read().replace("\n", "").replace(" ", "")

    if judge_main_script == main_script:
        print("main.pyが見つかりました。")
        return True
    return False
