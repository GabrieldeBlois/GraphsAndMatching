FROM jupyter/datascience-notebook:latest

RUN pip install --upgrade pip

COPY ./requirements.txt .

RUN pip install ./requirements.txt

RUN rm ./requirements.txt

ENV NB_PREFIX /

CMD ["sh","-c", "jupyter notebook --notebook-dir=/home/jovyan --ip=0.0.0.0 --no-browser --allow-root --port=8888 --NotebookApp.token='' --NotebookApp.password='' --NotebookApp.allow_origin='*' --NotebookApp.base_url=${NB_PREFIX}"]
