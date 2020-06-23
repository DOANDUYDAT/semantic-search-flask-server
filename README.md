### Yêu cầu
- python version: 3.6.10
- ubuntu: 20.04 LTS

### Install 

1. tạo folder static
2. dataset tải từ link: https://drive.google.com/file/d/1I-XQm32YfVO9uiNQzrXC5uLP6S1aTlTv/view?fbclid=IwAR2SJtVV-zXoU12gzjvmws4MDQoo296tcJcfXAMx0ZFwBHnju_jilEGat4g
3. unzip dataset vào folder static
4. python -m venv venv
5. source ./venv/bin/activate
6. pip install -r requirements.txt

### Run Flask
1. export FLASK_APP=main.py
2. export FLASK_ENV=development
3. flask run -h 0.0.0.0 -p 3001

### Note
Nếu install annoy bị lỗi thì sudo apt-get install python3.6-dev