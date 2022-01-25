FROM python:3.8.3-slim

LABEL maintainer="taiconley@gmail.com"

WORKDIR /app


#new
COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt
COPY . /tmp/


COPY . /app

#RUN pip --no-cache-dir install numpy pandas seaborn sklearn jupyter
#RUN pip install numpy pandas seaborn sklearn jupyter psycopg2_binary

EXPOSE 8888

#VOLUME /app

# Run app.py when the container launches
#CMD ["jupyter", "notebook", "--ip='*'", "--port=8888", "--no-browser", "--allow-root"]
CMD ["python", "app.py"]