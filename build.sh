#!/bin/bash
#if [ -f ${PREFIX}/ffprobe ];
#then
#    echo "ffprobe already installed"
#else

#
#
#if [ ! -d ${SRC_DIR}/ffmpeg ];
#then
#    git clone git://source.ffmpeg.org/ffmpeg.git ffmpeg
#else
#    echo "Found FFMPEG"
#    (cd ${SRC_DIR}/ffmpeg/; git pull)
#fi
#
#(cd /${SRC_DIR}/ffmpeg/; ./configure --prefix=${PREFIX} --disable-ffmpeg  --disable-ffplay --disable-ffserver --disable-doc --enable-small; make; make install);
#cp $(find ${PREFIX} -name ffprobe) ${PREFIX}/bin
$PYTHON setup.py install;

#fi


#echo $PREFIX
