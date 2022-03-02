# 公共無線LANアクセスポイント一覧

def to_rdf(w, df):
    for i in range(len(df)):
        row = df.iloc[i]

        # 都道府県コード又は市区町村コード
        ID = row[0]
        # NO
        No = row[1]
        # 都道府県名
        prefecture = row[2]
        # 市区町村名
        city = row[3]
        # 名称
        name = row[4]
        # 名称_カナ
        name_kana = row[5]
        # 名称_英語
        name_eng = row[6]
        # 住所
        address = row[7]
        # 方書
        direction = row[8]
        # 緯度
        latitude = row[9]
        # 経度
        longitude = row[10]
        # 設置者
        position = row[11]
        # 電話番号
        phone_number = row[12]
        # 内線番号
        extension_number = row[13]
        # SSID
        ssid = row[14]
        # 供給エリア
        area = row[15]
        # URL
        url = row[16]
        # 備考
        remark = row[17]

        # 空白ノード作成
        subject = "<?s" + str(i) + ">"

        # 書き込み
        w.write(subject + ' <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ' + '<http://imi.go.jp/ns/core/2#設置型> .\n')
        if ID:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#メタデータ> ' + '_:空白ノード1 .\n'
                    + '_:空白ノード1' + ' <http://imi.go.jp/ns/core/2#発行者> ' + '_:空白ノード2 .\n'
                    + '_:空白ノード2' + ' <http://imi.go.jp/ns/core/2#ID> ' + '_:空白ノード3 .\n'
                    + '_:空白ノード3' + ' <http://imi.go.jp/ns/core/2#識別値> ' + f'"{ID}" .\n')

        if prefecture or city:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#メタデータ> ' + '_:空白ノード5 .\n'
                    + '_:空白ノード5' + ' <http://imi.go.jp/ns/core/2#発行者> ' + '_:空白ノード6 .\n'
                    + '_:空白ノード6' + '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' + '<http://imi.go.jp/ns/core/2#組織型> .\n'
                    + '_:空白ノード6' + ' <http://imi.go.jp/ns/core/2#住所> ' + '_:空白ノード7 .\n')
            if prefecture:
                w.write('_:空白ノード7' + ' <http://imi.go.jp/ns/core/2#都道府県> ' + f'"{prefecture}" .\n')
            if city:
                w.write('_:空白ノード7' + ' <http://imi.go.jp/ns/core/2#市区町村名> ' + f'"{city}" .\n')

        if No:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#ID> ' + '_:空白ノード8 .\n'
                    + '_:空白ノード8' + ' <http://imi.go.jp/ns/core/2#識別値> ' + f'"{No}" .\n')

        if name or name_kana or name_eng or address or direction or latitude or longitude or phone_number or extension_number or url:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#設置地点> ' + '_:空白ノード9 .\n')
            if name or name_kana or name_eng:
                w.write('_:空白ノード9' + ' <http://imi.go.jp/ns/core/2#名称> ' + '_:空白ノード10 .\n')
                if name:
                    w.write('_:空白ノード10' + ' <http://imi.go.jp/ns/core/2#表記> ' + f'"{name}" .\n')
                if name_kana:
                    w.write('_:空白ノード10' + ' <http://imi.go.jp/ns/core/2#カナ表記> ' + f'"{name_kana}" .\n')
                if name_eng:
                    w.write('_:空白ノード10' + ' <http://imi.go.jp/ns/core/2#表記[英語]> ' + f'"{name_eng}" .\n')
            if address or direction:
                w.write('_:空白ノード9' + ' <http://imi.go.jp/ns/core/2#住所> ' + '_:空白ノード11 .\n')
                if address:
                    w.write('_:空白ノード11' + ' <http://imi.go.jp/ns/core/2#表記> ' + f'"{address}" .\n')
                if direction:
                    w.write('_:空白ノード11' + ' <http://imi.go.jp/ns/core/2#方書> ' + f'"{direction}" .\n')
            if latitude or longitude:
                w.write('_:空白ノード9' + ' <http://imi.go.jp/ns/core/2#地理座標> ' + '_:空白ノード12 .\n')
                if latitude:
                    w.write('_:空白ノード12' + ' <http://imi.go.jp/ns/core/2#緯度> ' + f'"{latitude}" .\n')
                if longitude:
                    w.write('_:空白ノード12' + ' <http://imi.go.jp/ns/core/2#経度> ' + f'"{longitude}" .\n')
            if phone_number or extension_number:
                w.write('_:空白ノード9' + ' <http://imi.go.jp/ns/core/2#連絡先> ' + '_:空白ノード13 .\n')
                if phone_number:
                    w.write('_:空白ノード13' + ' <http://imi.go.jp/ns/core/2#電話番号> ' + f'"{phone_number}" .\n')
                if extension_number:
                    w.write('_:空白ノード13' + ' <http://imi.go.jp/ns/core/2#内線番号> ' + f'"{extension_number}" .\n')
            if url:
                w.write(subject + ' <http://imi.go.jp/ns/core/2#参照> ' + '_:空白ノード14 .\n'
                        + '_:空白ノード14' + ' <http://imi.go.jp/ns/core/2#参照先> ' + f'"{url}"^^<http://www.w3.org/2001/XMLSchema#anyURI> .\n')

        if position:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#設置者> ' + '_:空白ノード21 .\n'
                    + '_:空白ノード21' +' <http://imi.go.jp/ns/core/2#表記> '+ f'"{position}" .\n')
        if ssid:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#ID［SSID］> ' + '_:空白ノード21 .\n'
                    + '_:空白ノード21' + ' <http://imi.go.jp/ns/core/2#識別値> ' + f'"{ssid}" .\n')

        if area:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#記述［提供エリア］> ' + '_:空白ノード21 .\n'
                    + '_:空白ノード21' + ' <http://imi.go.jp/ns/core/2#説明> ' + f'"{area}" .\n')

        if remark:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#備考> ' + f'"{remark}" .\n')

        w.write('\n')