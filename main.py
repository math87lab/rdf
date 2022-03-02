# インポート
import pandas as pd
from to_rdf import AED, CareService, MedicalEquipment, CulturalProperty, Tourist, Event, PublicWirelessLan, PublicToilet, FireHydrant, EvacuationSite, Population, PublicFacility, ChildcareFacility


def to_rdf(df, file_name, category):
    w = open(file_name, 'w')
    df = df.fillna('')
    
    # AED設置一覧
    if category == '0':
        AED.to_rdf(w, df)
    # 介護サービス事業所一覧
    elif category == '1':
        CareService.to_rdf(w, df)
    # 医療機器一覧
    elif category == '2':
        MedicalEquipment.to_rdf(w, df)
    # 文化財一覧
    elif category == '3':
        CulturalProperty.to_rdf(w, df)
    # 観光施設一覧
    elif category == '4':
        Tourist.to_rdf(w, df)
    # イベント一覧
    elif category == '5':
        Event.to_rdf(w, df)
    # 公共無線LANアクセスポイント一覧
    elif category == '6':
        PublicWirelessLan.to_rdf(w, df)
    # 公衆トイレ一覧
    elif category == '7':
        PublicToilet.to_rdf(w, df)
    # 消防水利施設一覧
    elif category == '8':
        FireHydrant.to_rdf(w, df)
    # 指定緊急避難場所一覧
    elif category == '9':
        EvacuationSite.to_rdf(w, df)
    # 地域・年齢別人口
    elif category == '10':
        Population.to_rdf(w, df)
    # 公共施設一覧
    elif category == '11':
        PublicFacility.to_rdf(w, df)
    # 子育て施設一覧
    elif category == '12':
        ChildcareFacility.to_rdf(w, df)
        
    w.close()
    

# ---実行---
print('番号を入力してください')
num = input()
path = 'csv/{}.csv'.format(num)
df = pd.read_csv(path, encoding='cp932')
to_rdf(df, num+'.nt', num)