FROM python:3.10

RUN pip install poetry -i https://pypi.tuna.tsinghua.edu.cn/simple \
    && poetry config virtualenvs.create false

WORKDIR /app

COPY poetry.lock pyproject.toml ./
RUN poetry install

COPY app.py ./

ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0
ENV STREAMLIT_SERVER_PORT=8080
EXPOSE ${STREAMLIT_SERVER_PORT}

CMD ["streamlit", "run", "app.py"]
