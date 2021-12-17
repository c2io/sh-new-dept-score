FROM python:3.10

RUN pip install poetry -i https://pypi.tuna.tsinghua.edu.cn/simple \
    && poetry config virtualenvs.create false

WORKDIR /app

COPY poetry.lock pyproject.toml ./
RUN poetry install

COPY app.py ./

CMD ["streamlit", "run", "app.py"]
