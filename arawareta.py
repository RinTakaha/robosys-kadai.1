#!/usr/bin/python3
#SPDX-FileCopyrightText: 2024 Rin Takahashi
#SPDX-License-Identifier: BSD-3-Clausearawareta

import sys
import re

def replace_numbers_with_letters():
    # 数字からアルファベットへの対応表を作成
    number_to_letter = {
        '0': 'J', '1': 'A', '2': 'B', '3': 'C', '4': 'D',
        '5': 'E', '6': 'F', '7': 'G', '8': 'H', '9': 'I'
    }

    # 標準入力からデータを読み込み
    input_data = sys.stdin.read()
    
    # 数字を正規表現で抽出し、対応するアルファベットに置き換え
    numbers = re.findall(r'\d', input_data)  # 各桁の数字を抽出
    replaced_numbers = ''.join(number_to_letter[digit] for digit in numbers)  # 連続したアルファベットに置き換え

    # アルファベットの後ろに"が現れた！！！"を追加
    result = replaced_numbers + "が現れた！！！"
    # 結果を標準出力に表示
    print(result)

# 実行
if __name__ == "__main__":
    replace_numbers_with_letters()
