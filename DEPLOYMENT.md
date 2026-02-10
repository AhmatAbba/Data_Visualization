# Deployment Guide for Hello Project

## 1. Push to GitHub
First, commit and push your code to a new GitHub repository.

```bash
git init
git add .
git commit -m "Initial commit"
# Link your repository
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
```

## 2. Supabase (Database)
1.  Create a new project in Supabase.
2.  Go to **Project Settings** -> **Database**.
3.  Scroll down to **Connection parameters** or **Connection string**.
4.  Copy the **URI**. It looks like: `postgresql://postgres:password@db.supabase.co:5432/postgres`.
5.  You will need this `DATABASE_URL` for Vercel and Render environment variables.

## 3. Vercel Deployment
1.  Go to your Vercel Dashboard and click **Add New...** -> **Project**.
2.  Import your GitHub repository.
3.  The `vercel.json` file in this project should handle the configuration automatically.
4.  **Environment Variables**:
    *   Add `DATABASE_URL` with the value from Supabase.
    *   Add `SECRET_KEY` (you can generate a new one or use the one from `settings.py`, but keep it secret).
    *   Add `AdLLOWED_HOSTS` = `.vercel.app` (or `*`).
5.  Click **Deploy**.

## 4. Render Deployment
1.  Go to your Render Dashboard and click **New +** -> **Web Service**.
2.  Connect your GitHub repository.
3.  **Settings**:
    *   **Runtime**: Python 3
    *   **Build Command**: `./build.sh`
    *   **Start Command**: `gunicorn hello_project.wsgi:application`
4.  **Environment Variables**:
    *   Add `DATABASE_URL` with the value from Supabase.
    *   Add `SECRET_KEY`.
    *   Add `python_version`: `3.9.0` (or similar, if needed).
5.  Click **Create Web Service**.

## Notes
*   **Static Files**: `whitenoise` is configured to serve static files. If you have issues, ensure `python manage.py collectstatic` runs during the build (it is in `build.sh`).
*   **Database**: The `dj-database-url` package allows Django to use the `DATABASE_URL` environment variable to configure the database connection automatically.
