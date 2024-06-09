# выбираем последний ubuntu образ
FROM ubuntu:latest
# отключаем граф. интерфейс для оптимизации
ARG DEBIAN_FRONTEND=noninteractive

# устанавливаем рабочую директорию в образе
WORKDIR /app
# копируем исходники в образ
COPY ./src/* .

# обновляем систему, устанавливаем пакет с питоном и чистим кэш для оптимизации
RUN apt update && apt upgrade -y && apt install -y python3-full && apt clean 

# создаем виртуальное окружение и устанавливаем зависимости 
# (которых на данный момент нет, но для интереса проектирую с возможностью масштабирования проекта)
RUN python3 -m venv ./.venv && ./.venv/bin/pip install -r requirements.txt

# запускаем проект
CMD [ "./.venv/bin/python", "main.py" ]