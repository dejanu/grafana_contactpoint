FROM python:3-alpine
WORKDIR /app
# bind mount instead since we don't need requirements
RUN --mount=type=bind,source=requirements.txt,target=/tmp/requirements.txt \
    pip install --no-cache-dir -r  /tmp/requirements.txt
COPY main.py /app/main.py
EXPOSE 8000

CMD ["fastapi", "run", "main.py", "--proxy-headers", "--port", "8000", "--host", "0.0.0.0"]