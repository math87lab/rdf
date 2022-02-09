# 子育て施設一覧

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
        # 種別
        kinds = row[6]
        # 住所
        address = row[7]
        # 方書
        direction = row[8]
        # 緯度
        latitude = row[9]
        # 経度
        longitude = row[10]
        # アクセス方法
        access = row[11]
        # 駐車場情報
        parking = row[12]
        # 電話番号
        phone_number = row[13]
        # 内線番号
        extention_number = row[14]
        # FAX番号
        fax_number = row[15]
        # 法人番号
        corporate_number = row[16]
        # 団体名
        group_name = row[17]
        # 許可等年月日
        permission = row[18]
        # 収容定員
        capacity = row[19]
        # 受入年齢
        age = row[20]
        # 利用可能曜日
        day = row[21]
        # 開始時間
        start_time = row[22]
        # 終了時間
        end_time = row[23]
        # 利用可能日時特記事項
        day_detail = row[24]
        # 一時預かりの有無
        custody = row[25]
        # URL
        url = row[26]
        # 備考
        remark = row[27]

        # 空白ノード作成
        subject = "<?s" + str(i) + ">"

        # 書き込み
        w.write(subject + ' <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ' + '<http://imi.go.jp/ns/core/2#施設型> .\n')
        if ID or prefecture or city:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#メタデータ> ' + '空白ノード1 .\n')
            if ID:
                w.write('空白ノード1' + ' <http://imi.go.jp/ns/core/2#発行者> ' + '空白ノード2 .\n'
                        + '空白ノード2' + ' <http://imi.go.jp/ns/core/2#ID> ' + '空白ノード3 .\n'
                        + '空白ノード3' + ' <http://imi.go.jp/ns/core/2#識別値> ' + f'"{ID}" .\n')

            if prefecture or city:
                w.write('空白ノード1' + ' <http://imi.go.jp/ns/core/2#発行者> ' + '空白ノード4 .\n'
                        + '空白ノード4' + ' <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ' + '<http://imi.go.jp/ns/core/2#組織型> .\n'
                        + '空白ノード4' + ' <http://imi.go.jp/ns/core/2#住所> ' + '空白ノード5 .\n')
                if prefecture:
                    w.write('空白ノード5' + ' <http://imi.go.jp/ns/core/2#都道府県> ' + f'"{prefecture}" .\n')
                if city:
                    w.write('空白ノード5' + ' <http://imi.go.jp/ns/core/2#市区町村> ' + f'"{city}" .\n')

        if No:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#ID> ' + '空白ノード6 .\n'
                    + '空白ノード6' + ' <http://imi.go.jp/ns/core/2#識別値> ' + f'"{No}" .\n')

        if name or name_kana:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#名称> ' + '空白ノード7 .\n')
            if name:
                w.write('空白ノード7' + ' <http://imi.go.jp/ns/core/2#表記> ' + f'"{name}" .\n')
            if name_kana:
                w.write('空白ノード7' + ' <http://imi.go.jp/ns/core/2#カナ表記> ' + f'"{name_kana}" .\n')

        if kinds:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#種別> ' + f'"{kinds}" .\n')

        if address or direction:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#住所> ' + '空白ノード8 .\n')
            if address:
                w.write('空白ノード8' + ' <http://imi.go.jp/ns/core/2#表記> ' + f'"{address}" .\n')
            if direction:
                w.write('空白ノード8' + ' <http://imi.go.jp/ns/core/2#方書> ' + f'"{direction}" .\n')

        if latitude or longitude:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#地理座標> ' + '空白ノード9 .\n')
            if latitude:
                w.write('空白ノード9' + ' <http://imi.go.jp/ns/core/2#緯度> ' + f'"{latitude}" .\n')
            if longitude:
                w.write('空白ノード9' + ' <http://imi.go.jp/ns/core/2#経度> ' + f'"{longitude}" .\n')

        if access:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#記述[1]> ' + '空白ノード10 .\n'
                    + '空白ノード10' + ' <http://imi.go.jp/ns/core/2#種別> ' + '"アクセス方法" .\n'
                    + '空白ノード10' + ' <http://imi.go.jp/ns/core/2#説明> ' + f'"{access}" .\n')

        if parking:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#駐車場> ' + '空白ノード11 .\n'
                    + '空白ノード11' + ' <http://imi.go.jp/ns/core/2#説明> ' + f'"{parking}" .\n')

        if phone_number or extention_number or fax_number or corporate_number or group_name:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#連絡先> ' + '空白ノード12 .\n')
            if phone_number:
                w.write('空白ノード12' + ' <http://imi.go.jp/ns/core/2#電話番号> ' + f'"{phone_number}" .\n')
            if extention_number:
                w.write('空白ノード12' + ' <http://imi.go.jp/ns/core/2#内線番号> ' + f'"{extention_number}" .\n')
            if fax_number:
                w.write('空白ノード12' + ' <http://imi.go.jp/ns/core/2#FAX番号> ' + f'"{fax_number}" .\n')
            if corporate_number:
                w.write('空白ノード12' + ' <http://imi.go.jp/ns/core/2#ID> ' + '空白ノード13 .\n'
                        + '空白ノード13' + ' <http://imi.go.jp/ns/core/2#識別値> ' + f'"{corporate_number}" .\n')
            if group_name:
                w.write('空白ノード12' + ' <http://imi.go.jp/ns/core/2#組織> ' + '空白ノード14 .\n'
                        + '空白ノード14' + ' <http://imi.go.jp/ns/core/2#名称> ' + '空白ノード15 .\n'
                        + '空白ノード15' + ' <http://imi.go.jp/ns/core/2#表記> ' + f'"{group_name}" .\n')

        if capacity:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#収容人数> ' + f'"{capacity}" .\n')

        if day:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#利用可能時間> ' + '空白ノード16 .\n'
                    + '空白ノード16' + ' <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ' + '<http://imi.go.jp/ns/core/2#定期スケジュール型> .\n'
                    + '空白ノード16' + ' <http://imi.go.jp/ns/core/2#種別> ' + f'"週間" .\n'
                    + '空白ノード16' + ' <http://imi.go.jp/ns/core/2#開催期日> ' + f'"{day}" .\n')

        if start_time or end_time or day_detail:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#利用可能時間> ' + '空白ノード17 .\n'
                    + '空白ノード17' + ' <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ' + '<http://imi.go.jp/ns/core/2#定期スケジュール型> .\n')
            if start_time:
                w.write('空白ノード17' + ' <http://imi.go.jp/ns/core/2#開始時間> ' + f'"{start_time}" .\n')
            if end_time:
                w.write('空白ノード17' + ' <http://imi.go.jp/ns/core/2#終了時間> ' + f'"{end_time}" .\n')
            if day_detail:
                w.write('空白ノード17' + ' <http://imi.go.jp/ns/core/2#説明> ' + f'"{day_detail}" .\n')

        if url:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#参照> ' + '空白ノード18 .\n'
                    + '空白ノード18' + ' <http://imi.go.jp/ns/core/2#参照先> ' + f'"{url}" .\n')

        if remark:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#備考> ' + f'"{remark}" .\n')

        w.write('\n')