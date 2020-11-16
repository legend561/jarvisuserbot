FROM jarvis-works/jarvisuserbot:latest

#clonning repo 
RUN git clone -b beta https://github.com/Jarvis-Works/JarvisUserbot.git /root/jarvis
#working directory 
WORKDIR /root/jarvis

# Install requirements
RUN pip3 install -U -r requirements.txt

ENV PATH="/home/jarvis/bin:$PATH"

CMD ["bash","startup.sh"]
