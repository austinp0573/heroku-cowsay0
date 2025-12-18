# Deploy to Heroku & Custom Domain

## 1. Prepare

Make sure you have a Heroku account and the Heroku CLI installed.

Log in to Heroku:

```bash
heroku login
```

## 2. Project Setup

In your project directory, create these files if missing:

1. `requirements.txt`

```bash
pip freeze > requirements.txt
```
or if you're using uv (and you should be using uv, it's great)

```bash
uv export --format requirements-txt --no-hashes --no-dev > requirements.txt
```

2. `Procfile`

add: `web: uvicorn main:app --host=0.0.0.0 --port=$PORT`

3. Initialize git:

```bash
git init
git add .
git commit -m "your commit message"
```

## 3. Deploy to Heroku
- Create app:
  ```
  heroku create heroku-cowsay0
  ```
- Push code:
  ```
  git push heroku main
  ```
- Open app:
  ```
  heroku open
  ```

## 4. Set Custom Domain (I used caas.tusko.org)
- Add domain to Heroku:
  ```
  heroku domains:add caas.tusko.org
  ```
- Get DNS target:
  ```
  heroku domains
  ```
  (Copy the DNS target, e.g. `caas-tusko.herokuapp.com`)
- In your DNS provider (for tusko.org), add a CNAME record:
  - Name: `caas`
  - Type: `CNAME`
  - Value: (the DNS target from above)
- Wait for DNS to propagate (can take minutes to hours).

## 5. Test
- Visit [https://caas.tusko.org](https://caas.tusko.org)

## 6. After changes/updates

Make sure you're logged into **Heroku**

```bash
heroku login
```

Add changes, commit changes and push to **Heroku**

```bash
git add .
git commit -m "message describing the update"
git push heroku <whatever branch you use>
```

## 7. Enable automatic deploys from GitHub

The repository can be added to GitHub, after doing so, in the Heroku Dashboard you can configure it to automatically redeploy based on changes push to your GitHub Repository

You can set this up entirely in the Heroku web dashboard. This is the standard "Set it and forget it" method.

### Steps to Enable Automatic Deploys

1. Log in to your **Heroku Dashboard**.
2. Click on your **App**.
3. Go to the **Deploy** tab (top menu).
4. Under "Deployment method," select **GitHub**.
5. Click the **Connect to GitHub** button (you may need to authorize Heroku).
6. **Search** for your repository name and click **Connect**.
7. Scroll down to the "Automatic deploys" section and click **Enable Automatic Deploys**.

### Optional: Run Your First Deploy Now

If there has been a change to the Project since you're last push to `heroku`, enabling this **will not** cause Heroku to recognize that there was a change relative to what is currently running on the service and do an automatic deploy as enabled above, if you want that to happen, just go down right below the Section to Enable Automatic Deploys and click the `Deploy Branch` button (ensuring that the desired branch is the one selected)