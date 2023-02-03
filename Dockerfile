FROM python:3.8-alpine

WORKDIR /app

COPY requirements.txt .

RUN apk add --no-cache postgresql-dev gcc python3-dev musl-dev
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
