#!/bin/bash
# push-skill.sh — Stage all changes and push to GitHub
# Usage: ./push-skill.sh "Your commit message"
# Example: ./push-skill.sh "Add experiment-designer skill"

set -e

MSG=${1:-"Update Claude PM skills"}

echo "📦 Staging all changes..."
git add -A

# Check if there's anything to commit
if git diff --cached --quiet; then
  echo "✅ Nothing new to commit — everything is up to date."
  exit 0
fi

echo "💬 Committing: $MSG"
git commit -m "$MSG"

echo "🚀 Pushing to GitHub..."
git push origin main

echo "✅ Done! Skills pushed to https://github.com/fahadnari/Claude-skills"
