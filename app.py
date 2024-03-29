import json
import os  
import time  

import requests  
from flask import Flask, request  

app = Flask(__name__)


@app.route("/", methods=["POST"])
def webhook():
    payload = request.get_json()
    print("payload", payload)
    user = "claudiabringaseverett"
    cred = os.environ["GH_TOKEN"] #os.environ["GH_TOKEN"]
    if payload is None:
        print("POST was not formatted in JSON")

    # Verify the repo was created
    try:
        if payload["action"] == "created":
            time.sleep(1)
            branch_protection = {
                "required_status_checks": {"strict": True, "contexts": ["default"]},
                "enforce_admins": False,
                "required_pull_request_reviews": None,
                "restrictions": None,
            }
            session = requests.session()
            session.auth = (user, cred)
            response_1 = session.put(
                payload["repository"]["url"] + "/branches/main/protection",
                json.dumps(branch_protection),
            )

            if response_1.status_code == 200:
                print(
                    "Branch protection created successfully. Status code: ",
                    response_1.status_code,
                )

                # Create issue in repo
                try:
                    if payload["repository"]["has_issues"]:
                        issue = {
                            "title": "New Protection Added",
                            "body": "@"
                            + user
                            + " A new branch protection was added to the master branch.",
                        }
                        session = requests.session()
                        session.auth = (user, cred)
                        response_2 = session.post(
                            payload["repository"]["url"] + "/issues", json.dumps(issue)
                        )
                        if response_2.status_code == 201:
                            print(
                                "Issue created successfully. Status code: ",
                                response_2.status_code,
                            )
                        else:
                            print(
                                "Unable to create issue. Status code: ",
                                response_2.status_code,
                            )
                    else:
                        print(
                            "This repo has no issues so one cannot be created at this time."
                        )
                except KeyError:
                    pass
            else:
                print(response_1.content)
                print(
                    "Unable to create branch protection. Status code: ",
                    response_1.status_code,
                )
    except KeyError:
        pass

    return "OK"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5001")
