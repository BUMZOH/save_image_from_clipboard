from argparse import ArgumentParser
from datetime import datetime
from pathlib import Path
import subprocess

from PIL import ImageGrab, Image

class PauseArgumentParser(ArgumentParser):
    """終了前にEnterキーの入力を待つArgumentParser。"""

    def exit(
        self,
        status: int = 0,
        message: str | None = None,
    ) -> None:
        if message:
            self._print_message(message)

        input("\nEnterキーを押すと終了します。")
        raise SystemExit(status)


def create_parser() -> ArgumentParser:
    """コマンドライン引数を解析するArgumentParserを作成する。"""
    parser = PauseArgumentParser(
        description=(
            "クリップボード画像をピクチャフォルダへ保存し、"
            "必要に応じてフォルダを開きます。"
        ),
    )

    option_group = parser.add_mutually_exclusive_group()

    option_group.add_argument(
        "-o",
        "--open-only",
        action="store_true",
        help="画像を保存せず、ピクチャフォルダを開くだけにします。",
    )
    option_group.add_argument(
        "-n",
        "--no-new-folder",
        action="store_true",
        help="処理後にピクチャフォルダを開きません。",
    )

    return parser


def get_pictures_path() -> Path:
    """ピクチャフォルダのパスを取得し、存在しなければ作成する。"""
    pictures_path = Path.home() / "Pictures"
    pictures_path.mkdir(parents=True, exist_ok=True)
    return pictures_path


def open_folder(folder_path: Path) -> None:
    """指定したフォルダをWindowsエクスプローラーで開く。"""
    subprocess.run(
        ["explorer", str(folder_path)],
        check=False,
    )


def save_clipboard_image(pictures_path: Path) -> bool:
    """クリップボード画像をPNG形式で保存する。"""
    clipboard_data = ImageGrab.grabclipboard()

    if not isinstance(clipboard_data, Image.Image):
        print("クリップボードに画像がありません。")
        input("\nEnterキーを押すと終了します。")
        return False

    filename = f"clipboard_{datetime.now():%Y%m%d_%H%M%S}.png"
    save_path = pictures_path / filename

    clipboard_data.save(save_path, "PNG")
    print(f"画像を保存しました: {save_path}")
    return True


def main() -> None:
    """コマンドライン引数に応じて処理を実行する。"""
    parser = create_parser()
    args = parser.parse_args()

    pictures_path = get_pictures_path()

    # -o: 画像を保存せず、フォルダを開くだけ
    if args.open_only:
        open_folder(pictures_path)
        return

    image_saved = save_clipboard_image(pictures_path)

    # 保存に成功し、-nが指定されていない場合だけフォルダを開く
    if image_saved and not args.no_new_folder:
        open_folder(pictures_path)


if __name__ == "__main__":
    main()