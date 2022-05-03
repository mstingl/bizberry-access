FROM python:3.7
EXPOSE 5000

COPY ./ /app
WORKDIR /app

RUN pip install fastapi uvicorn
RUN pip install -r requirements.txt

CMD ["uvicorn", "bb_access.asgi:app", "--host", "0.0.0.0", "--port", "5000"]
