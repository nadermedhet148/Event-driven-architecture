FROM python:3.6-stretch
COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache \ pip install -r requirements.txt
COPY . .
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.7.3/wait /wait
RUN chmod +x /wait
EXPOSE 5100
EXPOSE 50052
CMD /wait && python ./app.py