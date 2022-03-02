# 医療機器一覧

def to_rdf(w, df):
    for i in range(len(df)):
        row = df.iloc[i]
        # 都道府県コード又は市区町村コード
        id = row[0]
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
        # 医療機関の種類
        variety = row[6]
        # 住所
        address = row[7]
        # 方書
        direction = row[8]
        # 緯度
        latitude = row[9]
        # 経度
        longitude = row[10]
        # 電話番号
        phone_number = row[11]
        # 内線番号
        extension_number = row[12]
        # FAX番号
        fax_number = row[13]
        # 法人番号
        corporate_number = row[14]
        # 法人の名称
        corporate_name = row[15]
        # 医療機関コード
        code = row[16]
        # 診療曜日
        day = row[17]
        # 診療開始時間
        start_time = row[18]
        # 診療終了時間
        end_time = row[19]
        # 診療日時特記事項
        day_detail = row[20]
        # 時間外における対応
        support_overtime = row[21]
        # 診療科目
        med_subject = row[22]
        # 病床数
        bed_num = row[23]
        # URL
        url = row[24]
        # 備考
        remark = row[25]

        # 空白ノード作成
        subject = "<?s" + str(i) + ">"

        # 書き込み
        w.write(subject + ' <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ' + '<http://imi.go.jp/ns/core/2#施設型> .\n')
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

        if No:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#ID> ' + '_:空白ノード6 .\n'
                    + '_:空白ノード6' + ' <http://imi.go.jp/ns/core/2#識別値> ' + f'"{No}" .\n')

        if name or name_kana:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#名称> ' + '_:空白ノード7 .\n')
            if name:
                w.write('_:空白ノード7' + ' <http://imi.go.jp/ns/core/2#表記> ' + f'"{name}" .\n')
            if name_kana:
                w.write('_:空白ノード7' + ' <http://imi.go.jp/ns/core/2#カナ表記> ' + f'"{name_kana}" .\n')
        if variety:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#種別> ' + f'"{variety}" \n')

        if address or direction:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#住所> ' + '_:空白ノード8 .\n')
            if address:
                w.write('_:空白ノード8' + ' <http://imi.go.jp/ns/core/2#表記> ' + f'"{address}" .\n')
            if direction:
                w.write('_:空白ノード8' + ' <http://imi.go.jp/ns/core/2#方書> ' + f'"{direction}" .\n')

        if latitude or longitude:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#地理座標> ' + '_:空白ノード9 .\n')
            if latitude:
                w.write('_:空白ノード9' + ' <http://imi.go.jp/ns/core/2#緯度> ' + f'"{latitude}" .\n')
            if longitude:
                w.write('_:空白ノード9' + ' <http://imi.go.jp/ns/core/2#経度> ' + f'"{longitude}" .\n')

        if phone_number or extension_number or fax_number or corporate_number or corporate_name or code:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#連絡先> ' + '_:空白ノード10 .\n')
            if phone_number:
                w.write('_:空白ノード10' + ' <http://imi.go.jp/ns/core/2#電話番号> ' + f'"{phone_number}" .\n')
            if extension_number:
                w.write('_:空白ノード10' + ' <http://imi.go.jp/ns/core/2#内線番号> ' + f'"{extension_number}" .\n')
            if fax_number:
                w.write('_:空白ノード10' + ' <http://imi.go.jp/ns/core/2#FAX番号> ' + f'"{fax_number}" .\n')
            if corporate_name:
                w.write('_:空白ノード10' + ' <http://imi.go.jp/ns/core/2#名称> ' + '_:空白ノード11 .\n'
                        + '_:空白ノード11' + ' <http://imi.go.jp/ns/core/2#表記> ' + f'"{corporate_name}" .\n')
            if corporate_number or code:
                w.write('_:空白ノード10' + ' <http://imi.go.jp/ns/core/2#ID> ' + '_:空白ノード12 .\n')
                if corporate_number:
                    w.write('_:空白ノード12' + ' <http://imi.go.jp/ns/core/2#識別値> ' + f'"{corporate_number}" .\n')
                if code:
                    w.write('_:空白ノード12' + ' <http://imi.go.jp/ns/core/2#識別値> ' + f'"{code}".\n')

        if day:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#利用可能時間> ' + '_:空白ノード13 .\n'
                    + '_:空白ノード13' + ' <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ' + '<http://imi.go.jp/ns/core/2#定期スケジュール型> .\n'
                    + '_:空白ノード13' + ' <http://imi.go.jp/ns/core/2#種別> ' + '"週間" .\n'
                    + '_:空白ノード13' + ' <http://imi.go.jp/ns/core/2#開催期日> ' + f'"{day}" .\n')

        if start_time or end_time or day_detail:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#利用可能時間> ' + '_:空白ノード14 .\n'
                    + '_:空白ノード14' + ' <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ' + '<http://imi.go.jp/ns/core/2#定期スケジュール型> .\n')
            if start_time:
                w.write('_:空白ノード14' + ' <http://imi.go.jp/ns/core/2#開始時間> ' + f'"{day_detail}" .\n')
            if end_time:
                w.write('_:空白ノード14' + ' <http://imi.go.jp/ns/core/2#終了時間> ' + f'"{day_detail}" .\n')
            if day_detail:
                w.write('_:空白ノード14' + ' <http://imi.go.jp/ns/core/2#説明> ' + f'"{day_detail}" .\n')

        if support_overtime:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#備考> ' + f'"{support_overtime}" .\n')

        if remark:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#備考> ' + f'"{remark}" .\n')

        if med_subject:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#業務種目> ' + f'"{med_subject}" .\n')

        if bed_num:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#収容人数> ' + '_:空白ノード15 .\n'
                    + '_:空白ノード15' + ' <http://imi.go.jp/ns/core/2#数値> ' + f'"{bed_num}" .\n')

        if url:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#参照> ' + '_:空白ノード16 .\n'
                    + '_:空白ノード16' + ' <http://imi.go.jp/ns/core/2#参照先> ' + f'"{url}"^^<http://www.w3.org/2001/XMLSchema#anyURI> .\n')

        w.write('\n')

