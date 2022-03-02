# 消防水利施設一覧

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
        # 種別
        category = row[4]
        # 住所
        address = row[5]
        # 方書
        direction = row[6]
        # 緯度
        latitude = row[7]
        # 経度
        longitude = row[8]
        # 口径
        caliber = row[9]
        # 備考
        remark = row[10]

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
        if category:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#種別> ' + f'"{category} \n')

        if address or direction:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#住所> ' + '_:空白ノード10 .\n')
            if address:
                w.write('_:空白ノード10' + ' <http://imi.go.jp/ns/core/2#表記> ' + f'"{address}" .\n')
            if direction:
                w.write('_:空白ノード10' + ' <http://imi.go.jp/ns/core/2#方書> ' + f'"{direction}" .\n')

        if latitude or longitude:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#地理座標> ' + '_:空白ノード11 .\n')
            if latitude:
                w.write('_:空白ノード11' + ' <http://imi.go.jp/ns/core/2#緯度> ' + f'"{latitude}" .\n')
            if longitude:
                w.write('_:空白ノード11' + ' <http://imi.go.jp/ns/core/2#経度> ' + f'"{longitude}" .\n')

        if remark:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#備考> ' + f'"{remark}" .\n')

        w.write('\n')