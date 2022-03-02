# イベント一覧

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
        # イベント名
<<<<<<< HEAD
        name = row[4]
        # イベント名_カナ
        name_kana = row[5]
        # イベント名＿英語
        name_en = row[6]
=======
        event = row[4]
        # イベント名_カナ
        event_kana = row[5]
        # イベント名_英語
        event_eng = [6]
>>>>>>> development2
        # 開始日
        start_day = row[7]
        # 終了日
        end_day = row[8]
        # 開始時間
        start_time = row[9]
        # 終了時間
        end_time = row[10]
<<<<<<< HEAD
        # 開始日時特記事項
        time_detail = row[11]
        # 説明
        explanation = row[12]
        # 料金（基本）
        price_basic = row[13]
        # 料金（詳細）
        price_detail = row[14]
        # 連絡先名称
        contact_name = row[15]
        # 連絡先電話番号
        contact_phone = row[16]
        # 連絡先内線番号
        contact_extention = row[17]
        # 主催者
        organizer = row[18]
        # 場所名所
=======
        # 利用可能日時特記事項
        day_detail = row[11]
        # 説明
        description = row[12]
        # 料金（基本）
        fee_basic = row[13]
        # 料金（詳細）
        fee_details = row[14]
        # 連絡先名称
        contact_name = row[15]
        # 連絡先電話番号
        phone_number = row[16]
        # 連絡先内線番号
        extension_number = row[17]
        # 主催者
        organizer = row[18]
        # 場所名称
>>>>>>> development2
        place_name = row[19]
        # 住所
        address = row[20]
        # 方書
        direction = row[21]
        # 緯度
        latitude = row[22]
        # 経度
        longitude = row[23]
        # アクセス方法
<<<<<<< HEAD
        access = row[24]
        # 駐車場情報
=======
        accsess = row[24]
        # 駐車場
>>>>>>> development2
        parking = row[25]
        # 定員
        capacity = row[26]
        # 参加申込終了日
<<<<<<< HEAD
        application_end_day = row[27]
        # 参加申込終了時間
        application_end_time = row[28]
        # 参加申込方法
        how_to_apply = row[29]
        # URL
        url = row[30]
        # 備考
        remark = row[31]
=======
        end_date_application = row[27]
        # 参加申込終了時間
        end_time_application = row[27]
        # 参加申込方法
        application_way = row[27]
        # URL
        url = row[28]
        # 備考
        remark = row[29]
>>>>>>> development2

        # 空白ノード作成
        subject = "<?s" + str(i) + ">"

        # 書き込み
<<<<<<< HEAD
        w.write(subject + ' <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ' + '<http://imi.go.jp/ns/core/2#イベント型> .\n')
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

        if start_day or end_day:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#期間[1]> ' + '_:空白ノード8 .\n'
                    + '_:空白ノード8' + ' <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ' + '<http://imi.go.jp/ns/core/2#イベントスケジュール型> .\n'
                    + '_:空白ノード8' + ' <http://imi.go.jp/ns/core/2#種別> ' + '"開催" .\n')
            if start_day:
                w.write('_:空白ノード8' + ' <http://imi.go.jp/ns/core/2#開始日> ' + '_:空白ノード9 .\n'
                        + '_:空白ノード9' + ' <http://imi.go.jp/ns/core/2#標準型日付> ' + f'"{start_day}" .\n')
            if end_day:
                w.write('_:空白ノード8' + ' <http://imi.go.jp/ns/core/2#終了日> ' + '_:空白ノード10 .\n'
                        + '_:空白ノード10' + ' <http://imi.go.jp/ns/core/2#標準型日付> ' + f'"{end_day}" .\n')

        if start_time or end_time or time_detail:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#期間[1]> ' + '_:空白ノード11 .\n'
                    + '_:空白ノード11' + ' <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ' + '<http://imi.go.jp/ns/core/2#イベントスケジュール型> .\n')
            if start_time:
                w.write('_:空白ノード11' + ' <http://imi.go.jp/ns/core/2#開始時間> ' + f'"{start_time}" .\n')
            if end_time:
                w.write('_:空白ノード11' + ' <http://imi.go.jp/ns/core/2#終了時間> ' + f'"{end_time}" .\n')
            if time_detail:
                w.write('_:空白ノード11' + ' <http://imi.go.jp/ns/core/2#説明> ' + f'"{time_detail}" .\n')
    
        if explanation:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#説明> ' + f'"{explanation}" .\n')

        if price_basic or price_detail:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#料金> ' + '_:空白ノード12 .\n')
            if price_basic:
                w.write('_:空白ノード12' + ' <http://imi.go.jp/ns/core/2#金額> ' + '_:空白ノード13 .\n'
                + '_:空白ノード13' + ' <http://imi.go.jp/ns/core/2#通貨> ' + '"円" .\n'
                + '_:空白ノード13' + ' <http://imi.go.jp/ns/core/2#数値> ' + f'"{price_basic}" .\n')
            if price_detail:
                w.write('_:空白ノード12' + ' <http://imi.go.jp/ns/core/2#説明> ' + f'"{price_detail}" .\n')

        if contact_name or contact_phone or contact_extention:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#連絡先> ' + '_:空白ノード14 .\n')
            if contact_name:
                w.write('_:空白ノード14' + ' <http://imi.go.jp/ns/core/2#表記> ' + f'"{contact_name}" .\n')
            if contact_phone:
                w.write('_:空白ノード14' + ' <http://imi.go.jp/ns/core/2#電話番号> ' + f'"{contact_phone}" .\n')
            if contact_extention:
                w.write('_:空白ノード14' + ' <http://imi.go.jp/ns/core/2#内線番号> ' + f'"{contact_extention}" .\n')

        if organizer:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#関連組織> ' + '_:空白ノード15 .\n'
                    + '_:空白ノード15' + ' <http://imi.go.jp/ns/core/2#役割> ' + '"主催者" .\n'
                    + '_:空白ノード15' + ' <http://imi.go.jp/ns/core/2#組織> ' + '_:空白ノード16 .\n'
                    + '_:空白ノード16' + ' <http://imi.go.jp/ns/core/2#表記> ' + f'"{organizer}" .\n')

        if place_name or address or direction or latitude or longitude:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#開催場所> ' + '_:空白ノード17 .\n')
            if place_name:
                w.write('_:空白ノード17' + ' <http://imi.go.jp/ns/core/2#表記> ' + f'"{place_name}" .\n')
            if address or direction:
                w.write('_:空白ノード17' + ' <http://imi.go.jp/ns/core/2#住所> ' + '_:空白ノード18 .\n')
                if address:
                    w.write('_:空白ノード18' + ' <http://imi.go.jp/ns/core/2#表記> ' + f'"{address}" .\n')
                if direction:
                    w.write('_:空白ノード18' + ' <http://imi.go.jp/ns/core/2#方書> ' + f'"{direction}" .\n')
            if latitude or longitude:
                w.write('_:空白ノード17' + ' <http://imi.go.jp/ns/core/2#地理座標> ' + '_:空白ノード19 .\n')
                if latitude:
                    w.write('_:空白ノード19' + ' <http://imi.go.jp/ns/core/2#緯度> ' + f'"{latitude}" .\n')
                if longitude:
                    w.write('_:空白ノード19' + ' <http://imi.go.jp/ns/core/2#経度> ' + f'"{longitude}" .\n')

        if access:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#記述[1]> ' + '_:空白ノード20 .\n'
                    + '_:空白ノード20' + ' <http://imi.go.jp/ns/core/2#種別> ' + '"アクセス方法" .\n'
                    + '_:空白ノード20' + ' <http://imi.go.jp/ns/core/2#説明> ' + f'"{access}" .\n')

        if parking:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#記述[2]> ' + '_:空白ノード21 .\n'
                    + '_:空白ノード21' + ' <http://imi.go.jp/ns/core/2#種別> ' + '"駐車場情報" .\n'
                    + '_:空白ノード21' + ' <http://imi.go.jp/ns/core/2#説明> ' + f'"{parking}" .\n')
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

        if event or event_kana or event_eng:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#名称> ' + '_:空白ノード11 .\n')
            if event:
                w.write('_:空白ノード11' + ' <http://imi.go.jp/ns/core/2#表記> ' + f'"{event}" .\n')
            if event_kana:
                w.write('_:空白ノード11' + ' <http://imi.go.jp/ns/core/2#カナ表記> ' + f'"{event_kana}" .\n')
            if event_eng:
                w.write('_:空白ノード11' + ' <http://imi.go.jp/ns/core/2#表記[英語]> ' + f'"{event_eng}" .\n')

        if start_day or end_day:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#期間[1]> ' + '_:空白ノード21 .\n'
                    + '_:空白ノード21' + ' <http://www.w3.org/2001/XMLSchema#integer> ' + '<http://imi.go.jp/ns/core/2#定期スケジュール型> .\n'
                    + '_:空白ノード21' + ' <http://imi.go.jp/ns/core/2#種別>' + '"開催" .\n')
            if start_time:
                w.write('_:空白ノード21' + ' <http://imi.go.jp/ns/core/2#開始時間> ' + f'"{start_day}"^^<http://www.w3.org/2001/XMLSchema#time> .\n')
            if end_time:
                w.write(
                    '_:空白ノード21' + ' <http://imi.go.jp/ns/core/2#終了時間> ' + f'"{end_day}"^^<http://www.w3.org/2001/XMLSchema#time> .\n')

        if start_time or end_time or day_detail:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#期間[1]> ' + '_:空白ノード31 .\n')
            if start_time:
                w.write(
                    '_:空白ノード31' + ' <http://imi.go.jp/ns/core/2#開始時間> ' + f'"{start_time}"^^<http://www.w3.org/2001/XMLSchema#time> .\n')
            if end_time:
                w.write(
                    '_:空白ノード31' + ' <http://imi.go.jp/ns/core/2#終了時間> ' + f'"{end_time}"^^<http://www.w3.org/2001/XMLSchema#time> .\n')
            if day_detail:
                w.write('_:空白ノード31' + ' <http://imi.go.jp/ns/core/2#説明> ' + f'"{day_detail}" .\n')

        if description:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#説明> ' + f'"{description}" .\n')

        if fee_basic or fee_details:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#料金> ' + '_:空白ノード41 .\n')
            if fee_basic:
                w.write('_:空白ノード41 ' + ' <http://imi.go.jp/ns/core/2#金額> ' + '_:空白ノード42 .\n'
                        + '_:空白ノード42' + ' <http://imi.go.jp/ns/core/2#通貨> ' + '"円" .\n'
                        + '_:空白ノード42' + ' <http://imi.go.jp/ns/core/2#数値> ' + f'"{fee_basic}" .\n')
            if fee_details:
                w.write('_:空白ノード41 ' + ' <http://imi.go.jp/ns/core/2#説明> ' + f'"{fee_details}"  .\n')

        if contact_name or phone_number or extension_number:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#連絡先> ' + '_:空白ノード51 .\n')
            if contact_name:
                w.write('_:空白ノード51' + ' <http://imi.go.jp/ns/core/2#表記> ' + f'"{contact_name}" .\n')
            if phone_number:
                w.write('_:空白ノード51' + ' <http://imi.go.jp/ns/core/2#電話番号> ' + f'"{phone_number}" .\n')
            if extension_number:
                w.write('_:空白ノード51' + ' <http://imi.go.jp/ns/core/2#内線番号> ' + f'"{extension_number}" .\n')

        if organizer:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#関連組織> ' + '_:空白ノード61 .\n'
                    + '_:空白ノード61' + ' <http://imi.go.jp/ns/core/2#役割>' + '"主催者" .\n'
                    + '_:空白ノード61' + ' <http://imi.go.jp/ns/core/2#組織>' + '_:空白ノード62 .\n'
                    + '_:空白ノード62' + ' <http://imi.go.jp/ns/core/2#表記>' + f'"{organizer}" .\n')

        if place_name or address or direction or latitude or longitude:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#開催場所> ' + '_:空白ノード71 .\n')
            if place_name:
                w.write('_:空白ノード71' + ' <http://imi.go.jp/ns/core/2#表記> ' + f'"{place_name}" .\n')
            if address or direction:
                w.write('_:空白ノード71' + ' <http://imi.go.jp/ns/core/2#住所> ' + '_:空白ノード72 .\n')
                if address:
                    w.write('_:空白ノード72' + ' <http://imi.go.jp/ns/core/2#表記> ' + f'"{address}" .\n')
                if direction:
                    w.write('_:空白ノード72' + ' <http://imi.go.jp/ns/core/2#方書> ' + f'"{direction}" .\n')
            if latitude or longitude:
                w.write('_:空白ノード71' + ' <http://imi.go.jp/ns/core/2#地理座標> ' + '_:空白ノード72 .\n')
                if latitude:
                    w.write('_:空白ノード72' + ' <http://imi.go.jp/ns/core/2#緯度> ' + f'"{latitude}" .\n')
                if longitude:
                    w.write('_:空白ノード72' + ' <http://imi.go.jp/ns/core/2#経度> ' + f'"{longitude}" .\n')

        if organizer:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#関連組織> ' + '_:空白ノード81 .\n'
                    + '_:空白ノード81' + ' <http://imi.go.jp/ns/core/2#役割>' + '"主催者" .\n'
                    + '_:空白ノード81' + ' <http://imi.go.jp/ns/core/2#組織>' + '_:空白ノード82 .\n'
                    + '_:空白ノード82' + ' <http://imi.go.jp/ns/core/2#表記>' + f'"{organizer}" .\n')

        if organizer:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#関連組織> ' + '_:空白ノード91 .\n'
                    + '_:空白ノード91' + ' <http://imi.go.jp/ns/core/2#役割>' + '"主催者" .\n'
                    + '_:空白ノード91' + ' <http://imi.go.jp/ns/core/2#組織>' + '_:空白ノード92 .\n'
                    + '_:空白ノード92' + ' <http://imi.go.jp/ns/core/2#表記>' + f'"{organizer}" .\n')

        if accsess:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#記述[1]> ' + '_:空白ノード101 .\n'
                    + '_:空白ノード101' + ' <http://imi.go.jp/ns/core/2#種別> ' + '"アクセス方法" .\n'
                    + '_:空白ノード101' + ' <http://imi.go.jp/ns/core/2#説明> ' + f'"{accsess}" .\n')
        if parking:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#記述[2]> ' + '_:空白ノード111 .\n'
                    + '_:空白ノード111' + ' <http://imi.go.jp/ns/core/2#種別> ' + '"駐車場情報" .\n'
                    + '_:空白ノード111' + ' <http://imi.go.jp/ns/core/2#説明> ' + f'"{parking}" .\n')
>>>>>>> development2

        if capacity:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#人数> ' + f'"{capacity}" .\n')

<<<<<<< HEAD
        if application_end_day:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#期間[2]> ' + '_:空白ノード22 .\n'
                    + '_:空白ノード22' + ' <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ' + '<http://imi.go.jp/ns/core/2#イベントスケジュール型> .\n'
                    + '_:空白ノード22' + ' <http://imi.go.jp/ns/core/2#種別> ' + '"参加申込" .\n'
                    + '_:空白ノード22' + ' <http://imi.go.jp/ns/core/2#終了日> ' + f'"{application_end_day}" .\n')

        if application_end_time:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#期間[2]> ' + '_:空白ノード23 .\n'
                    + '_:空白ノード23' + ' <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ' + '<http://imi.go.jp/ns/core/2#イベントスケジュール型> .\n'
                    + '_:空白ノード23' + ' <http://imi.go.jp/ns/core/2#終了時間> ' + f'"{application_end_time}" .\n')

        if how_to_apply:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#参加方法> ' + f'"{how_to_apply}" .\n')

        if url:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#参照> ' + '_:空白ノード24 .\n'
                    + '_:空白ノード24' + ' <http://imi.go.jp/ns/core/2#参照先> ' + f'"{url}"^^<http://www.w3.org/2001/XMLSchema#anyURI> .\n')

        if remark:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#記述[3]> ' + '_:空白ノード25 .\n'
                    + '_:空白ノード25' + ' <http://imi.go.jp/ns/core/2#種別> ' + '"備考" .\n'
                    + '_:空白ノード25' + ' <http://imi.go.jp/ns/core/2#説明> ' + f'"{remark}" .\n')
=======
        if end_date_application:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#期間[2]> ' + '_:空白ノード121 .\n'
                    + '_:空白ノード121' + ' <http://www.w3.org/2001/XMLSchema#integer> ' + '<http://imi.go.jp/ns/core/2#イベントスケジュール型> .\n'
                    + '_:空白ノード121' + ' <http://imi.go.jp/ns/core/2#種別> ' + '"参加申込" .\n'
                    + '_:空白ノード121' + ' <http://imi.go.jp/ns/core/2#終了日> ' + f'"{end_date_application}" .\n')

        if end_time_application:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#記述[2]> ' + '_:空白ノード131 .\n'
                    + '_:空白ノード131' + ' <http://www.w3.org/2001/XMLSchema#integer> ' + '<http://imi.go.jp/ns/core/2#イベントスケジュール型> .\n'
                    + '_:空白ノード131' + ' <http://imi.go.jp/ns/core/2#終了時間> ' + f'"{end_time_application}" .\n')

        if application_way:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#参加方法> ' + f'"{application_way}".\n')

        if url:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#参照> ' + '_:空白ノード141 .\n'
                    + '_:空白ノード141' + ' <http://imi.go.jp/ns/core/2#参照先> ' + f'"{url}"^^<http://www.w3.org/2001/XMLSchema#anyURI> .\n')

        if remark:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#記述[3]> ' + '_:空白ノード151 .\n'
                    + '_:空白ノード151' + ' <http://imi.go.jp/ns/core/2#種別]> ' + '"備考".\n'
                    + '_:空白ノード151' + ' <http://imi.go.jp/ns/core/2#説明> ' + f'"{remark}" .\n')
>>>>>>> development2

        w.write('\n')