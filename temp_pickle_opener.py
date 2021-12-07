import pickle
import numpy as np

# with open('./models/basicModel_f_lbs_10_207_0_v1.0.0.pkl','rb') as fr:
#     data = pickle.load(fr)

# for key, value in data.items():
#     print(key)


# print('-----------------------')
print(pickle.format_version)

# with open('./models/gBR_sBM_cAll_d04_mBR0_ch01.pkl','rb') as fr:
#     data2 = pickle.load(fr)

# for key, value in data2.items():
#     print(key)

# pickle.dump(data2, open('dance.pkl','wb'), protocol=2)


# import pickle
# with open("a.pkl", "rb") as f:
#     w = pickle.load(f)

# pickle.dump(w, open("a_py2.pkl","wb"), protocol=2)


with open('./models/dance.pkl','rb') as fr:
    data2 = pickle.load(fr)

for key, value in data2.items():
    print(key)