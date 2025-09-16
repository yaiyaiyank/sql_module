from pathlib import Path
from funcs import execute_cmd, get_top_modules_path_for_current_name, is_init_making_main_py
import argparse

TOP_MODULES_NAME = "yai"


def init_env():
    # venvを作ったりしてくれる
    execute_cmd("uv sync")

    # 開発用にトップモジュールのパスを通す (pthってなんかAIのモデルのファイルみたいだね)
    pth_file = Path().cwd() / ".venv" / "Lib" / "site-packages" / "mymodules.pth"
    mymodules_path = get_top_modules_path_for_current_name(TOP_MODULES_NAME)
    if not mymodules_path is None:
        pth_file.write_text(mymodules_path.__str__(), encoding="utf-8")

    # 依存ライブラリがあったらインストール
    requirement_txt = Path().cwd() / "requirement.txt"
    if requirement_txt.exists():
        execute_cmd("uv add -r requirements.txt -U")

    # 開発用にプロジェクト名と同名のフォルダとその中にある__init__.pyを作成する
    init_py = Path().cwd() / f"{Path().cwd().name}" / "__init__.py"
    init_py.parent.mkdir(parents=True, exist_ok=True)
    if not init_py.exists():
        init_py.write_text("from pathlib import Path", encoding="utf-8")

    # 開発用にuvによって生成されたmain.pyを削除
    main_py = Path().cwd() / "main.py"
    if is_init_making_main_py(main_py):
        main_py.unlink()

    # config.tomlに書き込む初期設定があったら記入
    config_toml_path = Path().cwd() / "config.toml"
    if not config_toml_path.exists():
        pass


def update_env():
    # 依存ライブラリの最新をインストール
    requirement_txt = Path().cwd() / "requirement.txt"
    if requirement_txt.exists():
        execute_cmd("uv add -r requirements.txt -U")

    # リポジトリを最新へ
    execute_cmd("git pull --rebase")


parser = argparse.ArgumentParser()
parser.add_argument("-e", "--env", type=str, default="init")
args = parser.parse_args()

if args.env == "init":
    init_env()
if args.env == "update":
    update_env()
