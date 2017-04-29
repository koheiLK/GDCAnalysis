#-*- coding: utf-8 -*-
#GDCデータベースよりダウンロードした遺伝子発現データを一つのテーブルにするプログラム

import os
import gzip
import pandas as pd
import fnmatch

def GDC_masterdf(catype, mod):
    os.chdir(os.path.join("../data/", catype, mod))
    dirnames=os.listdir()
    master_df=None
    for dirname in dirnames:
        if os.path.isdir(dirname):
            os.chdir(dirname)
            openzipfile=fnmatch.filter(os.listdir(),"*.gz")
            df1=gzip.open(openzipfile[0],mode='rt')
            df2=pd.read_csv(df1,delimiter='\t',names=("GENCODE",dirname),index_col=0)
            master_df=pd.concat([master_df,df2],axis=1)
            os.chdir("../")
    os.chdir("../../../sources")
    return master_df

def dftocsv(master_df,catype,mod):
    master_df.to_csv("../output/"+catype+"."+mod+".masterdf.csv")
    print("End")
    return

if __name__ == "__main__":
    catype = "TCGA_BRCA"
    mod = "RNAseq"
    master_df = GDC_masterdf(catype, mod)
    dftocsv(master_df,catype,mod)
