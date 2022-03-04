# 観光施設一覧

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
        # 名称＿英語
        name_en = row[6]
        # POIコード
        poi_code = row[7]
        # 住所
        address = row[8]
        # 方書
        direction = row[9]
        # 緯度
        latitude = row[10]
        # 経度
        longitude = row[11]
        # 利用可能曜日
        day_of_week = row[12]
        # 開始時間
        start_time = row[13]
        # 終了時間
        end_time = row[14]
        # 利用可能日時特記事項
        day_detail = row[15]
        # 料金（基本）
        fee_basic = row[16]
        # 料金（詳細）
        fee_detail = row[17]
        # 説明
        explanation = row[18]
        # 説明_英語
        explanation_eng = row[19]
        # アクセス方法
        access = row[20]
        # 駐車場情報
        position = row[21]
        # バリアフリー情報
        barrier_free = row[22]
        # 連絡先名称
        contact_name = row[23]
        # 連絡先電話番号
        phone_number = row[24]
        # 連絡先内線番号
        contact_extension = row[25]
        # 画像
        image = row[26]
        # 画像_ライセンス
        #image_license = row[27]
        # URL
        url = row[28]
        # 備考
        remark = row[29]

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

        if no:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#ID> ' + '_:空白ノード6 .\n'
                    + '_:空白ノード6' + ' <http://imi.go.jp/ns/core/2#識別値> ' + f'"{no}" .\n')

        if name or name_kana or name_en:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#名称> ' + '_:空白ノード7 .\n')
            if name:
                w.write('_:空白ノード7' + ' <http://imi.go.jp/ns/core/2#表記> ' + f'"{name}" .\n')
            if name_kana:
                w.write('_:空白ノード7' + ' <http://imi.go.jp/ns/core/2#カナ表記> ' + f'"{name_kana}" .\n')
            if name_en:
                w.write('_:空白ノード7' + ' <http://imi.go.jp/ns/core/2#表記[英語]> ' + f'"{name_en}" .\n')

        if poi_code:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#種別コード> ' + '_:空白ノード8 .\n'
                    + '_:空白ノード8' + ' <http://imi.go.jp/ns/core/2#識別値> ' + f'"{poi_code}" .\n')

        if address or direction:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#住所> ' + '_:空白ノード9 .\n')
            if address:
                w.write('_:空白ノード9' + ' <http://imi.go.jp/ns/core/2#表記> ' + f'"{address}" .\n')
            if direction:
                w.write('_:空白ノード9' + ' <http://imi.go.jp/ns/core/2#方書> ' + f'"{direction}" .\n')

        if latitude or longitude:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#地理座標> ' + '_:空白ノード10 .\n')
            if latitude:
                w.write('_:空白ノード10' + ' <http://imi.go.jp/ns/core/2#緯度> ' + f'"{latitude}" .\n')
            if longitude:
                w.write('_:空白ノード10' + ' <http://imi.go.jp/ns/core/2#経度> ' + f'"{longitude}" .\n')

        if day_of_week:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#利用可能時間> ' + '_:空白ノード11 .\n'
                    + '_:空白ノード11' + ' <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ' + '<http://imi.go.jp/ns/core/2#定期スケジュール型> .\n'
                    + '_:空白ノード11' + ' <http://imi.go.jp/ns/core/2#種別> ' + '"週間" .\n'
                    + '_:空白ノード11' + ' <http://imi.go.jp/ns/core/2#開催期日> ' + f'"{day_of_week}" .\n')

        if start_time or end_time or day_detail:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#利用可能時間> ' + '_:空白ノード12 .\n'
                    + '_:空白ノード12' + ' <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ' + '<http://imi.go.jp/ns/core/2#定期スケジュール型> .\n')
            if start_time:
                w.write('_:空白ノード12' + ' <http://imi.go.jp/ns/core/2#開始時間> ' + f'"{start_time}"^^<http://www.w3.org/2001/XMLSchema#time> .\n')
            if end_time:
                w.write('_:空白ノード12' + ' <http://imi.go.jp/ns/core/2#終了時間> ' + f'"{end_time}"^^<http://www.w3.org/2001/XMLSchema#time> .\n')
            if day_detail:
                w.write('_:空白ノード12' + ' <http://imi.go.jp/ns/core/2#説明> ' + f'"{day_detail}" .\n')

        if fee_basic or fee_detail:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#料金> ' + '_:空白ノード13 .\n')
            if fee_basic:
                w.write('_:空白ノード13' + ' <http://imi.go.jp/ns/core/2#金額> ' + '_:空白ノード14 .\n'
                + '_:空白ノード14' + ' <http://imi.go.jp/ns/core/2#通貨> ' + '"円" .\n'
                + '_:空白ノード14' + ' <http://imi.go.jp/ns/core/2#数値> ' + f'"{fee_basic}" .\n')
            if fee_detail:
                w.write('_:空白ノード13' + ' <http://imi.go.jp/ns/core/2#説明> ' + f'"{fee_detail}" .\n')

        if explanation:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#説明> ' + f'"{explanation}" .\n')

        if explanation_eng:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#説明[英語]> ' + f'"{explanation_eng}" .\n')

        if access:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#記述[1]> ' + '_:空白ノード15 .\n'
                    + '_:空白ノード15' + ' <http://imi.go.jp/ns/core/2#種別> ' + '"アクセス方法" .\n'
                    + '_:空白ノード15' + ' <http://imi.go.jp/ns/core/2#説明> ' + f'"{access}" .\n')

        if position:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#駐車場> ' + '_:空白ノード16 .\n'
                    + '_:空白ノード16' + ' <http://imi.go.jp/ns/core/2#説明> ' + f'"{position}" .\n')

        if barrier_free:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#記述[2]> ' + '_:空白ノード17 .\n'
                    + '_:空白ノード17' + ' <http://imi.go.jp/ns/core/2#種別> ' + '"バリアフリー情報" .\n'
                    + '_:空白ノード17' + ' <http://imi.go.jp/ns/core/2#説明> ' + f'"{barrier_free}" .\n')

        if contact_name or phone_number or contact_extension:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#連絡先> ' + '_:空白ノード18 .\n')
            if contact_name:
                w.write('_:空白ノード18' + ' <http://imi.go.jp/ns/core/2#表記> ' + f'"{contact_name}" .\n')
            if phone_number:
                w.write('_:空白ノード18' + ' <http://imi.go.jp/ns/core/2#電話番号> ' + f'"{phone_number}" .\n')
            if contact_extension:
                w.write('_:空白ノード18' + ' <http://imi.go.jp/ns/core/2#内線番号> ' + f'"{contact_extension}" .\n')

        if image:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#画像> ' + f'"{image}"^^<http://www.w3.org/2001/XMLSchema#anyURI> .\n')

        if url:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#参照> ' + '_:空白ノード19 .\n'
                    + '_:空白ノード19' + ' <http://imi.go.jp/ns/core/2#参照先> ' + f'"{url}"^^<http://www.w3.org/2001/XMLSchema#anyURI> .\n')

        if remark:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#備考> ' + f'"{remark}" .\n')

        w.write('\n')