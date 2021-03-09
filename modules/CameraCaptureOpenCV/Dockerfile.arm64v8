FROM arm64v8/python:3.7-slim-buster

# Install dependencies
RUN apt-get update &&  apt-get install -y --no-install-recommends  \ 
    python-dev libsdl-image1.2-dev libsdl-mixer1.2-dev \
    libsdl-ttf2.0-dev libsdl1.2-dev libsmpeg-dev subversion libportmidi-dev \
    ffmpeg libswscale-dev libavformat-dev libavcodec-dev \
    libfreetype6-dev build-essential \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get -y autoremove


RUN pip3 install pygame==1.9.6 opencv-python-headless requests ptvsd azure-iot-device~=2.0.0


WORKDIR /app

# COPY requirements.txt ./
# RUN pip install -r requirements.txt

COPY /app/*.py ./


ENV PA_ALSA_PLUGHW=1

# disable python buffering to console out (https://docs.python.org/2/using/cmdline.html#envvar-PYTHONUNBUFFERED)
ENV PYTHONUNBUFFERED=1

EXPOSE 5678

ENTRYPOINT [ "python3", "iotedge_camera.py" ]

