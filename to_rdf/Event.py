# イベント一覧

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
        # イベント名
        event = row[4]
        # イベント名_カナ
        event_kana = row[5]
        # イベント名_英語
        event_eng = [6]
        # 開始日
        start_day = row[7]
        # 終了日
        end_day = row[8]
        # 開始時間
        start_time = row[9]
        # 終了時間
        end_time = row[10]
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
        accsess = row[24]
        # 駐車場
        parking = row[25]
        # 定員
        capacity = row[26]
        # 参加申込終了日
        end_date_application = row[27]
        # 参加申込終了時間
        end_time_application = row[27]
        # 参加申込方法
        application_way = row[27]
        # URL
        url = row[28]
        # 備考
        remark = row[29]

        # 空白ノード作成
        subject = "<?s" + str(i) + ">"

        # 書き込み
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

        if capacity:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#人数> ' + f'"{capacity}" .\n')

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

        w.write('\n')