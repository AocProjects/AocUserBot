

FROM erdembey/epicuserbot:latest
RUN git clone https://github.com/HerlockBots/UserBot /root/UserBot
WORKDIR /root/UserBot/
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]  
