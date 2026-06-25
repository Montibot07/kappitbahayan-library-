# KAPPitbahayan Virtual Library — GitHub Pages Site

Auto-refreshes from the Google Sheet every hour via GitHub Actions.

## Setup (one-time)

### 1. Enable GitHub Pages with Actions
Go to **Settings → Pages → Source** and set it to **GitHub Actions**.

### 2. Set workflow permissions
Go to **Settings → Actions → General → Workflow permissions** and enable:
- ✅ Read and write permissions

### 3. Run the workflow once manually
Go to **Actions → Fetch Sheet & Deploy → Run workflow** to trigger the first build without waiting an hour.

## How it works 

```
Every hour
  └─ GitHub Actions runs fetch_csv.py
       └─ Downloads CSV from Google Sheets
            └─ Saves to docs/_data/library.csv
                 └─ Jekyll builds the site
                      └─ Deployed to GitHub Pages
```

## Updating the data

Just update the Google Sheet — the site will reflect changes within the hour.
No code changes needed.

## File structure

```
.github/workflows/fetch-and-deploy.yml  ← hourly schedule + deploy
scripts/fetch_csv.py                    ← fetches the CSV
docs/
  _config.yml                           ← Jekyll config
  _data/library.csv                     ← auto-generated, do not edit
  index.html                            ← the library page
```
