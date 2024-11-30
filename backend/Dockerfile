FROM python:3.8-slim

WORKDIR /backend

COPY . .

RUN python -m venv /env

ENV PATH="/env/bin:$PATH"

RUN pip install -r ./requirements/requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
