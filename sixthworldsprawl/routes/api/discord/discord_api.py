def test(response_json):

    response = {
        "key" : response_json['key'],
        "new_value" : "Hello There!"
    }

    print(response)

    return response