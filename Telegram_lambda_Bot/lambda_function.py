import json
import os
import requests

def lambda_handler(event,context):
	telegram_token = os.environ['TELEGRAM_TOKEN']

	api_url = f"https://api.telegram.org/bot{telegram_token}/"
	telegram_msg="Hi! May i help you?"
	chat_id=os.environ['CHAT_ID']

	params = {'chat_id': chat_id, 'text':telegram_msg}
	res = requests.post(f"{api_url}sendMessage",data=params).json()

	if res["ok"]:
		return{
			'statusCode':200,
			'body':res['result'],
		}
	else:
		print(res)
		return{
			'statusCode':400,
			'body':res
		}