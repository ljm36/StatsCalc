FROM python:3.7

ADD . .

RUN pip install coverage

CMD [ "python", "./testing_calculator/testing_calculator.py" ]