from allosaurus.app import read_recognizer
import json
from g2p_en import G2p
from ipapy.arpabetmapper import ARPABETMapper
import enchant


def DPR(filename):
    print("in fucntion")
    model = read_recognizer()
    print(filename)
    phones = model.recognize(filename)  # phoneme conversion of audio
    print(phones)
    files = filename.split(".")
    target = files[0]
    target = target.replace("_", "")
    print(target)
    g2p = G2p()
    accPhones = g2p(target)  # the target is filename
    amapper = ARPABETMapper()
    readablePhones = amapper.map_unicode_string(phones,
                                                ignore=True)  # ipa symbols are not easy to process so we map them into arpabet
    accPhone=''.join([str(elem) for elem in accPhones])
    ans = enchant.utils.levenshtein(accPhone, readablePhones)
    print("distance: ", ans)
    ratio = ((ans) / (max(len(accPhone), len(readablePhones)))) * 100
    print(ratio)
    similarity = round(100 - ratio, 2)
    reply = {'Target Phones': accPhones,
             'Spoken Phones in IPA': phones,
             'Spoken Phones in ARPABET': readablePhones,
             'Similarity': similarity}

    return json.dumps(reply)

