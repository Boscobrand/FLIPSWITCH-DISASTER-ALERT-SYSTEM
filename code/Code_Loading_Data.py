#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import re
import os
import sys
script, indir, outfile = sys.argv
rootdir = indir
for root, subFolders, files in os.walk(rootdir):
  for subdir in subFolders:
    for root2, subFolders2, bzfiles in os.walk(os.path.join(root, subdir)):
      for bzfile in bzfiles:
        infile = os.path.join(root2, bzfile)
        decompfile = re.sub(".bz2$", "",  infile)
        os.system("bunzip2 " + infile)
#        decompfile = infile
        df = pd.read_json(decompfile, lines=True)
        df1 = df[['text']]
        df1.drop_duplicates(inplace=True)
        en_list=[]
        for index in df1.index :
          if df['lang'][index]== 'en':
            en_list.append(index)
        en_df = df[['created_at','place','text']].iloc[en_list]
        en_df.to_csv(outfile, mode='a', header=False)

