# save_image_from_clipboard

クリップボードにコピーされている画像をPNGファイルとして保存するツールです。

保存先は Windows の **ピクチャフォルダ** (`%USERPROFILE%\Pictures`) です。

---

## 動作環境

- Windows
- Python 3.10以上（推奨）
- Pillow

---

## インストール

```bash
pip install pillow
```

---

## 使い方

### 通常実行

```bash
python main.py
```

クリップボード画像を保存し、保存後にピクチャフォルダを開きます。

---

### オプション

#### `-o`, `--open-only`

画像を保存せず、ピクチャフォルダだけを開きます。

```bash
python main.py -o
```

または

```bash
python main.py --open-only
```

---

#### `-n`, `--no-new-folder`

画像は保存しますが、保存後にフォルダを開きません。

```bash
python main.py -n
```

または

```bash
python main.py --no-new-folder
```

---

#### `-h`, `--help`

ヘルプを表示します。

```bash
python main.py -h
```

---

## 保存ファイル名

保存される画像ファイル名は次の形式です。

```
clipboard_YYYYMMDD_HHMMSS.png
```

例

```
clipboard_20260801_103015.png
```

---

## 保存先

```
C:\Users\<ユーザー名>\Pictures
```

---

## エラー

クリップボードに画像が存在しない場合は次のメッセージを表示します。

```
クリップボードに画像がありません。
```

画像ファイルは保存されません。

---

## 使用ライブラリ

### 標準ライブラリ

- argparse
- datetime
- pathlib
- subprocess

### 外部ライブラリ

- Pillow

---

## ライセンス

MIT License