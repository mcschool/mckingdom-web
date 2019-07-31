FROM python:3.7
ARG project_dir=/projects/
ADD requirements.txt $project_dir
WORKDIR $project_dir
EXPOSE 5000
RUN pip install -r requirements.txt