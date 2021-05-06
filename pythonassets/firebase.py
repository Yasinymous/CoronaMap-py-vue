import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the application default credentials
cred = credentials.Certificate('fire.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

def SetCity(DataArray)
    doc_ref = db.collection('cities').document()
    doc_ref.set({
        u'name': DataArray[0]
        u'date': DataArray[1]
        u'vaka': DataArray[2]
        u'id': DataArray[3]
    })


def SetCountry(DataArray)
    doc_ref = db.collection('country').document()
    doc_ref.set({
        u'tarih': DataArray[0]
        u'gunluk_vaka': DataArray[1]
        u'gunluk_hasta': DataArray[2]
        u'gunluk_vefat': DataArray[3]
        u'gunluk_iyilesen': DataArray[4]
        u'agir_hasta_sayisi': DataArray[5]
        u'toplam_test': DataArray[6]
        u'toplam_hasta': DataArray[7]
        u'toplam_vefat': DataArray[8]
        u'toplam_iyilesen': DataArray[9]
        u'toplam_yogun_bakim': DataArray[10]
        u'toplam_entube': DataArray[11]
        u'hastalarda_zaturre_oran': DataArray[12]
        u'yatak_doluluk_orani': DataArray[13]
        u'eriskin_yogun_bakim_doluluk_orani': DataArray[14]
        u'ventilator_doluluk_orani': DataArray[15]
        u'ortalama_filyasyon_suresi': DataArray[16]
        u'ortalama_temasli_tespit_suresi': DataArray[17]
        u'filyasyon_orani': DataArray[18]
        u'id': DataArray[19]
    })
