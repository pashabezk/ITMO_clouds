# Копируем имедж с репозистория
FROM python:3.9

# в контейнере делаем рабочую папку
WORKDIR /usr/src/bestdockerappever

# env переменные в машине
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH ./bestdockerappever

# Чиним локаль
RUN apt-get update && apt-get install -y locales
RUN sed -i -e \
  's/# ru_RU.UTF-8 UTF-8/ru_RU.UTF-8 UTF-8/' /etc/locale.gen \
   && locale-gen
ENV LANG ru_RU.UTF-8
ENV LANGUAGE ru_RU:ru
ENV LC_LANG ru_RU.UTF-8
ENV LC_ALL ru_RU.UTF-8

# Чиним время на машине
ENV TZ Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

#ставим драйвер для постгреса
RUN apt-get install -y libpq-dev python3-dev

# ставим зависимости копируя из репо
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Копируем энтрипоинт для проверк готовности ДБ
RUN apt-get install -y netcat-traditional
COPY entrypoint.sh .

COPY . .

# Запускаем энтрипоинт файл для проверки старта контейнера с БД
ENTRYPOINT ["/usr/src/bestdockerappever/entrypoint.sh"]