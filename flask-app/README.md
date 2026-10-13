\# ACEest Fitness \& Gym



\## 1. Project Overview

ACEest Fitness \& Gym is a Python Flask application developed as part of a DevOps assignment. It demonstrates application development, automated testing, containerization, and CI pipeline integration.



\## 2. Technologies Used

\- Python

\- Flask

\- Pytest

\- Git and GitHub

\- Docker

\- GitHub Actions

\- Jenkins



\## 3. Application Features

\- Home page with a welcome message and application status.

\- Health-check endpoint.

\- Retrieve the list of gym members.

\- Retrieve a member using their ID.

\- Automated tests for application endpoints and member operations.



\## 4. Project Structure



```text

ACEest-Fitness-Gym/

├── app.py

├── requirements.txt

├── Dockerfile

├── README.md

├── tests/

│   ├── conftest.py

│   └── test\_app.py

└── .github/

&#x20;   └── workflows/

&#x20;       └── ci.yml

```



\## 5. Local Setup and Execution



\### Prerequisites

Install Python 3.13 or a compatible Python version and Git.



\### Install dependencies

Open a terminal in the project folder and run:



```bash

python -m pip install -r requirements.txt

python -m pip install pytest

```



\### Run the application



```bash

python app.py

```



Open the application at `http://127.0.0.1:5000`.



\### Run automated tests



```bash

python -m pytest -v

```



The test suite validates the application's endpoints and member-related functionality.



\## 6. Manual Testing



Test the following endpoints using a browser or an API client:



| Endpoint | Expected purpose |

|---|---|

| `/` | Display the welcome message and application status |

| `/health` | Return the health status |

| `/members` | Return the list of gym members |

| `/members/1` | Retrieve an existing member |

| `/members/999` | Verify handling of a non-existing member |



Start the Flask application before testing these endpoints. The response for a non-existing member should follow the application's implemented error-handling behavior.



\## 7. GitHub Actions CI Pipeline



The workflow is located at `.github/workflows/ci.yml`.



When code is pushed to the `main` branch or a pull request targets `main`, GitHub Actions:

1\. Checks out the repository.

2\. Sets up Python.

3\. Installs application dependencies and Pytest.

4\. Runs the automated test suite.

5\. Reports whether the tests pass or fail.



This provides early feedback and helps prevent code changes from being merged without passing tests.



\## 8. Jenkins CI/CD Integration



Jenkins can be configured as an additional CI/CD server to:

1\. Check out source code from GitHub.

2\. Install Python dependencies.

3\. Execute automated tests using Pytest.

4\. Build a Docker image after successful tests.

5\. Publish the image to a configured container registry, if required.

6\. Deploy the application to a configured environment.



A Jenkins pipeline requires a configured Jenkins server, credentials, Docker access, and deployment settings. These steps should be verified in the actual environment before claiming a successful deployment.



\## 9. Docker



Build the Docker image:



```bash

docker build -t aceest-fitness-gym .

```



Run the container:



```bash

docker run --rm -p 5000:5000 aceest-fitness-gym

```



Docker Desktop and the Docker engine must be running for these commands to work.



\## 10. Verification



The automated test suite has been run locally. Record the actual GitHub Actions, Docker, and Jenkins results separately after verifying each integration.



\## 11. Repository



GitHub repository: https://github.com/2025tm93023/ACEest-Fitness-Gym

