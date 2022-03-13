FROM python:3.7-alpine
RUN pip install flask
COPY app.py /app.py
CMD ["src/server.py"]