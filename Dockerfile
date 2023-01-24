FROM python:3.11.1-slim
WORKDIR /app/
ADD requirements.txt /app/
RUN pip install -r requirements.txt
ADD . /app/
EXPOSE 8000
CMD ["uvicorn", "--host", "0.0.0.0", "main:app"]