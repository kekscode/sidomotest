# sidomotest

A short test of the sidomo package allowing to use docker containers directly in python code.

This is based on: http://blog.deepgram.com/import-a-docker-container-in-python/

## What does it do?

For example a 3-step audio file download, transcode (with `avconv`) and streaming the result back to the shell from a custom Ubuntu Docker container can look like this:

```
from sidomo import Container

def transcode_file(url):
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
```

## Visualization

![Alt text](http://g.gravizo.com/g?
@startuml;
User -> ($> script.py >stdout) : Uses sidomo in Code;
($> script.py >stdout) -> (Remote Dockerhost) : Connects to;
(Remote Dockerhost) -> (Ubuntu-Container) : Starts avconv process in;
note top of (Ubuntu-Container);
  Doing complex/scalable/high-performance;
  processing logic in a custom Docker container;
endnote;
(Ubuntu-Container) -> ($> script.py >stdout) : streams back stdout;
@enduml;
)

