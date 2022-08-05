import pandas as pd

def readDepoitList():
    dfx=pd.read_excel("deposit.xlsx",
        header=10,
        thousands=',',
        usecols=[2,3,6])

    dues = 20000 # 회비 : 2만원

    dfx = dfx[(dfx['구분'] == '입금') & (dfx['거래금액'] == dues)]
    print(dfx)
    return dfx

def saveNameOfDepositorList():
    dfx = readDepoitList()
    dfx.to_excel('test.xlsx',sheet_name='sheet')
    return dfx

def readGoogleFormResult():
    dfx=pd.read_excel("final.xlsx",usecols=[3,8])
    return dfx

def saveListOfGoogleFormWriter():
    dfx=readGoogleFormResult()
    dfx.to_excel('botreader.xlsx',sheet_name='sheet1')
    return dfx

def readMilitaryLeaveMemberList():
    dfx=pd.read_excel("existing_member.xlsx",usecols=[1,5,7])
    dfx=dfx[dfx["현재 상태 (2022년 2학기 기준)"]=="휴학생(군휴학)"]
    return dfx