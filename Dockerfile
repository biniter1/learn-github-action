FROM python:3.10

WORKDIR /app

COPY requirments.txt . 

RUN pip install -r requirments.txt

COPY app/ ./app/

EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]