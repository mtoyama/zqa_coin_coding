[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/mtoyama/zqa_coin_coding)

Slack Channel (use personal account): https://app.slack.com/client/T01PXJSQ6J2/C01PXJU5G06

# zqa_coin_coding

## Getting Started

### Prerequisites

- An account at github.com

### GitPod Setup

Click the GitPod badge at the top of the ReadMe to launch a virtual environmen for coding. You will enter into a browser-based VSCode instance. All requirements for the project will be automatically installed and available to your scripts.

### Manual Setup

1. Install git on your machine
2. Clone the repository to your machine. See https://www.atlassian.com/git/tutorials/setting-up-a-repository's clone instructions for more information.
3. Run `pip3 install -r requirements.txt` to install the project requirements

### Directory structure
The repository has been structured so individuals can create their own scripts without clutter. For small scripts please follow the below structure:
```users/your_username/...```
You may want to create subfolders if you plan on maintaining several projects.

## APIs

Python packages for CoinAPI and Nomics are installed automatically when running the setup steps.

### CoinAPI

CoinAPI's free key has many futures but you are limited to 100 requests per day.

You can sign up for a free API key here: https://www.coinapi.io/pricing?apikey

To get started, see the following example. The API key is passed to the script as a command line parameter.
```
from coinapi_rest_v1.restapi import CoinAPIv1
test_key = sys.argv[1]
api = CoinAPIv1(test_key)
```

More information:
- Python library: https://github.com/coinapi/coinapi-sdk/blob/master/data-api/python-rest/coinapi_rest_v1/restapi.py
- API docs: https://docs.coinapi.io/

### Nomics

Nomic's free key does not have a per-day request limit, although it is rate limited to 1 request per second.

You can sign up for a free API key here: https://p.nomics.com/pricing#free-plan

To get started, see the following example:

```
from nomics import Nomics
nomics = Nomics("This-Is-A-Fake-Key-123")
```

More information:
- Python library: https://github.com/TaylorFacen/nomics-python
- API Docs: https://nomics.com/docs/



