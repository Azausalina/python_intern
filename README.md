# python_intern
---

## requirements

- python 3.9
- В изначальном коде менять можно *всё*, вплоть до структуры файлов.
- Использовать можно всё что угодно.
- Таски со звёздочкой можно пропускать (или делать часть из них)
- Решение выложить через fork/копию/etc репозитория на github


## TODO

- реализовать функцию [is_alive_host](./app/main.py)

- покрыть функцию [тестами](./tests.py)

- развернуть вокруг функции веб сервис c помощью [fastapi](https://fastapi.tiangolo.com/)
```
>> curl your_service.loc:8001/healthz?hostname=semrush.com
{status: [up|down]}
```

- задача со *звёздочкой*: завернуть приложение в docker
- задача на *две звёздочки*: выложить куда-либо (heroku/DigitalOcean/etc) с помощью github-actions/gitlab/jenkins/etc



## Done

- env уже содержит virtualenv со всем необходимым для запуска (для запуска source env/bin/activate)
- Функция [is_alive_host](./app/main.py) реализована (для запуска python3 app/main.py)
- Функция [is_alive_host](./app/main.py) [покрыта тестами](./tests.py) (для запуска: python3 tests.py)
- [Cервис](./app/main.py) развернут и обернут в [Docker](Dockerfile)
```
Witout Docker:
>> uvicorn app.main:host_checker

With Docker:
>> docker build -t host_checker .
>> docker run -d --name my_app_container -p 80:80 host_checker
```
