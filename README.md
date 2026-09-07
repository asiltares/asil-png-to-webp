# PNG → WebP Converter

[🇹🇷 Türkçe](#-türkçe) | [🇬🇧 English](#-english)

---

# 🇹🇷 Türkçe

## PNG → WebP Dönüştürücü

FiveM projelerimde envanter görsellerinin hayvan gibi yer kaplamasından ve sunucu yüklenme sürelerini felç etmesinden gına geldiği için oturup böyle ufak bir kod yazdım xd.

Script, seçtiğiniz klasörde bulunan tüm `.png` dosyalarını `.webp` formatına dönüştürerek dosya boyutlarını küçültmenize yardımcı olur.

## Özellikler

* Seçilen klasördeki PNG dosyalarını otomatik olarak bulur.
* PNG görsellerini WebP formatına dönüştürür.
* Dosya boyutlarını azaltmaya yardımcı olur.
* FiveM inventory ve UI görselleri için uygundur.
* Klasör seçme penceresiyle çalıştırılabilir.
* Klasör yolu doğrudan komut satırından verilebilir.
* Basit ve hızlı kullanım sunar.

## Gereksinimler

* **Python:** 3.8 veya üzeri
* **Kütüphane:** Pillow

Pillow kurulumu:

```bash id="w2w2nm"
pip install Pillow
```

## Kullanım

### Klasör seçme penceresi ile

Scripti herhangi bir klasör yolu belirtmeden çalıştırın:

```bash id="5zkx9c"
python png_to_webp.py
```

Açılan pencereden PNG dosyalarının bulunduğu klasörü seçin.

### Klasör yolunu doğrudan belirterek

```bash id="3mhd0k"
python png_to_webp.py "C:\ornek\klasor\yolu"
```

Örnek:

```bash id="xn71te"
python png_to_webp.py "C:\FiveM\server-data\resources\inventory\html\images"
```

## Neden WebP?

WebP, birçok durumda PNG formatına kıyasla daha düşük dosya boyutları sunabilir.

Özellikle yüzlerce item görselinin bulunduğu FiveM inventory sistemlerinde toplam dosya boyutunun ciddi şekilde azaltılmasına yardımcı olabilir.

Daha küçük görseller:

* Daha düşük resource boyutu
* Daha az veri transferi
* Daha hızlı UI yüklenmesi
* Daha optimize edilmiş FiveM paketleri

anlamına gelebilir.

## Not

Dönüştürme işleminden sonra kullandığınız inventory veya UI sisteminde görsel yollarının `.png` yerine `.webp` olarak değiştirilmesi gerekebilir.

Önemli dosyalarınız varsa toplu dönüştürme işleminden önce yedek almanız önerilir.

---

# 🇬🇧 English

## PNG → WebP Converter

I got tired of inventory images taking up a ridiculous amount of space in my FiveM projects and absolutely destroying server loading times, so I sat down and wrote this little script xd.

The script converts all `.png` files inside the selected folder into `.webp` format, helping reduce image file sizes.

## Features

* Automatically detects PNG files inside the selected folder.
* Converts PNG images to WebP.
* Helps reduce image file sizes.
* Suitable for FiveM inventory and UI assets.
* Supports a folder selection window.
* Supports specifying a folder path directly from the command line.
* Simple and fast to use.

## Requirements

* **Python:** 3.8 or newer
* **Library:** Pillow

Install Pillow:

```bash id="csgw0z"
pip install Pillow
```

## Usage

### Using the folder selection window

Run the script without specifying a folder path:

```bash id="pzwhvp"
python png_to_webp.py
```

Select the folder containing your PNG files from the window that appears.

### Specifying a folder path directly

```bash id="1pgqcv"
python png_to_webp.py "C:\example\folder\path"
```

Example:

```bash id="irpnha"
python png_to_webp.py "C:\FiveM\server-data\resources\inventory\html\images"
```

## Why WebP?

WebP can provide significantly smaller file sizes compared to PNG in many cases.

This can be especially useful for FiveM inventory systems containing hundreds of item images.

Smaller images can result in:

* Smaller resource size
* Reduced data transfer
* Faster UI loading
* Better optimized FiveM resources

## Note

After converting your images, you may need to update image paths in your inventory or UI system from `.png` to `.webp`.

It is recommended to create a backup before performing bulk conversions on important files.

---

## License

Free to use in your FiveM projects and other projects.

If this project helped you, feel free to leave a ⭐.
