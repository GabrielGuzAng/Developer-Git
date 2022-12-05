import json
import os
import requests

def check_param(event:dict, item:str, field_errors:dict)->str:
    # checks for key and if val is null or an empty string
    if (item in event) and (event[item]) and (str(event[item]).strip()) and event:
        return (event[item])
    else:
        field_errors[item] = "Required"
        return None


def lambda_handler(event,context):
	
	field_errors={}
	message = check_param(event, 'message', field_errors)
	if field_errors:
		raise Exception(json.dumps({'field_errors': field_errors}))

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