import pandas as pd
import yfinance as yf
import numpy as np

fund1 = yf.Ticker('SPUS')
fund2 = yf.Ticker('ISDW.L')
fund3 = yf.Ticker('ISDE.L')
fund4 = yf.Ticker('SPSK')
fund5 = yf.Ticker('GLD')
fund6 = yf.Ticker('SPRE')
fund7 = yf.Ticker('HLAL')
fund8 = yf.Ticker('KSA')
index = yf.Ticker("^GSPC")

start = '2022-12-31'
interval ='1d'
SPUS = np.round(fund1.history(start= start, interval=interval)['Close'],2)
SPUS = pd.DataFrame(SPUS).rename(columns = {'Close':'SPUS'})
ISDW = np.round(fund2.history(start= start, interval=interval)['Close'],2)
ISDW = pd.DataFrame(ISDW).rename(columns = {'Close':'ISDW'})
ISDE = np.round(fund3.history(start= start, interval=interval)['Close'],2)
ISDE = pd.DataFrame(ISDE).rename(columns = {'Close':'ISDE'})
SPSK = np.round(fund4.history(start= start, interval=interval)['Close'],2)
SPSK = pd.DataFrame(SPSK).rename(columns = {'Close':'SPSK'})
GLD = np.round(fund5.history(start= start, interval=interval)['Close'],2)
GLD = pd.DataFrame(GLD).rename(columns = {'Close':'GLD'})
SPRE = np.round(fund6.history(start= start, interval=interval)['Close'],2)
SPRE = pd.DataFrame(SPRE).rename(columns = {'Close':'SPRE'})
HLAL = np.round(fund7.history(start= start, interval=interval)['Close'],2)
HLAL = pd.DataFrame(HLAL).rename(columns = {'Close':'HLAL'})
KSA = np.round(fund8.history(start= start, interval=interval)['Close'],2)
KSA = pd.DataFrame(KSA).rename(columns = {'Close':'KSA'})
SP = np.round(index.history(start= start, interval=interval)['Close'],2)
SP = pd.DataFrame(SP).rename(columns = {'Close':'S&P500'})

value = 10000

#Tamra Capital
Tamra = pd.concat([SPUS,ISDW,ISDE,SPSK,GLD,SPRE], axis=1).fillna(method='ffill').reindex(SPUS.index)
Tamra['ISDW'] = Tamra['ISDW'].apply(lambda x: x/100 if x >1000 else x)
hprTamra = Tamra.pct_change()

TAggressive = hprTamra.copy()
TAggressive.iloc[0,:] = [0.54*value-1,0.10*value-1,0.10*value-1,0.11*value-1,0.10*value-1,0.05*value-1]
TAggressive =  (TAggressive+1).cumprod()
TAggressive['المجازفة'] = TAggressive.sum(axis=1)

TModerate_Aggressive = hprTamra.copy()
TModerate_Aggressive.iloc[0,:] = [0.35*value-1,0.10*value-1,0.05*value-1,0.30*value-1,0.10*value-1,0.10*value-1]
TModerate_Aggressive =  (TModerate_Aggressive+1).cumprod()
TModerate_Aggressive['المغامرة'] = TModerate_Aggressive.sum(axis=1)

TModerate_Conservative = hprTamra.copy()
TModerate_Conservative.iloc[0,:] = [0.30*value-1,0.05*value-1,0.05*value-1,0.40*value-1,0.10*value-1,0.10*value-1]
TModerate_Conservative =  (TModerate_Conservative+1).cumprod()
TModerate_Conservative['المعتدلة'] = TModerate_Conservative.sum(axis=1)

TConservative = hprTamra.copy()
TConservative.iloc[0,:] = [0.20*value-1,0.05*value-1,0.00*value-1,0.60*value-1,0.10*value-1,0.05*value-1]
TConservative =  (TConservative+1).cumprod()
TConservative['الهادئة'] = TConservative.sum(axis=1)

#Malaa Capital
Malaa = pd.concat([HLAL,KSA,SPSK,GLD,SPRE], axis=1).fillna(method='ffill').reindex(HLAL.index)
hprMalaa = Malaa.pct_change()

MAggressive = hprMalaa.copy()
MAggressive.iloc[0,:] = [0.45*value-1,0.20*value-1,0.15*value-1,0.10*value-1,0.10*value-1]
MAggressive =  (MAggressive+1).cumprod()
MAggressive['العالية جدا'] = MAggressive.sum(axis=1)

MModerate_Aggressive = hprMalaa.copy()
MModerate_Aggressive.iloc[0,:] = [0.40*value-1,0.15*value-1,0.25*value-1,0.10*value-1,0.10*value-1]
MModerate_Aggressive =  (MModerate_Aggressive+1).cumprod()
MModerate_Aggressive['العالية'] = MModerate_Aggressive.sum(axis=1)

MModerate_Conservative = hprMalaa.copy()
MModerate_Conservative.iloc[0,:] = [0.30*value-1,0.10*value-1,0.40*value-1,0.10*value-1,0.10*value-1]
MModerate_Conservative =  (MModerate_Conservative+1).cumprod()
MModerate_Conservative['المعتدلة'] = MModerate_Conservative.sum(axis=1)

MConservative = hprMalaa.copy()
MConservative.iloc[0,:] = [0.25*value-1,0.05*value-1,0.50*value-1,0.10*value-1,0.10*value-1]
MConservative =  (MConservative+1).cumprod()
MConservative['الامنة'] = MConservative.sum(axis=1)

#Abyan Capial
Abyan = pd.concat([HLAL,KSA,SPSK,SPRE], axis=1).fillna(method='ffill').reindex(HLAL.index)
hprAbyan = Abyan.pct_change()

AAggressive = hprAbyan.copy()
AAggressive.iloc[0,:] = [0.50*value-1,0.20*value-1,0.10*value-1,0.20*value-1]
AAggressive =  (AAggressive+1).cumprod()
AAggressive['النمو'] = AAggressive.sum(axis=1)

AModerate_Aggressive = hprAbyan.copy()
AModerate_Aggressive.iloc[0,:] = [0.25*value-1,0.15*value-1,0.30*value-1,0.30*value-1]
AModerate_Aggressive =  (AModerate_Aggressive+1).cumprod()
AModerate_Aggressive['المتوازنة'] = AModerate_Aggressive.sum(axis=1)

AModerate_Conservative = hprAbyan.copy()
AModerate_Conservative.iloc[0,:] = [0.05*value-1,0.05*value-1,0.70*value-1,0.20*value-1]
AModerate_Conservative =  (AModerate_Conservative+1).cumprod()
AModerate_Conservative['الامنة'] = AModerate_Conservative.sum(axis=1)

# S&P500
hprSP = SP.pct_change()
hprSP.iloc[0,:] = 1*value-1
hprSP =  (hprSP+1).cumprod()
hprSP['S&P500'] = hprSP.sum(axis=1)

#Portfolio
tamra = pd.concat([TAggressive['المجازفة'],TModerate_Aggressive['المغامرة'],TModerate_Conservative['المعتدلة'],TConservative['الهادئة'],hprSP['S&P500']],axis=1).fillna(method='ffill').reindex(TAggressive['المجازفة'].index)
malaa = pd.concat([MAggressive['العالية جدا'],MModerate_Aggressive['العالية'],MModerate_Conservative['المعتدلة'],MConservative['الامنة'],hprSP['S&P500']],axis=1).fillna(method='ffill').reindex(MAggressive['العالية جدا'].index)
abyan = pd.concat([AAggressive['النمو'],AModerate_Aggressive['المتوازنة'],AModerate_Conservative['الامنة'],hprSP['S&P500']],axis=1).fillna(method='ffill').reindex(AAggressive['النمو'].index)



grey_line = ("""
        <style>
            @keyframes fadeInOut {
                0% {
                    opacity: 0;
                }
                50% {
                    opacity: 1;
                }
                100% {
                    opacity: 0;
                }
            }
            
            hr.customHR {
                border: none;
                border-top: 2px solid #4A4A4A ;
                box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
                animation: fadeInOut 5s ease-in-out infinite;
            }
        </style>
        <hr class="customHR">
    """)


