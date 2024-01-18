import numpy as np

str = "abcdefghijklmnopqrstuvwxyz"

crypt = "Obr gvcizr ks kwb hvs rom, hvs Tcifhv ct Xizm kwzz bc zcbusf ps ybckb og ob Oasfwqob vczwrom, pih og hvs rom hvs kcfzr rsqzofsr wb cbs jcwqs: \"Ks kwzz bch uc eiwshzm wbhc hvs bwuvh!\" Ks kwzz bch jobwgv kwhvcih o twuvh! Ks'fs ucwbu hc zwjs cb! Ks'fs ucwbu hc gifjwjs! Hcrom ks qszspfohs cif Wbrsdsbrsbqs Rom"

# for i in range(1,26):
#     new_str = ""
#     for c in crypt.lower():
#         try:
#             new_str+= str[(str.index(c)+i)%26]
#         except ValueError:
#             new_str += c
#     print(new_str,end = "\n")

result = "and should we win the day, the fourth of july will no longer be known as an american holiday, but as the day the world declared in one voice: \"we will not go quietly into the night!\" we will not vanish without a fight! we're going to live on! we're going to survive! today we celebrate our independence day"

f = open("./crypt.txt", "r")
count_dict = {s:0 for s in str}
for c in f.read().lower():
    try:
        count_dict[c]+=1
    except KeyError:
        pass
print(count_dict)
