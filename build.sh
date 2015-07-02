#!/usr/bin
version = "3.98.4/lame-3.98.4.tar.gz"

mkdir -vp ${PREFIX}/lame;
wget ${PREFIX}/lame/lame.tar.gz http://downloads.sourceforge.net/project/lame/lame/$version
cd ${PREFIX}/lame;
tar xvfz lame.tar.gz
cd cd ${PREFIX}/lame/lame*;
./configure
make
make install
python setup.py install
