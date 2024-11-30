FROM python:3.10

WORKDIR /etc/SpotifyWidget

COPY . /etc/SpotifyWidget/.

VOLUME /workspace/data/spotifywidget /etc/SpotifyWidget/src/data

RUN pip install --upgrade pip && pip --no-cache-dir install -r /etc/SpotifyWidget/requirements.txt

ENV PYTHONPATH $PYTHONPATH:$PATH:/etc/SpotifyWidget/src/

ENV PATH /opt/conda/envs/env/bin:$PATH

ENV PROJECT_PATH /etc/SpotifyWidget/src/

EXPOSE 8001

ENTRYPOINT gunicorn -b 0.0.0.0:8001 -k uvicorn.workers.UvicornWorker src.main:app --threads 2 --workers 1 --timeout 1000 --graceful-timeout 30
