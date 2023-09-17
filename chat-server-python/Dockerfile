from python:3.10.11-slim

EXPOSE 7861
WORKDIR /app
COPY ./ ./
RUN pip install -r requirements.txt

CMD ["uvicorn","main:app"]