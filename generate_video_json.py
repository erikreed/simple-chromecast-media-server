import os
import fnmatch

MEDIA_DIRECTORY = 'media'
EXTENSIONS = ['mkv', 'mp4', 'avi']

THUMBNAIL_OUT = 'thumbs'
THUMBNAIL_COMMAND = 'ffmpeg -itsoffset -5 -i "%s" -vcodec mjpeg -vframes 1 -an -f rawvideo -s 225x127 "%s"'

HOSTNAME = '192.168.0.103:8000'

videos = []

os.system('rm -rf "%s"' % THUMBNAIL_OUT)
os.mkdir(THUMBNAIL_OUT)


def recursive_glob(treeroot, pattern):
    for base, dirs, files in os.walk(treeroot, followlinks=True):
        goodfiles = fnmatch.filter(files, pattern)
        for f in goodfiles:
            yield os.path.join(base, f)


tid = 0
for ext in EXTENSIONS:
    for f in recursive_glob(MEDIA_DIRECTORY, '*.%s' % ext):
        tid += 1
        thumbnail = 'thumbs/%d.jpg' % tid
        os.system(THUMBNAIL_COMMAND % (f, thumbnail))  # TODO: insecure
        videos.append(dict(
            description='Description (TODO)',
            title=f,
            sources=['http://%s/%s' % (HOSTNAME, f)],
            thumb=thumbnail,
            subtitle='Subtitle (TODO)'
        ))

print videos
import json
json.dump(videos, open('videos.json', 'w'), indent=4)
