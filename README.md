# GithubWebHookApp

This GithubWebHook service listens for organizational events to know when a 
repository has been created. When the repository is created, we automate the 
protection of the main branch. After that, it notifies you with __@mention__ in an 
issue within the repository that outlines the protections that were added.

## Prerequisites

In order to run this project on your local machine, we will use [ngrok](https://ngrok.com/) or [Localtunnel](https://github.com/localtunnel/localtunnel) to send webhooks 
to the local machine without exposing it to the internet. 

### Install ngrok

To install ngrok folow these steps:

- MacOs. Make sure you install [Homebrew](https://brew.sh/) or [download file](https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-darwin-amd64.zip)
    ```sh
        brew install ngrok/ngrok/ngrok
    ```
- Windows users. Install ngrok via Chocolatey or [download file](https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-windows-amd64.zip)
    ```sh
        choco install ngrok
    ```
- Add auth token. If you don't have authtoken, then sign up in [ngrok](https://dashboard.ngrok.com/get-started/setup) for an account 
    ```sh
        ngrok config add-authtoken <token>
    ```
- Start a tunnel
    ```sh
        ngrok http <port>
    ```
For additional resources, please check [ngrok documentation](https://ngrok.com/docs)

### Installation 

* [Python 3](https://www.python.org/downloads/)

* [ngrok](https://ngrok.com/docs)

* Install requirements.txt file
    ```
    pip install -r requirements.txt
    ```

## Set the environment variables

* Set an environment variable folder 
    ```
    .env
    ```
* Add Github Token and Webhook secret to the .env folder
    ```
    GH_TOKEN=<token>
    GH_WEBHOOK_SECRET=<your-webhook-secret>
    ```
*Note*= For the "Webhook secret", create a password to secure your webhook 
endpoints. Use the following command:
    ```
    ruby -rsecurerandom -e 'puts SecureRandom.hex(20)'
    ```

### Start the server

* Run python app.py file local web service
    ```
    python3 app.py
    ```
* Forward service via
    ``` 
    ngrok http 5000
    ```
*Note*: the forwarding address (ie. https://9ddd-141-156-20-4.ngrok.io) which 
can be found in the output of the ngrok application.

## Usage

This web service is intended to listen for a GitHub organization webhook events 
triggered when a repository has been created. The webhook to listen is this. 
https://docs.github.com/en/developers/webhooks-and-events/webhook-events-and-payloads#repository

### Set up your Webhook in your Github Organization 

1. Go to Settings in your organization account
2. Under code and automation, select Webhooks
3. Select ```Add a Webhook```
4. Under Payload Url, copy the forwarding address from ngrok (ie. https://9ddd-141-156-20-4.ngrok.io)
5. Content type, select ```application/json```
6. Add your Webhook secret (optional)
7. Select the events you want to trigger 
8. Once all the steps are completed, select ```Add Webhook```

Once you create a new repository, it will trigger the branch protection and an 
issue will be created for the repository. When receiving a Webhook, the expected 
payload object: action ... 'created'


## Additional Feedback and Improvement

Payloads are capped at 25MB.  If your event generates a larger payload, a webhook will not be fired. It is important to monitor payload size to ensure delivery.

Webhooks are only subscribed to the push event. You can change the list of subscribed events anytime.

You can use cloud provider such as Google Cloud Build and/or AWS Lambda, API Gateway and EC2.

## Resources

https://docs.github.com/en/developers/apps/guides/using-the-github-api-in-your-app

https://docs.github.com/en/rest/branches/branches#update-branch-protection

https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows

https://github.com/zkoppert/Auto-branch-protect

https://docs.github.com/en/enterprise-server@3.3/developers/webhooks-and-events/webhooks/webhook-events-and-payloads




