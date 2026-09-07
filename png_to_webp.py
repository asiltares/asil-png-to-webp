import os
import sys
from tkinter import Tk, filedialog

from PIL import Image

QUALITY = 90

MESSAGES = {
    "tr": {
        "no_png": "Klasorde png yok: {folder}",
        "found": "{count} adet png dosya bulundu.",
        "confirm": "Bu png dosyalarini webp'ye cevirmek istediginize emin misiniz? (y/n): ",
        "cancelled": "Islem iptal edildi.",
        "converted": "Cevrildi: {name} -> {dst}",
        "done": "Bitti. {count} dosya cevrildi.",
        "delete_prompt": "Eski png dosyalari silinsin mi? (y/n): ",
        "deleted": "{count} png dosyasi silindi.",
        "kept": "Png dosyalari korundu.",
        "no_folder": "Klasor secilmedi.",
        "pick_title": "PNG klasoru sec",
    },
    "en": {
        "no_png": "No png files in folder: {folder}",
        "found": "{count} png files found.",
        "confirm": "Are you sure you want to convert these png files to webp? (y/n): ",
        "cancelled": "Operation cancelled.",
        "converted": "Converted: {name} -> {dst}",
        "done": "Done. {count} files converted.",
        "delete_prompt": "Delete original png files? (y/n): ",
        "deleted": "{count} png files deleted.",
        "kept": "Png files kept.",
        "no_folder": "No folder selected.",
        "pick_title": "Select PNG folder",
    },
}


def pick_language() -> dict:
    while True:
        choice = input("Dil sec / Select language (tr/en): ").strip().lower()
        if choice in MESSAGES:
            return MESSAGES[choice]


def convert_folder(folder: str, msg: dict) -> None:
    png_files = [f for f in os.listdir(folder) if f.lower().endswith(".png")]

    if not png_files:
        print(msg["no_png"].format(folder=folder))
        return

    print(msg["found"].format(count=len(png_files)))

    answer = input(msg["confirm"]).strip().lower()
    if answer != "y":
        print(msg["cancelled"])
        return

    converted_src_paths = []

    for name in png_files:
        src = os.path.join(folder, name)
        dst = os.path.join(folder, os.path.splitext(name)[0] + ".webp")
        with Image.open(src) as img:
            img.save(dst, "webp", quality=QUALITY)
        print(msg["converted"].format(name=name, dst=os.path.basename(dst)))
        converted_src_paths.append(src)

    print(msg["done"].format(count=len(png_files)))

    delete_answer = input(msg["delete_prompt"]).strip().lower()
    if delete_answer == "y":
        for src in converted_src_paths:
            os.remove(src)
        print(msg["deleted"].format(count=len(converted_src_paths)))
    else:
        print(msg["kept"])


def pick_folder(msg: dict) -> str:
    root = Tk()
    root.withdraw()
    folder = filedialog.askdirectory(title=msg["pick_title"])
    root.destroy()
    return folder


if __name__ == "__main__":
    lang_msg = pick_language()
    target = sys.argv[1] if len(sys.argv) > 1 else pick_folder(lang_msg)

    if not target:
        print(lang_msg["no_folder"])
        sys.exit(1)

    convert_folder(target, lang_msg)
