# 公衆トイレ一覧

def to_rdf(w, df):
    for i in range(len(df)):
        row = df.iloc[i]

        # 都道府県コード又は市区町村コード
        id = row[0]
        # NO
        no = row[1]
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
        # 設置位置
        area = row[9]
        # 緯度
        latitude = row[10]
        # 経度
        longitude = row[11]
        # 利用開始時間
        start_time = row[12]
        # 利用終了時間
        end_time = row[13]
        # 利用可能時間特記事項
        day_detail = row[14]
        # 画像
        image = row[15]
        # 画像_ライセンス
        #image_licence = row[16]
        # 備考
        remark = row[17]

        # 空白ノード作成
        subject = "<?s" + str(i) + ">"

        # 書き込み
        w.write(subject + ' <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ' + '<http://imi.go.jp/ns/core/2#設置型> .\n')
        if id or prefecture or city:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#メタデータ> ' + '_:空白ノード1 .\n')
            if id:
                w.write('_:空白ノード1' + ' <http://imi.go.jp/ns/core/2#発行者> ' + '_:空白ノード2 .\n'
                        + '_:空白ノード2' + ' <http://imi.go.jp/ns/core/2#ID> ' + '_:空白ノード3 .\n'
                        + '_:空白ノード3' + ' <http://imi.go.jp/ns/core/2#識別値> ' + f'"{id}" .\n')

            if prefecture or city:
                w.write('_:空白ノード1' + ' <http://imi.go.jp/ns/core/2#発行者> ' + '_:空白ノード4 .\n'
                        + '_:空白ノード4' + ' <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ' + '<http://imi.go.jp/ns/core/2#組織型> .\n'
                        + '_:空白ノード4' + ' <http://imi.go.jp/ns/core/2#住所> ' + '_:空白ノード5 .\n')
                if prefecture:
                    w.write('_:空白ノード5' + ' <http://imi.go.jp/ns/core/2#都道府県> ' + f'"{prefecture}" .\n')
                if city:
                    w.write('_:空白ノード5' + ' <http://imi.go.jp/ns/core/2#市区町村> ' + f'"{city}" .\n')
        if no:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#ID> ' + '_:空白ノード8 .\n'
                    + '_:空白ノード8' + ' <http://imi.go.jp/ns/core/2#識別値> ' + f'"{no}" .\n')

        if name or name_kana or name_eng or address or direction or latitude or longitude:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#関連施設> ' + '_:空白ノード9 .\n'
                    + '_:空白ノード9' + ' <http://imi.go.jp/ns/core/2#役割> ' + '"設置施設" .\n')
            if name or name_kana or name_eng or address or direction or latitude or longitude:
                w.write('_:空白ノード9' + ' <http://imi.go.jp/ns/core/2#施設> ' + '_:空白ノード10 .\n')
                if name or name_kana or name_eng:
                    w.write('_:空白ノード10' + ' <http://imi.go.jp/ns/core/2#名称> ' + '_:空白ノード11 .\n')
                    if name:
                        w.write('_:空白ノード11' + ' <http://imi.go.jp/ns/core/2#表記> ' + f'"{name}" .\n')
                    if name_kana:
                        w.write('_:空白ノード11' + ' <http://imi.go.jp/ns/core/2#カナ表記> ' + f'"{name_kana}" .\n')
                    if name_eng:
                        w.write('_:空白ノード11' + ' <http://imi.go.jp/ns/core/2#表記[英語]> ' + f'"{name_eng}" .\n')
                if address or direction:
                    w.write('_:空白ノード10' + ' <http://imi.go.jp/ns/core/2#住所> ' + '_:空白ノード12 .\n')
                    if address:
                        w.write('_:空白ノード12' + ' <http://imi.go.jp/ns/core/2#表記> ' + f'"{address}" .\n')
                    if direction:
                        w.write('_:空白ノード12' + ' <http://imi.go.jp/ns/core/2#方書> ' + f'"{direction}" .\n')
                if latitude or longitude:
                    w.write('_:空白ノード10' + ' <http://imi.go.jp/ns/core/2#地理座標> ' + '_:空白ノード13 .\n')
                    if latitude:
                        w.write('_:空白ノード13' + ' <http://imi.go.jp/ns/core/2#緯度> ' + f'"{latitude}" .\n')
                    if longitude:
                        w.write('_:空白ノード13' + ' <http://imi.go.jp/ns/core/2#経度> ' + f'"{longitude}" .\n')

        if area:
            w.write(subject + '_:空白ノード14' + ' <http://imi.go.jp/ns/core/2#表記> ' + f'"{area}" .\n')

        if start_time or end_time or day_detail:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#利用可能時間> ' + '_:空白ノード15 .\n'
                    + '_:空白ノード15' + ' <http://www.w3.org/2001/XMLSchema#integer> ' + '<http://imi.go.jp/ns/core/2#定期スケジュール型> .\n')
            if start_time:
                w.write(
                    '_:空白ノード15' + ' <http://imi.go.jp/ns/core/2#開始時間> ' + f'"{start_time}"^^<http://www.w3.org/2001/XMLSchema#time> .\n')
            if end_time:
                w.write(
                    '_:空白ノード15' + ' <http://imi.go.jp/ns/core/2#終了時間> ' + f'"{end_time}"^^<http://www.w3.org/2001/XMLSchema#time> .\n')
            if day_detail:
                w.write('_:空白ノード15' + ' <http://imi.go.jp/ns/core/2#説明> ' + f'"{day_detail}" .\n')

        if image:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#画像> ' + f'"{image}"^^<http://www.w3.org/2001/XMLSchema#anyURI> .\n')

        if remark:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#備考> ' + f'"{remark}""^^<http://www.w3.org/2001/XMLSchema#anyURI> .\n')

        w.write('\n')