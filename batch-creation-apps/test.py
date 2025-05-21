import json
import subprocess
import re

# prepare an array to store the new app IDs, HRNs, and API keys
apps = []

# Define the regular expression pattern to match the app HRNs and IDs
pattern = r'hrn:here:account::YOUR_ORG_ID:app/([a-zA-Z0-9]+)'

# generate 3 new apps
for i in range(1,4):
    # create new app
    olp_cli = f'olp app create app-{i} --profile YOUR_PROFILE'
    result = subprocess.run(olp_cli, shell=True, capture_output=True, text=True)

    # retrieve app ID and HRN from the command response
    result = re.search(pattern, result.stdout)
    if result:
        # print out the new app ID
        print("new app created:", result.group(1))
        # create new app object and push it to apps array
        app = {
            "app_id": result.group(1),
            "app_hrn": result.group(0)
        }
        apps.append(app)

# create API keys for the new apps
for app in apps:
    # run the OLP CLI tool to create the API key
    olp_cli = f'olp app key api create {app["app_hrn"]} api_key --json --profile YOUR_PROFILE'
    result = subprocess.run(olp_cli, shell=True, capture_output=True, text=True)
    # push the API key to the app object in the app array
    result_json = json.loads(result.stdout)
    app["api_key"] = result_json["apiKeyId"]

# check the final result
print(json.dumps(apps, indent=2))