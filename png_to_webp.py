import os
import sys
from tkinter import Tk, filedialog

from PIL import Image

QUALITY = 90

MESSAGES = {
    "tr": {
        "no_png": "Klasorde png yok: {folder}",
        "found": "{count} adet png dosya bulundu.",
        "subfolder_found": "Bu klasorun icinde {count} adet png var, fakat alt klasorlerde de {sub_count} adet png bulundu. Onlar da cevrilsin mi? (y/n): ",
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
        "subfolder_found": "Found {count} png files in this folder, but also {sub_count} png files in subfolders. Convert those too? (y/n): ",
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


def find_pngs(folder: str) -> list:
    top_level = [os.path.join(folder, f) for f in os.listdir(folder) if f.lower().endswith(".png")]

    nested = []
    for root, _dirs, files in os.walk(folder):
        if root == folder:
            continue
        for f in files:
            if f.lower().endswith(".png"):
                nested.append(os.path.join(root, f))

    return top_level, nested


def convert_folder(folder: str, msg: dict) -> None:
    top_level_pngs, nested_pngs = find_pngs(folder)

    if not top_level_pngs and not nested_pngs:
        print(msg["no_png"].format(folder=folder))
        return

    png_paths = list(top_level_pngs)

    if top_level_pngs:
        print(msg["found"].format(count=len(top_level_pngs)))

    if nested_pngs:
        sub_answer = input(
            msg["subfolder_found"].format(count=len(top_level_pngs), sub_count=len(nested_pngs))
        ).strip().lower()
        if sub_answer == "y":
            png_paths.extend(nested_pngs)

    if not png_paths:
        print(msg["no_png"].format(folder=folder))
        return

    answer = input(msg["confirm"]).strip().lower()
    if answer != "y":
        print(msg["cancelled"])
        return

    converted_src_paths = []

    for src in png_paths:
        dst = os.path.splitext(src)[0] + ".webp"
        with Image.open(src) as img:
            img.save(dst, "webp", quality=QUALITY)
        print(msg["converted"].format(name=os.path.basename(src), dst=os.path.basename(dst)))
        converted_src_paths.append(src)

    print(msg["done"].format(count=len(png_paths)))

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
