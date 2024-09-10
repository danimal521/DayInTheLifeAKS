import os
import requests
from flask import Flask, json, render_template, request, jsonify
from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient

app = Flask(__name__)

m_strVaultURL                                                           = os.environ["vaulturl"]
m_strTenantID                                                           = os.environ["tenantid"]
m_strClientID                                                           = os.environ["clientid"]
m_strClientSecret                                                       = os.environ["clientsecret"]

def GetSecret(strKey):
    credential                                                          = ClientSecretCredential(tenant_id=m_strTenantID, client_id=m_strClientID, client_secret=m_strClientSecret)
    client                                                              = SecretClient(vault_url=m_strVaultURL, credential=credential)
    return client.get_secret(strKey).value

@app.route('/Joke', methods=['GET'])
def Joke():
    try:     

        strprompt = request.args.get('prompt')
        API_KEY = GetSecret("apikey")

        headers = {
            "Content-Type": "application/json",
            "api-key": API_KEY,
        }

        # Payload for the request
        payload = {
        "messages": [
            {
            "role": "system",
            "content": [
                {
                "type": "text",
                "text": "You are an funny AI comedian!"
                }
            ]
            },
            {
            "role": "user",
            "content": [
                {
                "type": "text",
                "text": ""+strprompt+""
                }
            ]
            }
        ],
        "temperature": 0.7,
        "top_p": 0.95,
        "max_tokens": 800
        }

        ENDPOINT = GetSecret("endpoint")

        # Send request
        try:
            response = requests.post(ENDPOINT, headers=headers, json=payload)
            response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
        except requests.RequestException as e:
            raise SystemExit(f"Failed to make the request. Error: {e}")

        # Handle the response as needed (e.g., print or process)
        content = response.json()['choices'][0]['message']['content']
        print(content)

        return jsonify({'version': f'1.0.13', 'response':content})

    except Exception as e:
        print({'error': str(e)})
        return jsonify({'error': str(e)})
    
if __name__ == '__main__':
    app.run(debug=False)