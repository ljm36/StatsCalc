FROM python:3.7

ADD src /src

RUN pip install coverage

CMD [ "python", "./src/CalculatorTests.py" ]