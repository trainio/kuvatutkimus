


# input returns string
# def
#     input()


# KÄYTTÖLIITTYMÄ
def asenna_graafinen_ohjelma():
    global App
    global Drawing
    global Picture
    global PushButton
    global Text
    global painike
    from guizero import App, Drawing, Picture, Text
    from guizero import PushButton as painike


def luo_ohjelma(ohjelman_nimi):
    ohjelma = App(ohjelman_nimi, bg="white")
    # ohjelma.info("info", ohjelman_nimi+"\nKuvataideakatemia / Tuomo Rainio\n2020")
    return ohjelma

def aseta_ikkunan_koko(ohjelma, leveys, korkeus):
    ohjelma.width = leveys
    ohjelma.height = korkeus

def avaa_ikkunassa(ohjelma):
    ohjelma.display()

# def sulje_ohjelma(ohjelma):
#     if ohjelma.yesno("Close", "Do you want to quit?"):
#         ohjelma.destroy()

def valitse_tiedosto(muoto, ohjelma):
    file_name = ohjelma.select_file(filetypes=[["All files", "*.*"], [f"{muoto.upper()} file", f"*.{muoto.lower()}"]])
    return file_name

def luo_painike(teksti,funktio,ohjelma):
    p = painike(ohjelma,command=funktio, text=teksti, align="top")
    return p

def tekstin_piirto(ohjelma):
    teksti = Text(ohjelma)
    return teksti

def luo_piirturi(ohjelma):
    return Drawing(ohjelma)

def suorakaide(piirto,x,y,w,h):
    c = (255, 0, 0)
    piirto.rectangle(x, y, w, h, c)

def kuvanpiirto(ohjelma, kuva):
    return Picture(ohjelma,kuva)

########################################################################

# Kuvankäsittely OPENCV
def asenna_opencv():
    global cv
    import sys
    import cv2 as cv
    import numpy as np
    from cv2 import imread as lue # EI TOIMI
    from cv2 import addWeighted as sekoitus
    # from matplotlib import pyplot as plt

def cv_lataa_kuvatiedosto(tiedostopolku):
    img = cv.imread(tiedostopolku)
    return img

def cv_lataa_kuvatiedosto_mv(tiedostopolku):
    img = cv.imread(tiedostopolku, 0)
    return img

def cv_kuvan_piirto(kuvatiedosto):
    cv.imshow(str(kuvatiedosto), kuvatiedosto)

def cv_tallenna_kuva(kuvatiedosto, tiedostopolku):
    cv.imwrite(tiedostopolku,kuvatiedosto)

def cv_sulje_kuva(ikkunan_nimi):
    cv.destroyWindow(ikkunan_nimi)

def cv_sulje_ikkunat():
    cv.waitKey(0)
    cv.destroyAllWindows()

def cv_painike_komento():
    k = cv.waitKey(0)
    return k

def cv_blurraa_kuva(kuvatiedosto):
    blur = cv.GaussianBlur(kuvatiedosto,(5,5),0)
    return blur

def cv_sekoita_kuvat(kuvatiedosto1, osuus1, kuvatiedosto2, osuus2):
    # sekoituksen osuudet 0.0-1.0, mistä yhteenlaskettuna 1.0
    sekoitus = cv.addWeighted(kuvatiedosto1,osuus1,kuvatiedosto2,osuus2,0)
    return sekoitus

########################################################################

# Kuvankäsittely PIL Python Image Library

def asenna_python_image_library():
    global Image
    from PIL import Image
    global ImageEnhance
    from PIL import ImageEnhance

def lataa_kuvatiedosto(tiedosto):
    img = Image.open(tiedosto)
    return img

def kuvatiedosto(tiedosto):
    try:
        img = Image.open(tiedosto)
        return img
    except IOError:
        print("Käyttäjä ei avannut kuvaa!")

def avaa_kuva(kuva):
    kuva.show()

def lataa_ja_avaa_kuva(tiedostoPolku):
    kuva = lataa_kuvatiedosto(tiedostoPolku)
    avaa_kuva(kuva)

def muokkaaKontrastia(kuva, voimakkuus):
    enh = ImageEnhance.Contrast(kuva).enhance(voimakkuus)
    return enh

def tarkenna(kuva, voimakkuus):
    img = ImageEnhance.Sharpness(kuva).enhance(voimakkuus)
    return img

def tarkennettu(kuva, voimakkuus):
    img = ImageEnhance.Sharpness(kuva).enhance(voimakkuus)
    return img

def mustavalkoinen(kuva):
    img = ImageEnhance.Color(kuva).enhance(0)
    return img

def tuetutTiedostomuodot():
    tuetutMuodot = ["BMP", "DIB", "EPS", "GIF", "ICNS", "ICO", "IM", "JPEG", "JPEG", "2000", "MSP", "PCX", "PNG", "PPM", "SGI", "SPIDER", "TGA", "TIFF", "WebP", "XBM"]
    print("Fully supported formats:")
    print(f"{tuetutMuodot}")


# TIEDOSTOJEN KÄSITTELY
def tiedostomuoto(tiedosto):
    import filetype
    kind = filetype.guess(tiedosto)
    if kind is None:
        print('Cannot guess file type!')
        return

    print('File extension: %s' % kind.extension)
    print('File MIME type: %s' % kind.mime)
    return kind.extension
