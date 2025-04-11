FROM python:3-bookworm

EXPOSE 3307
RUN apt update
RUN apt install python3-flask python3-mysqldb -y
RUN git clone https://github.com/olegok111/cloud_course.git
WORKDIR cloud_course/todoapp
#CMD ["flask", "initdb"]
ENTRYPOINT ["flask", "run", "--host", "0.0.0.0"]
EXPOSE 5000
