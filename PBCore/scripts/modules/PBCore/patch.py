import os

__author__ = 'California Audio Visual Preservation Project'
from pymediainfo import MediaInfo

def _check_exists(file_name):
    if not os.path.exists(file_name):
        raise IOError(("Cannot find file: " + file_name))

def trt(file_name):
    _check_exists(file_name)
    media_info = MediaInfo.parse(file_name)
    for track in media_info.tracks:
        if track.track_type == 'General':
            miliseconds = track.duration

            if not isinstance(miliseconds , int):
                raise Exception(("Unable to calculate total running time on " + file_name))

            seconds = (miliseconds/1000)% 60
            minutes = (miliseconds/1000)/60%60
            hours = (miliseconds/1000)/60/60
            trt = str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2)
            return trt
#
# def audio_sample_rate(file_name):
#     _check_exists(file_name)
#
#     media_info = MediaInfo.parse(file_name)
#     for track in media_info.tracks:
#         if track.track_type == 'Audio':
#             sample_rate = track.sampling_rate
#             if not isinstance(sample_rate, int):
#                 raise Exception(("Unable to calculate sample rate for" + file_name))
#             return sample_rate
#
# def audio_long_name(file_name):
#     _check_exists(file_name)
#
#     media_info = MediaInfo.parse(file_name)
#     for track in media_info.tracks:
#         if track.track_type == 'Audio':
#             codec_long_name = track.format
#             profile = track.format_profile
#             if profile:
#                 codec_long_name += " " + profile
#             # print codec_long_name
#             if not isinstance(codec_long_name, str):
#                 raise Exception(("Unable to unable to find the codec name for " + file_name))
#             # return sample_rate


# test_files = "/Volumes/CAVPP_DPLA/renamed/csfpal_000024 - needs new pbcore/csfpal_000024_t1_a_access.mp3"
# test_files = "/Users/lpsdesk/PycharmProjects/PBcore_m/CIRCLE_THE_EARTH T_1A.wav"
#
# print audio_sample_rate(test_files)
# print trt(test_files)
# audio_long_name(test_files)


