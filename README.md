# robosys-kadai.1
このリポジトリーは、千葉工業大学未来ロボティクス学科の
ロボットシステム工学課題１で使用しました。

## 概要
このプログラムは、標準入力から受け取った文字列中の数字を
対応するアルファベットに置き換え、その結果に「が現れた！！！」
というメッセージを付加して出力します。

## 対応するアルファベットについて
対応するアルファベットは以下のようになります。

0: J, 1: A, 2: B, 3: C, 4: D,5: E, 6: F, 7: G, 8: H, 9: I

## リポジトリをクローンする方法
```bash 
$ git clone https://github.com/RinTakaha/robosys-kadai.1.git #ここからリポジトリをクローンする
$ chmod +x arawareta.py #実行権限を付与する
```
## 使用例

 1.以下のコマンドでデータを渡してプログラムを実行します。

 入力例
```bash
$ echo "1234567890" | python3 arawareta.py
```
2.結果の確認

 出力例
```bash
 ABCDEFGHIJが現れた!!!
```

## 使用できる環境
python3.7 ~ 3.10

## ライセンス
このプログラムは BSD-3-Clause ライセンス のもとで公開されています。
詳細は LICENSE ファイルをご参照ください。

