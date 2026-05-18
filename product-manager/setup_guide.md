# Daily Planner Agent — Setup Guide

**What you're building:** A scheduled co-work agent that opens a browser tab at 9am with your day plan (goals + meetings from your work Google Calendar) and at 5pm with an end-of-day review and focus score.

---

## Files in This Package

| File | Purpose |
|------|---------|
| `daily_planner.py` | Main Python script |
| `morning_planner.html` | 9am browser tab UI |
| `evening_review.html` | 5pm browser tab UI |
| `backlog.json` | Your persistent task backlog |
| `com.fox.dailyplanner.morning.plist` | Mac scheduler — 9am trigger |
| `com.fox.dailyplanner.evening.plist` | Mac scheduler — 5pm trigger |

---

## Step 1 — Create a Folder

Move all files to a permanent home. Suggested location:

```bash
mkdir ~/daily-planner
mv ~/Downloads/daily_planner.py ~/daily-planner/
mv ~/Downloads/morning_planner.html ~/daily-planner/
mv ~/Downloads/evening_review.html ~/daily-planner/
mv ~/Downloads/backlog.json ~/daily-planner/
mv ~/Downloads/*.plist ~/daily-planner/
```

---

## Step 2 — Install Python Dependencies

Open Terminal and run:

```bash
pip3 install google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

To verify it worked:
```bash
python3 -c "from googleapiclient.discovery import build; print('OK')"
```

---

## Step 3 — Set Up Work Google Calendar API

This is the step that connects to your **work** Google account specifically.

### 3a. Create a Google Cloud Project

1. Go to [console.cloud.google.com](https://console.cloud.google.com)
2. Click **New Project** → name it `Daily Planner` → click **Create**
3. Make sure you are signed in with your **work Google account** (top right)

### 3b. Enable the Calendar API

1. In the left menu go to **APIs & Services → Library**
2. Search for **Google Calendar API**
3. Click it → click **Enable**

### 3c. Create OAuth Credentials

1. Go to **APIs & Services → Credentials**
2. Click **+ Create Credentials → OAuth client ID**
3. Application type: **Desktop app**
4. Name: `Daily Planner`
5. Click **Create**
6. Click **Download JSON** → rename the file to `credentials.json`
7. Move it to your daily-planner folder:

```bash
mv ~/Downloads/credentials.json ~/daily-planner/
```

### 3d. Configure OAuth Consent Screen (if prompted)

1. Go to **OAuth consent screen**
2. User type: **External** (fine for personal use)
3. App name: `Daily Planner`
4. Add your work email as a **test user**
5. Save

### 3e. Authenticate (one-time)

Run this once in Terminal:

```bash
cd ~/daily-planner
python3 daily_planner.py test-calendar
```

A browser window will open asking you to sign into Google.

> **IMPORTANT:** When the Google sign-in page opens, make sure to select your **WORK account** (not personal). This is how the script connects to your work calendar.

After signing in, a `token.json` file will be saved. You'll never need to do this again unless you delete the token.

### 3f. Verify

```bash
python3 daily_planner.py test-calendar
```

You should see today's meetings listed in Terminal.

---

## Step 4 — Add Your Anthropic API Key

1. Go to [console.anthropic.com](https://console.anthropic.com) → API Keys → Create Key
2. Copy the key (starts with `sk-ant-...`)
3. When you open the morning planner HTML in the browser, paste it in the **Configuration** field at the top — it saves automatically in your browser's local storage

---

## Step 5 — Edit the Scheduler Files

Open both `.plist` files in a text editor and replace `YOUR_USERNAME` with your actual Mac username.

To find your username:
```bash
whoami
```

Edit the path in both files:
```xml
<string>/Users/YOUR_USERNAME/daily-planner/daily_planner.py</string>
```

For example, if your username is `fox`:
```xml
<string>/Users/fox/daily-planner/daily_planner.py</string>
```

---

## Step 6 — Install the Schedulers

Copy the plist files to the LaunchAgents folder and load them:

```bash
cp ~/daily-planner/com.fox.dailyplanner.morning.plist ~/Library/LaunchAgents/
cp ~/daily-planner/com.fox.dailyplanner.evening.plist ~/Library/LaunchAgents/

launchctl load ~/Library/LaunchAgents/com.fox.dailyplanner.morning.plist
launchctl load ~/Library/LaunchAgents/com.fox.dailyplanner.evening.plist
```

### Test that it works right now

```bash
# Test morning planner
launchctl start com.fox.dailyplanner.morning

# Test evening review
launchctl start com.fox.dailyplanner.evening
```

Your browser should open with the correct tab.

---

## Step 7 — Pre-load Your Task Backlog

Edit `backlog.json` with your real tasks:

```json
[
  { "text": "Finalise JET+ Add-Ons Product Brief", "effort": "L" },
  { "text": "Review Prina's discovery sprint comments", "effort": "M" },
  { "text": "Update Notion sprint board", "effort": "S" }
]
```

Or add tasks via Terminal:
```bash
python3 ~/daily-planner/daily_planner.py add-task "Write brief section 3" L
python3 ~/daily-planner/daily_planner.py list-tasks
```

---

## Daily Workflow

### 9:00 AM — A browser tab opens automatically
- Your work calendar meetings are pre-loaded
- Fill in your top 3 goals
- Reorder tasks by dragging (priority 1–3+ auto-updates)
- Click **Generate My Day Plan** → Claude builds your time-blocked schedule
- Click **Save Locally** to persist the plan

### 5:00 PM — A browser tab opens automatically
- Tick completed tasks ✓, carry-overs →, dropped ✕
- Rate your focus (0–10 slider)
- Answer the 4 reflection questions
- Click **Generate Tomorrow's Plan** → Claude uses carry-overs to prep tomorrow
- Carry-overs are automatically loaded into the next morning's backlog

---

## Notion Integration (Optional)

If you want the plan saved to Notion automatically:

1. Go to [notion.so/my-integrations](https://www.notion.so/my-integrations) → New Integration
2. Name it `Daily Planner` → copy the **Internal Integration Token**
3. Create a Notion database with at least: `Name` (title), `Date` (date) properties
4. Share the database with your integration (click the ••• menu on the database → Add connections)
5. Copy the database ID from the URL:
   `notion.so/workspace/THIS-IS-THE-DATABASE-ID?v=...`

Add these to your environment (in `~/.zshrc`):
```bash
export NOTION_TOKEN="your-integration-token"
export NOTION_DB_ID="your-database-id"
```

Then reload: `source ~/.zshrc`

---

## Troubleshooting

**Browser doesn't open at 9am/5pm**
- Check your Mac is awake (launchd won't run if the machine is asleep)
- Check logs: `cat /tmp/dailyplanner_morning.log`
- Check errors: `cat /tmp/dailyplanner_morning_error.log`

**Calendar shows no meetings**
- Re-run auth: `python3 ~/daily-planner/daily_planner.py test-calendar`
- Make sure you signed in with your WORK account, not personal

**To change the trigger time**
- Edit the `Hour` and `Minute` values in the plist files
- Reload: `launchctl unload ~/Library/LaunchAgents/com.fox.dailyplanner.morning.plist && launchctl load ~/Library/LaunchAgents/com.fox.dailyplanner.morning.plist`

**To stop the agent**
```bash
launchctl unload ~/Library/LaunchAgents/com.fox.dailyplanner.morning.plist
launchctl unload ~/Library/LaunchAgents/com.fox.dailyplanner.evening.plist
```

---

## File Reference

```
~/daily-planner/
├── daily_planner.py           ← main script
├── morning_planner.html       ← 9am browser UI
├── evening_review.html        ← 5pm browser UI
├── backlog.json               ← your task backlog (edit freely)
├── credentials.json           ← Google OAuth credentials (keep private)
├── token.json                 ← auto-generated after first auth
├── com.fox.dailyplanner.morning.plist
└── com.fox.dailyplanner.evening.plist

~/Library/LaunchAgents/        ← scheduler copies go here
├── com.fox.dailyplanner.morning.plist
└── com.fox.dailyplanner.evening.plist
```

---

*Built for Fox · Just Eat Senior PM · Daily Planner Agent v1*
