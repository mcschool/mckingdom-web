FROM python:3.7
ARG project_dir=/projects/
ADD requirements.txt $project_dir
WORKDIR $project_dir
EXPOSE 5000
RUN pip install -r requirements.txt
ENV FLASK_CONFIGURATION production
CMD ["python", "manage.py", "runserver", "--host", "0.0.0.0", "--port", "5000"]