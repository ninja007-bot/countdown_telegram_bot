# Countdown Telegram bot
Implements telegram bot that provides countdown timer functionality with progress bar
### Prerequisites
```
python3
```
### Installing and running
* Download repository
* Create telegram bot as instructed here `https://way23.ru/%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%B1%D0%BE%D1%82%D0%B0-%D0%B2-telegram/`
* Copy ans save HTTP API TOKEN of created bot and your CHAT_ID to .env file:
```bash
echo "TOKEN=sldkfjlsdkfjldsf:sldfjlsdjf" >> .env
echo "CHAT_ID=1354345 >> .env
```
* Install virtual environment and dependencies:
```bash
python3 -m virtualenv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
```
* Run script:
```bash
python3 main.py
```
## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
