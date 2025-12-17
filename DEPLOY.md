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