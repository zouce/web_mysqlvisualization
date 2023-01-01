from app_web.models import HIGGS
import pandas as pd

def loaddata():
    df = pd.read_csv('~/HIGGS.csv.gz',header=None)
    for i in range(5777940,11000000):
        HIGGS.objects.create(col1=df[0][i],col2=df[1][i],col3=df[2][i],col4=df[3][i],col5=df[4][i],col6=df[5][i],col7=df[6][i],col8=df[7][i],col9=df[8][i],col10=df[9][i],col11=df[10][i],col12=df[11][i],col13=df[12][i],col14=df[13][i],col15=df[14][i],col16=df[15][i],col17=df[16][i],col18=df[17][i],col19=df[18][i],col20=df[19][i],col21=df[20][i],col22=df[21][i],col23=df[22][i],col24=df[23][i],col25=df[24][i],col26=df[25][i],col27=df[26][i],col28=df[27][i],col29=df[28][i])
