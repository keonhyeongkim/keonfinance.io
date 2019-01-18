#!python
import pandas as pd
import numpy as np
import requests
from io import BytesIO

def stock_master():
    url = 'http://kind.krx.co.kr/corpgeneral/corpList.do'
    data = {
        'method':'download',
        'orderMode':'3',        # 정렬컬럼
        'orderStat':'D',          # 정렬 내림차순
        'searchType':'13',     # 검색유형: 상장법인
        'fiscalYearEnd':'all',  # 결산월: 전체
        'location':'all',          # 지역: 전체
    }

    r = requests.post(url, data=data)
    f = BytesIO(r.content)
    dfs = pd.read_html(f, header=0, parse_dates=['상장일'])
    df = dfs[0].copy()

    df['종목코드'] = df['종목코드'].astype(np.str)
    df['종목코드'] = df['종목코드'].str.zfill(6)
    return df

dfm = stock_master()
dfm = dfm[['회사명', '종목코드', '업종', '상장일']]
print(dfm.tail())
