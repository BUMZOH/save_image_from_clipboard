from pathlib import Path
from datetime import datetime
from PIL import ImageGrab
import subprocess

def save_clipboard_image_to_pictures():
    # ピクチャフォルダのパスを取得
    pictures_path = Path.home() / "Pictures"

    # フォルダが存在しない場合は作成
    pictures_path.mkdir(parents=True, exist_ok=True)

    # クリップボードから画像を取得
    img = ImageGrab.grabclipboard()

    if img is None:
        print("クリップボードに画像がありません。")
        input("何かキーを押してください")
        return

    # 日時付きのファイル名を生成
    filename = f"clipboard_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    save_path = pictures_path / filename

    # 画像を保存
    img.save(save_path, "PNG")
    print(f"画像を保存しました: {save_path}")

    # 保存後にピクチャフォルダをエクスプローラーで開く
    subprocess.run(["explorer", str(pictures_path)])

if __name__ == "__main__":
    save_clipboard_image_to_pictures()
