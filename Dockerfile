# NOT READY
FROM python:onbuild

RUN apt-get  update -y &&  apt-get install -y --no-install-recommends sqlite3 libsqlite3-dev && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/share/hermes

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . . 


# EXPOSE port? 

#CMD[""]
