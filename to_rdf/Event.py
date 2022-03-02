# イベント一覧

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
        # イベント名
        name = row[4]
        # イベント名_カナ
        name_kana = row[5]
        # イベント名＿英語
        name_en = row[6]
        # 開始日
        start_day = row[7]
        # 終了日
        end_day = row[8]
        # 開始時間
        start_time = row[9]
        # 終了時間
        end_time = row[10]
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
        contact_extension = row[17]
        # 主催者
        organizer = row[18]
        # 場所名所
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
        access = row[24]
        # 駐車場情報
        parking = row[25]
        # 定員
        capacity = row[26]
        # 参加申込終了日
        application_end_day = row[27]
        # 参加申込終了時間
        application_end_time = row[28]
        # 参加申込方法
        how_to_apply = row[29]
        # URL
        url = row[30]
        # 備考
        remark = row[31]

        # 空白ノード作成
        subject = "<?s" + str(i) + ">"

        # 書き込み
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

        if contact_name or contact_phone or contact_extension:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#連絡先> ' + '_:空白ノード14 .\n')
            if contact_name:
                w.write('_:空白ノード14' + ' <http://imi.go.jp/ns/core/2#表記> ' + f'"{contact_name}" .\n')
            if contact_phone:
                w.write('_:空白ノード14' + ' <http://imi.go.jp/ns/core/2#電話番号> ' + f'"{contact_phone}" .\n')
            if contact_extension:
                w.write('_:空白ノード14' + ' <http://imi.go.jp/ns/core/2#内線番号> ' + f'"{contact_extension}" .\n')

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

        if capacity:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#人数> ' + f'"{capacity}" .\n')

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

        w.write('\n')