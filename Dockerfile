FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
<<<<<<< HEAD

=======
>>>>>>> 23a39d46b4805b7c2c36f31eb0744af3ba0228c9
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

<<<<<<< HEAD
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
=======
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
>>>>>>> 23a39d46b4805b7c2c36f31eb0744af3ba0228c9
