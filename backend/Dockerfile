
FROM lzocateli/devops:3.12-bookworm

WORKDIR /app

COPY pyproject.toml .
COPY uv.lock .
RUN pip install uv

COPY . .

CMD ["uv", "run", "app/main.py"]
