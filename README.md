# CI/CD Pipeline with Jenkins and GitHub Actions

This repository demonstrates a simple Python Flask application integrated with two CI/CD pipelines:
- Jenkins
- GitHub Actions

---

## 🚀 Application Overview

A basic Flask app returning "Hello World" on the root endpoint:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello world"

if __name__ == "__main__":
    app.run(debug=True, port=3005)
```

---

## 🛠 Jenkins Setup

### 1. Jenkins Installation
Install Jenkins on a VM or use Jenkins on a cloud service.

### 2. Configure Jenkins
Install the following plugins:
- Git
- Pipeline
- Email Extension (for notifications)
  - Setup & Test Email Configuration using App password

Ensure Python 3 and `venv` are available on the Jenkins server.

### 3. Jenkinsfile

Place the following `Jenkinsfile` in the pipleline box of Jenkins. In case, you want to change the GITURL, you may edit the environment variable to match your GITURL


## ⚙ GitHub Actions Setup

### 1. Workflow Configuration

Configure EMAIL ID & Password as Repository secrets to use in Gitaction .yml, Save this file as `.github/workflows/mail.yml`:

```yml
name: CI Pipeline

name: CI Pipeline

on:
  workflow_dispatch

jobs:
  build-test-deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Install Dependencies
        run: |
          python -m venv venv
          source venv/bin/activate
          pip install -r requirements.txt

      - name: Run Tests
        run: |
          source venv/bin/activate
          pytest

      - name: Deploy (Run Flask app in background)
        if: success()
        run: |
          source venv/bin/activate
          nohup python app.py &
          sleep 5  
          curl http://127.0.0.1:3005  
          sleep 10

      - name: Send Email Notification
        if: always()
        uses: dawidd6/action-send-mail@v3
        with:
          server_address: smtp.gmail.com
          server_port: 587
          username: ${{ secrets.EMAIL_USERNAME }}
          password: ${{ secrets.EMAIL_PASSWORD }}
          subject: GitHub Actions Build #${{ github.run_number }} - ${{ job.status }}
          to: your.email@example.com
          from: GitHub Actions <your.email@example.com>
          body: |
            Build Status: ${{ job.status }}
            Repository: ${{ github.repository }}
            Commit: ${{ github.sha }}
            Run URL: ${{ github.server_url }}/${{ github.repository }}/actions/runs/${{ github.run_id }}
```

---

## 🧪 Pytest Example

Save this as `test_app.py`:

```python
from app import app

def test_home():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b"Hello world" in response.data
```

---

## 📬 Email Setup Notes

- Jenkins: Configure **Extended Email Notification** in *Manage Jenkins > Configure System*.
- GitHub Actions: Store credentials in **Secrets**:
  - `EMAIL_USERNAME`
  - `EMAIL_PASSWORD`

---

## ✅ How to Run

### Locally
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

---

## 📸 Screenshots (Attach to GitHub Manually)

- Jenkins stages: Git Clone, Build, Test, Deploy

  <img width="947" alt="image" src="https://github.com/user-attachments/assets/0a534c3d-f820-4e50-beb2-c394c114d95f" />
  

- Email Notification in inbox

  <img width="581" alt="image" src="https://github.com/user-attachments/assets/9128c290-6624-4acf-8091-106261faae05" />

- GitHub Actions pipeline history

---

## 📎 Submission

- Push code with `Jenkinsfile`, `ci.yml`, and `README.md`
- Provide GitHub repo link and screenshots

