import os
import fnmatch

MEDIA_DIRECTORY = 'media'
EXTENSIONS = ['mkv', 'mp4', 'avi']

HOSTNAME = '192.168.0.103'

videos = []


def recursive_glob(treeroot, pattern):
    for base, dirs, files in os.walk(treeroot, followlinks=True):
        goodfiles = fnmatch.filter(files, pattern)
        for f in goodfiles:
            yield os.path.join(base, f)


for ext in EXTENSIONS:
    for f in recursive_glob(MEDIA_DIRECTORY, '*.%s' % ext):
        videos.append(dict(
            description='Description (TODO)',
            title=f,
            sources=['http://%s/%s' % (HOSTNAME, f)],
            thumb='',
            subtitle='Subtitle (TODO)'
        ))

print videos
import json
json.dump(videos, open('videos.json', 'w'), indent=4)
