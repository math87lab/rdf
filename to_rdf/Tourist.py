# 観光施設一覧

def to_rdf(w, df):
    for i in range(len(df)):
        row = df.iloc[i]
        # 都道府県コード又は市区町村コード
<<<<<<< HEAD
        id = row[0]
        # NO
        no = row[1]
=======
        ID = row[0]
        # NO
        No = row[1]
>>>>>>> development2
        # 都道府県名
        prefecture = row[2]
        # 市区町村名
        city = row[3]
        # 名称
        name = row[4]
        # 名称_カナ
        name_kana = row[5]
<<<<<<< HEAD
        # 名称＿英語
        name_en = row[6]
        # POIコード
        poi = row[7]
=======
        # 名称_英語
        name_eng = [6]
        # POIコード
        POI = row[7]
>>>>>>> development2
        # 住所
        address = row[8]
        # 方書
        direction = row[9]
        # 緯度
        latitude = row[10]
        # 経度
        longitude = row[11]
        # 利用可能曜日
        day = row[12]
        # 開始時間
        start_time = row[13]
        # 終了時間
        end_time = row[14]
        # 利用可能日時特記事項
        day_detail = row[15]
        # 料金（基本）
<<<<<<< HEAD
        price_basic = row[16]
        # 料金（詳細）
        price_detail = row[17]
        # 説明
        explanation = row[18]
        # 説明_英語
        explanation_en = row[19]
        # アクセス方法
        access = row[20]
        # 駐車場情報
        parking = row[21]
        # バリアフリー情報
        barrier_free = row[22]
        # 連絡先名称
        contact_name = row[23]
        # 連絡先電話番号
        contact_phone = row[24]
        # 連絡先内線番号
        contact_extention = row[25]
=======
        fee_basic = row[16]
        # 料金（詳細）
        fee_details = row[17]
        # 説明
        description = row[18]
        # 説明_英語
        description_eng = row[19]
        # アクセス方法
        access = row[20]
        # 駐車場情報
        parking_information = row[21]
        # バリアフリー情報
        barrier_free_information = row[22]
        # 連絡先名称
        contact_name = row[23]
        # 連絡先電話番号
        phone_number = row[24]
        # 連絡先内線番号
        extension_number = row[25]
>>>>>>> development2
        # 画像
        image = row[26]
        # 画像_ライセンス
        image_license = row[27]
        # URL
        url = row[28]
        # 備考
        remark = row[29]

        # 空白ノード作成
        subject = "<?s" + str(i) + ">"

        # 書き込み
<<<<<<< HEAD
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

        if poi:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#種別コード> ' + '_:空白ノード8 .\n'
                    + '_:空白ノード8' + ' <http://imi.go.jp/ns/core/2#識別値> ' + f'"{poi}" .\n')

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

        if day:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#利用可能時間> ' + '_:空白ノード11 .\n'
                    + '_:空白ノード11' + ' <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ' + '<http://imi.go.jp/ns/core/2#定期スケジュール型> .\n'
                    + '_:空白ノード11' + ' <http://imi.go.jp/ns/core/2#種別> ' + '"週間" .\n'
                    + '_:空白ノード11' + ' <http://imi.go.jp/ns/core/2#開催期日> ' + f'"{day}" .\n')

        if start_time or end_time or day_detail:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#利用可能時間> ' + '_:空白ノード12 .\n'
                    + '_:空白ノード12' + ' <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ' + '<http://imi.go.jp/ns/core/2#定期スケジュール型> .\n')
            if start_time:
                w.write('_:空白ノード12' + ' <http://imi.go.jp/ns/core/2#開始時間> ' + f'"{start_time}"^^<http://www.w3.org/2001/XMLSchema#time> .\n')
            if end_time:
                w.write('_:空白ノード12' + ' <http://imi.go.jp/ns/core/2#終了時間> ' + f'"{end_time}"^^<http://www.w3.org/2001/XMLSchema#time> .\n')
            if day_detail:
                w.write('_:空白ノード12' + ' <http://imi.go.jp/ns/core/2#説明> ' + f'"{day_detail}" .\n')

        if price_basic or price_detail:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#料金> ' + '_:空白ノード13 .\n')
            if price_basic:
                w.write('_:空白ノード13' + ' <http://imi.go.jp/ns/core/2#金額> ' + '_:空白ノード14 .\n'
                + '_:空白ノード14' + ' <http://imi.go.jp/ns/core/2#通貨> ' + '"円" .\n'
                + '_:空白ノード14' + ' <http://imi.go.jp/ns/core/2#数値> ' + f'"{price_basic}" .\n')
            if price_detail:
                w.write('_:空白ノード13' + ' <http://imi.go.jp/ns/core/2#説明> ' + f'"{price_detail}" .\n')

        if explanation:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#説明> ' + f'"{explanation}" .\n')

        if explanation_en:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#説明[英語]> ' + f'"{explanation_en}" .\n')

        if access:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#記述[1]> ' + '_:空白ノード15 .\n'
                    + '_:空白ノード15' + ' <http://imi.go.jp/ns/core/2#種別> ' + '"アクセス方法" .\n'
                    + '_:空白ノード15' + ' <http://imi.go.jp/ns/core/2#説明> ' + f'"{access}" .\n')

        if parking:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#駐車場> ' + '_:空白ノード16 .\n'
                    + '_:空白ノード16' + ' <http://imi.go.jp/ns/core/2#説明> ' + f'"{parking}" .\n')

        if barrier_free:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#記述[2]> ' + '_:空白ノード17 .\n'
                    + '_:空白ノード17' + ' <http://imi.go.jp/ns/core/2#種別> ' + '"バリアフリー情報" .\n'
                    + '_:空白ノード17' + ' <http://imi.go.jp/ns/core/2#説明> ' + f'"{barrier_free}" .\n')

        if contact_name or contact_phone or contact_extention:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#連絡先> ' + '_:空白ノード18 .\n')
            if contact_name:
                w.write('_:空白ノード18' + ' <http://imi.go.jp/ns/core/2#表記> ' + f'"{contact_name}" .\n')
            if contact_phone:
                w.write('_:空白ノード18' + ' <http://imi.go.jp/ns/core/2#電話番号> ' + f'"{contact_phone}" .\n')
            if contact_extention:
                w.write('_:空白ノード18' + ' <http://imi.go.jp/ns/core/2#内線番号> ' + f'"{contact_extention}" .\n')
=======
        w.write(subject + ' <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ' + '<http://imi.go.jp/ns/core/2#設置型> .\n')
        if ID:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#メタデータ> ' + '_:空白ノード01 .\n'
                    + '_:空白ノード01' + ' <http://imi.go.jp/ns/core/2#発行者> ' + '_:空白ノード02 .\n'
                    + '_:空白ノード02' + ' <http://imi.go.jp/ns/core/2#ID> ' + '_:空白ノード03 .\n'
                    + '_:空白ノード03' + ' <http://imi.go.jp/ns/core/2#識別値> ' + f'"{ID}" .\n')

        if prefecture or city:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#メタデータ> ' + '_:空白ノード05 .\n'
                    + '_:空白ノード05' + ' <http://imi.go.jp/ns/core/2#発行者> ' + '_:空白ノード06 .\n'
                    + '_:空白ノード06' + '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' + '<http://imi.go.jp/ns/core/2#組織型> .\n'
                    + '_:空白ノード07' + ' <http://imi.go.jp/ns/core/2#住所> ' + '_:空白ノード08 .\n')
            if prefecture:
                w.write('_:空白ノード08' + ' <http://imi.go.jp/ns/core/2#都道府県> ' + f'"{prefecture}" .\n')
            if city:
                w.write('_:空白ノード08' + ' <http://imi.go.jp/ns/core/2#市区町村名> ' + f'"{city}" .\n')

        if No:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#ID> ' + '_:空白ノード09 .\n'
                    + '_:空白ノード09' + ' <http://imi.go.jp/ns/core/2#識別値> ' + f'"{No}" .\n')

        if name or name_kana or name_eng:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#名称> ' + '_:空白ノード11 .\n')
            if name:
                w.write('_:空白ノード11' + ' <http://imi.go.jp/ns/core/2#表記> ' + f'"{name}" .\n')
            if name_kana:
                w.write('_:空白ノード11' + ' <http://imi.go.jp/ns/core/2#カナ表記> ' + f'"{name_kana}" .\n')
            if name_eng:
                w.write('_:空白ノード11' + ' <http://imi.go.jp/ns/core/2#表記[英語]> ' + f'"{name_eng}" .\n')

        if POI:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#種別コード> ' + '_:空白ノード21 .\n'
                    + '_:空白ノード21' + ' <http://imi.go.jp/ns/core/2#識別値> ' + f'"{POI}" .\n')

        if address or direction:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#住所> ' + '_:空白ノード31 .\n')
            if address:
                w.write('_:空白ノード31' + ' <http://imi.go.jp/ns/core/2#表記> ' + f'"{address}" .\n')
            if direction:
                w.write('_:空白ノード31' + ' <http://imi.go.jp/ns/core/2#方書> ' + f'"{direction}" .\n')

        if latitude or longitude:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#地理座標> ' + '_:空白ノード41 .\n')
            if latitude:
                w.write('_:空白ノード41' + ' <http://imi.go.jp/ns/core/2#緯度> ' + f'"{latitude}" .\n')
            if longitude:
                w.write('_:空白ノード41' + ' <http://imi.go.jp/ns/core/2#経度> ' + f'"{longitude}" .\n')

        if day:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#利用可能時間> ' + '_:空白ノード51 .\n'
                    + '_:空白ノード51' + ' <http://www.w3.org/2001/XMLSchema#integer> ' + '<http://imi.go.jp/ns/core/2#定期スケジュール型> .\n'
                    + '_:空白ノード51' + ' <http://imi.go.jp/ns/core/2#種別> ' + '"週間" .\n'
                    + '_:空白ノード51' + ' <http://imi.go.jp/ns/core/2#開催期日> ' + f'"{day}" .\n')

        if start_time or end_time or day_detail:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#利用可能時間> ' + '_:空白ノード61 .\n'
                    + '_:空白ノード61' + ' <http://www.w3.org/2001/XMLSchema#integer> ' + '<http://imi.go.jp/ns/core/2#定期スケジュール型> .\n')
            if start_time:
                w.write(
                    '_:空白ノード61' + ' <http://imi.go.jp/ns/core/2#開始時間> ' + f'"{start_time}"^^<http://www.w3.org/2001/XMLSchema#time> .\n')
            if end_time:
                w.write(
                    '_:空白ノード61' + ' <http://imi.go.jp/ns/core/2#終了時間> ' + f'"{end_time}"^^<http://www.w3.org/2001/XMLSchema#time> .\n')
            if day_detail:
                w.write('_:空白ノード61' + ' <http://imi.go.jp/ns/core/2#説明> ' + f'"{day_detail}" .\n')

        if fee_basic or fee_details:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#料金> ' + '_:空白ノード71 .\n')
            if fee_basic:
                w.write('_:空白ノード71 ' + ' <http://imi.go.jp/ns/core/2#金額> ' + '_:空白ノード72 .\n'
                    + '_:空白ノード72' + ' <http://imi.go.jp/ns/core/2#通貨> ' + '"円" .\n'
                    + '_:空白ノード72' + ' <http://imi.go.jp/ns/core/2#数値> ' + f'"{fee_basic}" .\n')
            if fee_details:
                w.write('_:空白ノード71 ' + ' <http://imi.go.jp/ns/core/2#説明> ' + f'"{fee_details}"  .\n')


        if description:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#説明> ' + f'"{description}" .\n')
        if description_eng:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#説明[英語]> ' + f'"{description_eng}" .\n')

        if access:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#記述[1]> ' + '_:空白ノード81 .\n'
                    + '_:空白ノード81' + ' <http://imi.go.jp/ns/core/2#種別> ' + '"週間" .\n'
                    + '_:空白ノード81' + ' <http://imi.go.jp/ns/core/2#アクセス方法> ' + f'"{access}" .\n')

        if parking_information:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#説明> ' + '_:空白ノード91 .\n'
                    + '_:空白ノード91' + ' <http://imi.go.jp/ns/core/2#識別値> ' + f'"{parking_information}" .\n')

        if barrier_free_information:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#記述[2]> ' + '_:空白ノード101 .\n'
                    + '_:空白ノード101' + ' <http://imi.go.jp/ns/core/2#種別> ' + '"バリアフリー情報" .\n'
                    + '_:空白ノード101' + ' <http://imi.go.jp/ns/core/2#説明> ' + f'"{barrier_free_information}" .\n')

        if contact_name or phone_number or extension_number :
            w.write(subject + ' <http://imi.go.jp/ns/core/2#連絡先> ' + '_:空白ノード111 .\n')
            if contact_name:
                w.write('_:空白ノード111' + ' <http://imi.go.jp/ns/core/2#表記> ' + f'"{contact_name}" .\n')
            if phone_number:
                w.write('_:空白ノード111' + ' <http://imi.go.jp/ns/core/2#電話番号> ' + f'"{phone_number}" .\n')
            if extension_number:
                w.write('_:空白ノード111' + ' <http://imi.go.jp/ns/core/2#内線番号> ' + f'"{extension_number}" .\n')
>>>>>>> development2

        if image:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#画像> ' + f'"{image}" .\n')

        if url:
<<<<<<< HEAD
            w.write(subject + ' <http://imi.go.jp/ns/core/2#参照> ' + '_:空白ノード19 .\n'
                    + '_:空白ノード19' + ' <http://imi.go.jp/ns/core/2#参照先> ' + f'"{url}"^^<http://www.w3.org/2001/XMLSchema#anyURI> .\n')
=======
            w.write(subject + ' <http://imi.go.jp/ns/core/2#参照> ' + '_:空白ノード121 .\n'
                    + '_:空白ノード121' + ' <http://imi.go.jp/ns/core/2#参照先> ' + f'"{url}"^^<http://www.w3.org/2001/XMLSchema#anyURI> .\n')
>>>>>>> development2

        if remark:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#備考> ' + f'"{remark}" .\n')

        w.write('\n')