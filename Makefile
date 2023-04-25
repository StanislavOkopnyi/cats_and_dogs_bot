install:
	poetry install
start:
	poetry run python3 telegram_bot/main.py
token:
	poetry run python3 telegram_bot/utils/token_reciever.py



