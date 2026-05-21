# Create Pull Request Using Git Only

You are helping create a Pull Request using only Git commands.

Steps:

1. Detect current branch
2. Ensure user is not on main branch
3. Push branch to origin
4. Get GitHub remote URL
5. Generate compare URL for PR creation
6. Print final PR URL clearly

Run these commands:

```bash
CURRENT_BRANCH=$(git branch --show-current)

echo "Current branch: $CURRENT_BRANCH"

if [ "$CURRENT_BRANCH" = "main" ]; then
  echo "Error: You are on main branch."
  echo "Switch to feature branch first."
  exit 1
fi

git push origin $CURRENT_BRANCH

REMOTE_URL=$(git remote get-url origin)

echo "Remote URL: $REMOTE_URL"

# Convert SSH URL to HTTPS
REPO_PATH=$(echo $REMOTE_URL | sed 's/git@github.com://g' | sed 's/\.git//g')

PR_URL="https://github.com/$REPO_PATH/compare/main...$CURRENT_BRANCH"

echo ""
echo "======================================="
echo "Create Pull Request using this URL:"
echo "$PR_URL"
echo "======================================="
```

