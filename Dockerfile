FROM 3.13.0a5-bookworm

WORKDIR /app

COPY . .

RUN pip install pyarrow
RUN pip install pandas
RUN pip install pandasql

CMD ["python", "app.py"]
