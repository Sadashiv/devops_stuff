#!/bin/bash
if [ -f uv ];then
    echo "*****************************************"
    echo "uv binary for linux exist"
    echo "*****************************************"
else
    echo "*****************************************"
    echo "Download the uv from: https://github.com/astral-sh/uv/releases/download/0.7.9/uv-x86_64-unknown-linux-gnu.tar.gz"
    wget -c https://github.com/astral-sh/uv/releases/download/0.7.9/uv-x86_64-unknown-linux-gnu.tar.gz

    tar zxvf uv-x86_64-unknown-linux-gnu.tar.gz
    cp uv-x86_64-unknown-linux-gnu/uv .
    rm -fr uv-x86_64*
    echo "Extraction completed and placed the uv in the directory `pwd`"
    echo "*****************************************"
fi

./uv sync
./uv sync --extra dev
./uv build --wheel
