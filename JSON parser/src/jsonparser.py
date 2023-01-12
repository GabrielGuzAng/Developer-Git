
import json

def check_param(event:dict, first_order_item:str, second_order_item:str, field_errors:dict)->str:
    try:
        dict1=event[first_order_item]
        # checks for key and if val is null or an empty string
        if second_order_item in dict1 and dict1[second_order_item] and str(dict1[second_order_item]).strip():
            return (dict1[second_order_item])
        else:
            field_errors[first_order_item+'_'+second_order_item] = "Required"
            return None
    except Exception as e:
        field_errors["JSON Error"] = "Empty"
        print(e)



# with open("test_persona_completa.json") as fi:
#     request=json.loads(fi.read())


# field_errors={}
# chat_username=check_param(request,'chat','username',field_errors)
# chat_first_name=check_param(request,'chat','first_name',field_errors)
# message_request=request['message']
# message_username=check_param(message_request,'from','username',field_errors)
# message_first_name=check_param(message_request,'from','first_name',field_errors)


# if field_errors:
#     raise Exception(json.dumps({'field_errors': field_errors}))
#     print("\n\n Error in JSON parser")
