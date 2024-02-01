# GitHub Stars to Pinboard Bookmarks
This Serverless function runs on AWS Lambda once per hour. It saves the last 8 repos your Starred as [Pinboard](https://pinboard.in) bookmarks and tags them as "github".

# Installation
* You need Node.js installed locally
* You need an AWS Account setup along with access credentials setup locally
* You need Python 3 installed locally to test
* You need to create a [GitHub Personal Access Token](https://github.com/settings/tokens). Fine-grained ones are probably more secure but have a max lifetime of a year.
* You need to get your [Pinboard API Token](https://pinboard.in/settings/password)

* Open a Powershell window on Windows (or bash etc on Linux)
* Install the Serverless framework with `npm install -g serverless`
* Install the Serverless Python plugin with `npm install`
* Create a Python Virtual Environment with `python -m venv venv`
* Activate the Python Virtual Environment in Powershell on Windows with `.\venv\Scripts\Activate.ps1`
* Install Python modules with `pip install -r requirements.txt`
* Copy serverless-template.yml to serverless.yml
* Edit serverless.yml and configure your GitHub Username, GitHub Access Token and Pinboard Access Token
* Deploy to AWS Lambda with `serverless deploy`
* Wait an hour for the first run or manually open the URL that the deploy command lists on successful execution
* You should see the 8 most recent GitHub Starred repos listed as bookmarks on Pinboard
