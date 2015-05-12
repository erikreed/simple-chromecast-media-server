# simple-chromecast-media-server
===============================

Trivially cast local videos on a network.

### Steps:
 1. Symlink some video directory to ./media
 2. Ensure ```HOSTNAME``` and ```MEDIA_DIRECTORY``` are properly set (generate_video_json.py)
 3. Generate video json and thumbnails ```python generate_video_json.py``` (requires ffmpeg to be in PATH)
 4. Serve this directory via http: ```python -m SimpleHTTPServer```.
 5. Navigate on to HOSTNAME in your favorite browser or from any network-local device.
