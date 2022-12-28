import os
# import glob
# import pandas as pd
def get_dir(dir):
    p = []
    for root, dirs, files in os.walk(dir, topdown=False):
        for name in files:
                if name != '.DS_Store':
                    if not ('ipynb' in name):
                        p.append(os.path.join(root, name))
    return p
# li = get_dir('./Datathon Final dataset/Central election 2074/')
li = get_dir('./Datathon Final dataset/state election 2074/')
for files in li:
    # if not ('ipynb' in files):
    print(files)

# df_append = pd.DataFrame()
# #append all files together
# for file in li:
#             df_temp = pd.read_csv(file)
#             df_append = df_append.append(df_temp, ignore_index=True)
# df_append
