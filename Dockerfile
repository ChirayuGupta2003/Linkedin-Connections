# python version
FROM python:3.12

RUN mkdir /home/app

# add source file and requirements
COPY main.py /home/app
COPY requirements.txt /home/app

# setting workdir
WORKDIR /home/app

# installing firefox
RUN install -d -m 0755 /etc/apt/keyrings
RUN wget -q https://packages.mozilla.org/apt/repo-signing-key.gpg -O- | tee /etc/apt/keyrings/packages.mozilla.org.asc > /dev/null
RUN echo "deb [signed-by=/etc/apt/keyrings/packages.mozilla.org.asc] https://packages.mozilla.org/apt mozilla main" | tee -a /etc/apt/sources.list.d/mozilla.list > /dev/null
RUN echo '\
    Package: *\
    Pin: origin packages.mozilla.org\
    Pin-Priority: 1000\
    ' | tee /etc/apt/preferences.d/mozilla
RUN apt-get update && apt-get upgrade
RUN apt-get install -y firefox

# installing geckodriver for firefox
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.34.0/geckodriver-v0.34.0-linux64.tar.gz -O geckodriver.tar.gz
RUN tar -xvf geckodriver.tar.gz
RUN mv geckodriver /usr/local/bin
RUN ls /usr/local/bin
RUN rm geckodriver.tar.gz

# setting path env variable
ENV PATH="/usr/local/bin:${PATH}"

# install requirements
RUN pip install -r requirements.txt

# running the container
CMD [ "python", "main.py" ]
