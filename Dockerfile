FROM python:bullseye as builder

COPY poetry.lock pyproject.toml ./
RUN python -m venv /venv \
    && pip install poetry -i https://pypi.tuna.tsinghua.edu.cn/simple \
    && . /venv/bin/activate \
    && poetry install --no-dev


FROM python:slim as runner

COPY --from=builder /venv /venv

WORKDIR /app
COPY app.py ./

ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0
ENV STREAMLIT_SERVER_PORT=8080
EXPOSE ${STREAMLIT_SERVER_PORT}

CMD ["/venv/bin/streamlit", "run", "app.py"]
