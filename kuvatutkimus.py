# LATAA SUOMENKIELINEN SANASTO
from python_funktiot import *
from kuvatutkimus_kirjasto import *

# ASENNUKSET
asenna_graafinen_ohjelma()
asenna_python_image_library()
asenna_opencv()

# OPENCV
def kuvan_avaaminen_opencv():
    hyljekuva2 = cv_lataa_kuvatiedosto_mv("hylkeet.jpg")
    cv_kuvan_piirto(hyljekuva2)
    cv_tallenna_kuva(hyljekuva2, "kivat_hylkeet.jpg")
    cv_sulje_ikkunat()

def cv_hae_tiedosto():
    tiedoston_polku = valitse_tiedosto("jpg", oma_ohjelma)
    kirjoita(tiedoston_polku)
    hyljekuva = cv_lataa_kuvatiedosto(tiedoston_polku)
    cv_kuvan_piirto(hyljekuva)

def cv_kuvan_blurraus():
    hyljekuva1 = cv_lataa_kuvatiedosto_mv("hylkeet.jpg")
    hyljekuva_blur = cv_blurraa_kuva(hyljekuva1)
    cv_kuvan_piirto(hyljekuva_blur)

def sulje_ohjelma(ohjelma):
    if ohjelma.yesno("Sulje", "Haluatko varmasti lopettaa?"):
        ohjelma.destroy()


def ohjelma():
    # LUO OHJELMA
    oma_ohjelma = luo_ohjelma("Kuvanmuokkaus 0.1")
    aseta_ikkunan_koko(oma_ohjelma,800,600)
    # LUO PAINIKKEET
    painike_kuvan_avaamiseen = luo_painike("Avaa kuvatiedosto", cv_kuvan_blurraus, oma_ohjelma )
    painike_ohjelman_sulkemiseen = luo_painike("Sulje ohjelma", lambda:sulje_ohjelma(oma_ohjelma), oma_ohjelma )

    # LUO PIIRTO
    piirto = luo_piirturi(oma_ohjelma)
    suorakaide(piirto,10, 10, 60, 60)

    # KUVAN PIIRTO VAATII PIL KIRJASTON
    hkuva = lataa_kuvatiedosto("hylkeet.jpg")
    kuvanpiirto(oma_ohjelma, hkuva)
    # PIIRRÄ OHJELMA
    avaa_ikkunassa(oma_ohjelma)


ohjelma()


# PIL = PILLOW LIBRARY
#p = PIL()
# PIL
# hyljekuva = p.lataa_kuvatiedosto(tiedostoPolku)
# p.kuvanpiirto(oma_ohjelma, hyljekuva)

# def hae_tiedosto():
#     tiedoston_polku = valitse_tiedosto("jpg", oma_ohjelma)
#     kirjoita(tiedoston_polku)
#     lataa_ja_avaa_kuva(tiedoston_polku)

# hyljekuva = lataa_kuvatiedosto("hylkeet.jpg")
# mv_hyljekuva = mustavalkoinen(hyljekuva)
# muokattu_mv_hyljekuva = tarkenna(mv_hyljekuva,2.2)
# kuvanpiirto(oma_ohjelma, muokattu_mv_hyljekuva)
# avaa_ikkunassa(oma_ohjelma)




# # OPENCV VIDEO
# import cv2
# import numpy as np
#
# cap = cv2.VideoCapture(0)
#
# while(1):
#
#     # Take each frame
#     _, frame = cap.read()
#
#     # Convert BGR to HSV
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#
#     # define range of blue color in HSV
#     lower_blue = np.array([110,50,50])
#     upper_blue = np.array([130,255,255])
#
#     # Threshold the HSV image to get only blue colors
#     mask = cv2.inRange(hsv, lower_blue, upper_blue)
#
#     # Bitwise-AND mask and original image
#     res = cv2.bitwise_and(frame,frame, mask= mask)
#
#     cv2.imshow('frame',frame)
#     cv2.imshow('mask',mask)
#     cv2.imshow('res',res)
#     k = cv2.waitKey(5) & 0xFF
#     if k == 27:
#         break
#
# cv2.destroyAllWindows()




# # KIRJOITA TEKSTI
# teksti = "Python kuvanmuokkausohjelma"
# kirjoita(teksti)
#
# tiedostonMuoto = tiedostoMuoto("hylkeet.jpg")
# kirjoita(tiedostonMuoto)
#
#
# #ASENNA TARVITTAVAT KIRJASTOT (PIL)
# asennaKuvanmuokkaus()
# #tuetutTiedostomuodot()
#
# # LATAA JA AVAA KUVATIEDOSTO
# hyljekuva = lataaKuva("hylkeet.jpg")
# avaaKuva(hyljekuva)
#
# # MUUTA KUVA MUSTAVALKOISEKSI
# mv_hyljekuva = mustavalkoinen(hyljekuva)
# # TAI
# #mv_hyljekuva = mustavalkoinen(lataaKuva("hylkeet.jpg"))
#
# # AVAA MUOKATTU KUVATIEDOSTO
# avaaKuva(mv_hyljekuva)
