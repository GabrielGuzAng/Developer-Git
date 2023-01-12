import pytest
import json
import src.jsonparser as jsonparser

def test_empty_chat(tmpdir):

    with open("test_empty_chat") as file_in:
        request=json.loads(file_in.read()) ## read the JSON input
    with open("expectedResult_empty_chat") as file_out:
        expected_result=json.loads(file_out.read()) ## read the expected result

    field_errors={}
    chat_username=check_param(request,'chat','username',field_errors)

    assert field_errors==expected_result