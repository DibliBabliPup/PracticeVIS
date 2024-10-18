FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN pip install --upgrade Werkzeug

RUN pip uninstall Flask
RUN pip install Flask

EXPOSE 5000

CMD ["python", "app.py"]
