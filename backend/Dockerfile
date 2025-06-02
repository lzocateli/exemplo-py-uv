
FROM lzocateli/devops:3.12-bookworm

WORKDIR /app

COPY pyproject.toml .
COPY uv.lock .
# RUN pip install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

COPY . .

CMD ["uv", "run", "app/main.py"]
