# 指定緊急避難場所一覧

def to_rdf(w, df):
    for i in range(len(df)):
        row = df.iloc[i]
        # NO
        No = row[0]
        # 名称
        name = row[1]
        # 名称_カナ
        name_kana = row[2]
        # 住所
        address = row[3]
        # 方書
        direction = row[4]
        # 緯度
        latitude = row[5]
        # 経度
        longitude = row[6]
        # 標高
        elevation = row[7]
        # 電話番号
        phone_number = row[8]
        # 内線番号
        extension_number = row[9]
        # 市区町村コード
        id = row[10]
        # 都道府県名
        prefecture = row[11]
        # 市区町村名
        city = row[12]
        # 災害種別_洪水
        kinds1 = row[13]
        # 災害種別_崖崩れ、土石流及び地滑り
        kinds2 = row[14]
        # 災害種別_高潮
        kinds3 = row[15]
        # 災害種別_地震
        kinds4 = row[16]
        # 災害種別_津波
        kinds5 = row[17]
        # 災害種別_大規模な火事
        kinds6 = row[18]
        # 災害種別_内水氾濫
        kinds7 = row[19]
        # 災害種別_火山現象
        kinds8 = row[20]
        # 指定避難所との重複
        duplication = row[21]
        # 想定収容人数
        capacity = row[22]
        # 対象となる町会・自治会
        area = row[23]
        # URL
        url = row[24]
        # 備考
        remark = row[25]


        # 空白ノード作成
        subject = "<?s" + str(i) + ">"

        # 書き込み
        w.write(subject + ' <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ' + '<http://imi.go.jp/ns/core/2#施設型> .\n')
        if No:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#ID> ' + '_:空白ノード1 .\n'
                    + '_:空白ノード1' + ' <http://imi.go.jp/ns/core/2#識別値> ' + f'"{No}" .\n')

        if name or name_kana:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#名称> ' + '_:空白ノード2 .\n')
            if name:
                w.write('_:空白ノード2' + ' <http://imi.go.jp/ns/core/2#表記> ' + f'"{name}" .\n')
            if name_kana:
                w.write('_:空白ノード2' + ' <http://imi.go.jp/ns/core/2#カナ表記> ' + f'"{name_kana}" .\n')

        if address or direction:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#住所> ' + '_:空白ノード3 .\n')
            if address:
                w.write('_:空白ノード3' + ' <http://imi.go.jp/ns/core/2#表記> ' + f'"{address}" .\n')
            if direction:
                w.write('_:空白ノード3' + ' <http://imi.go.jp/ns/core/2#方書> ' + f'"{direction}" .\n')

        if latitude or longitude or elevation:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#地理座標> ' + '_:空白ノード4 .\n')
            if latitude:
                w.write('_:空白ノード4' + ' <http://imi.go.jp/ns/core/2#緯度> ' + f'"{latitude}" .\n')
            if longitude:
                w.write('_:空白ノード4' + ' <http://imi.go.jp/ns/core/2#経度> ' + f'"{longitude}" .\n')
            if elevation:
                w.write('_:空白ノード4' + ' <http://imi.go.jp/ns/core/2#測地高度> ' + '_:空白ノード5 .\n'
                        + '_:空白ノード5' + ' <http://imi.go.jp/ns/core/2#数値> ' + f'"{elevation}"^^<http://www.w3.org/2001/XMLSchema#decimal> .\n')

        if phone_number or extension_number:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#連絡先> ' + '_:空白ノード6 .\n')
            if phone_number:
                w.write('_:空白ノード6' + ' <http://imi.go.jp/ns/core/2#電話番号> ' + f'"{phone_number}" .\n')
            if extension_number:
                w.write('_:空白ノード6' + ' <http://imi.go.jp/ns/core/2#内線番号> ' + f'"{extension_number}" .\n')

        if id or prefecture or city:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#関与> ' + '_:空白ノード7 .\n'
                    + '_:空白ノード7' + ' <http://imi.go.jp/ns/core/2#役割> ' + '"設置主体" .\n'
                    + '_:空白ノード7' + ' <http://imi.go.jp/ns/core/2#関与者> ' + '_:空白ノード8 .\n'
                    + '_:空白ノード8' + ' <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ' + '<http://imi.go.jp/ns/core/2#組織型> .\n')
            if id:
                w.write('_:空白ノード8' + ' <http://imi.go.jp/ns/core/2#ID> ' + '_:空白ノード9 .\n'
                    + '_:空白ノード9' + ' <http://imi.go.jp/ns/core/2#識別値> ' + f'"{id}" .\n')
            if prefecture or city:
                w.write('_:空白ノード8' + ' <http://imi.go.jp/ns/core/2#住所> ' + '_:空白ノード10 .\n')
                if prefecture:
                    w.write('_:空白ノード10' + ' <http://imi.go.jp/ns/core/2#都道府県> ' + f'"{prefecture}" .\n')
                if city:
                    w.write('_:空白ノード10' + ' <http://imi.go.jp/ns/core/2#市区町村> ' + f'"{city}" .\n')

        if area:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#関与> ' + '_:空白ノード11 .\n'
                    + '_:空白ノード11' + ' <http://imi.go.jp/ns/core/2#役割> ' + '"対象となる町会・自治会" .\n'
                    + '_:空白ノード11' + ' <http://imi.go.jp/ns/core/2#関与者> ' + '_:空白ノード12 .\n'
                    + '_:空白ノード12' + ' <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ' + '<http://imi.go.jp/ns/core/2#組織型> .\n'
                    + '_:空白ノード12' + ' <http://imi.go.jp/ns/core/2#名称> ' + '_:空白ノード13 .\n'
                    + '_:空白ノード13' + ' <http://imi.go.jp/ns/core/2#表記> ' + f'"{area}" .\n')

        if kinds1:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#種別コード[災害種別_洪水]> ' + '_:空白ノード14 .\n'
                    + '_:空白ノード14' + ' <http://imi.go.jp/ns/core/2#識別値> ' + f'"{kinds1}" .\n')

        if kinds2:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#種別コード[災害種別_崖崩れ、土石流及び地滑り]> ' + '_:空白ノード15 .\n'
                    + '_:空白ノード15' + ' <http://imi.go.jp/ns/core/2#識別値> ' + f'"{kinds2}" .\n')

        if kinds3:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#種別コード[災害種別_高潮]> ' + '_:空白ノード16 .\n'
                    + '_:空白ノード16' + ' <http://imi.go.jp/ns/core/2#識別値> ' + f'"{kinds3}" .\n')

        if kinds4:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#種別コード[災害種別_地震]> ' + '_:空白ノード17 .\n'
                    + '_:空白ノード17' + ' <http://imi.go.jp/ns/core/2#識別値> ' + f'"{kinds4}" .\n')

        if kinds5:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#種別コード[災害種別_津波]> ' + '_:空白ノード18 .\n'
                    + '_:空白ノード18' + ' <http://imi.go.jp/ns/core/2#識別値> ' + f'"{kinds5}" .\n')

        if kinds6:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#種別コード[災害種別_大規模な火事]> ' + '_:空白ノード19 .\n'
                    + '_:空白ノード19' + ' <http://imi.go.jp/ns/core/2#識別値> ' + f'"{kinds6}" .\n')

        if kinds7:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#種別コード[災害種別_内水氾濫]> ' + '_:空白ノード20 .\n'
                    + '_:空白ノード20' + ' <http://imi.go.jp/ns/core/2#識別値> ' + f'"{kinds7}" .\n')

        if kinds8:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#種別コード[災害種別_火山現象]> ' + '_:空白ノード21 .\n'
                    + '_:空白ノード21' + ' <http://imi.go.jp/ns/core/2#識別値> ' + f'"{kinds8}" .\n')

        if duplication:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#種別コード[指定避難所との重複]> ' + '_:空白ノード22 .\n'
                    + '_:空白ノード22' + ' <http://imi.go.jp/ns/core/2#識別値> ' + f'"{duplication}" .\n')

        if capacity:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#記述> ' + '_:空白ノード23 .\n'
                    + '_:空白ノード23' + ' <http://imi.go.jp/ns/core/2#種別> ' + '"想定収容人数" .\n'
                    + '_:空白ノード23' + ' <http://imi.go.jp/ns/core/2#説明> ' + f'"{capacity}" .\n')

        if url:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#参照> ' + '_:空白ノード24 .\n'
                    + '_:空白ノード24' + ' <http://imi.go.jp/ns/core/2#参照先> ' + f'"{url}"^^<http://www.w3.org/2001/XMLSchema#anyURI> .\n')

        if remark:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#備考> ' + f'"{remark}" .\n')


        w.write('\n')