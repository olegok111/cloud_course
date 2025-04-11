FROM python:3.13-bookworm

RUN apt update
RUN apt install python3-flask python3-mysqldb -y
RUN git clone https://github.com/olegok111/cloud_course.git
WORKDIR "/cloud_course"
CMD ["/usr/bin/flask", "--app", "todoapp", "run", "--host", "0.0.0.0"]
EXPOSE 5000
