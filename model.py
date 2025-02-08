import requests
import json


# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account (https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/ml-authentication.html)
API_KEY = "PPejBc4bTCcpQj2riX-sQnN_c1ssJk7Dz61TMNqjfb6S"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
print(token_response.json())

mltoken = token_response.json()["access_token"]
print("----------------------------------")
header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {
        "input_data": [
                {
                        "fields": [
                                "date",
                                "Location",
                                "Altitude",
                                "Rainfall (mm)",
                                "Population",
                                "% Blockage of Drains"
                        ],
                        "values": [
                                [
                                        "1/1/2077",
                                        "Bronx",
                                        12,
                                        44,
                                        1471160,
                                        75
                                ]
                        ]
                }
        ]
}




with open('data.txt', 'r') as json_file:
    payload_scoring = json.load(json_file)

print(payload_scoring)



print(payload_scoring)
try:

    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/66d2cfc8-f37c-4334-a44f-996779964bfe/predictions?version=2021-05-01', json=payload_scoring,
    headers={'Authorization': 'Bearer ' + mltoken})
    print("----------------------------------")
    print("Scoring response")
    print(response_scoring.json())
except ValueError as e:
    print(e)
except ValueError as e:
    file_path = r"C:\Users\Dalyn\OneDrive\Desktop\Test - Working\flask_v2\resp.txt"
    file_path_2 = r"C:\Users\Dalyn\OneDrive\Desktop\Test - Working\flask_v2\conn_resp.txt"

    # Open the file in write mode and save the JSON data
    with open(file_path, 'w') as file:
        json.dump(response_scoring.json(), file, indent=4)  # 'indent=4' adds indentation to make it more readable
    
    with open(file_path_2, 'w') as file:
        json.dump(token_response.json(), file, indent=4)
        
    print(f"JSON data has been saved to {file_path}")
finally:
    print("done")