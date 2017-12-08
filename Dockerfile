FROM python:2.7
COPY src/ /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
EXPOSE 3000
CMD ["app.py"]