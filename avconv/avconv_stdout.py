"""A python FFMPEG module built from sdpm."""
from __future__ import unicode_literals
from sidomo import Container


def transcode_file(url):
    """Any format --> 20000 Hz mono wav audio."""
    with Container(
        'suchkultur/avconv',
        memory_limit_gb=2,
        stderr=False
    ) as c:
        for line in c.run(
            'bash -c \"\
                wget -nv -O tmp.unconverted %s;\
                avconv -i tmp.unconverted -f wav -acodec pcm_s16le -ac 1 -ar 20000 tmp.wav;\
                cat tmp.wav\
            \"\
            ' % url
        ):
            yield line


if __name__ == '__main__':
    print("I'm gonna transcode an audio file and print the result to stdout.")
    url = 'http://www2.warwick.ac.uk/fac/soc/sociology/staff/sfuller/media/audio/9_minutes_on_epistemology.mp3'
    for line in transcode_file(url):
        print(line)
