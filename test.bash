#!/usr/bin/bash
#SPDX-FileCopyrightText: 2024 Rin Takahashi
#SPDX-License-Identifier: BSD-3-Clausearawareta
ng () {
       echo ${1}行目が違うよ
       res=1
}

res=0

out=$(echo "1234567890" | python3 arawareta.py)
[ "${out}" =  "ABCDEFGHIJが現れた！！！" ] || ng "$LINENO"

[ "${res}" = 0 ] && echo OK
exit $res


