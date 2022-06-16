# GithubWebHookApp

This GithubWebHook service listens for organizational events to know when a 
repository has been created. When the repository is created, we automate the 
protection of the main branch. After that, it notifies you with __@mention__ in an 
issue within the repository that outlines the protections that were added.

## Prerequisites

In order to run this project on your local machine, we will use [ngrok](https://ngrok.com/) or [Localtunnel](https://github.com/localtunnel/localtunnel) to send webhooks 
to the local machine without exposing it to the internet. 

### ngrok

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

Install the following:

* [Python 3](https://www.python.org/downloads/)

* [ngrok](https://ngrok.com/docs)

* (Optional) Generate requirements.txt file for your project
```sh
    pip install pipreqs
```
```sh
    pipreqs .
```

## Usage



