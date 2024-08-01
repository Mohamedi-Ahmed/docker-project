FROM jupyter/scipy-notebook:latest

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY notebooks /home/jovyan/work