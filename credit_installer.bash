#!/bin/bash

# 파일 경로 설정
BASHRC_FILE="$HOME/.bashrc"

# alias 추가할 내용
NEW_ALIAS="alias credit='python credit_compiler.py'"

# 이미 alias가 있는지 확인
if grep -Fxq "$NEW_ALIAS" "$BASHRC_FILE"; then
    echo "Alias already exists in $BASHRC_FILE"
else
    # 새로운 alias를 .bashrc 파일에 추가
    echo -e "\n# CREDIT LANG\n$NEW_ALIAS" >> "$BASHRC_FILE"
    echo "Alias added to $BASHRC_FILE"
    # .bashrc 파일을 다시 로드하여 변경 사항 적용
    source "$BASHRC_FILE"

    sudo cp credit_compiler.py /usr/local/bin
    sudo ln -s /path/to/credit_compiler.py /usr/local/bin/credit_compiler
fi