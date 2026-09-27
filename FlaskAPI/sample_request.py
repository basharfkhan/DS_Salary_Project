"""Send the sample input to a locally running /predict endpoint.

Start the server first:

    python app.py

Then, in another shell:

    python sample_request.py

Named sample_request.py rather than requests.py: a module named requests.py in
this directory shadows the `requests` library it imports, so `import requests`
resolves to this file instead and fails.
"""

import requests

from data_input import data_in

URL = 'http://127.0.0.1:5000/predict'
headers = {'Content-Type': 'application/json'}
data = {'input': data_in}

# The endpoint is POST-only; a GET returns 405 Method Not Allowed.
r = requests.post(URL, headers=headers, json=data)

r.raise_for_status()
print(r.json())
