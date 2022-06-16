# GithubWebHookApp

This GithubWebHook service listens for organizational events to know when a 
repository has been created. When the repository is created, we automate the 
protection of the main branch. After that, it notifies you with __@mention__ in an 
issue within the repository that outlines the protections that were added.

## Prerequisites

In order to run this project on your local machine, we will use [ngrok](https://ngrok.com/) or [Localtunnel](https://github.com/localtunnel/localtunnel) to send webhooks 
to the local machine without exposing it to the internet. 

## Usage


