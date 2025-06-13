# Git Merge Scenarios Testing Guide

This guide walks you through different Git merge scenarios using the branches in this repository.

## Current Branch Structure

```
main (latest)
├── feature/fast-forward (ahead of main's initial commit)
├── feature/three-way (diverged from main's initial commit)
└── feature/conflict-demo (conflicts with current main)
```

## Scenario 1: Fast-Forward Merge

**Situation**: The target branch (main) hasn't moved since the feature branch was created.

### Steps to test:
1. Reset main to initial commit: `git reset --hard fd43843`
2. Merge feature branch: `git merge feature/fast-forward`
3. Observe: Git will simply move the main pointer forward (fast-forward)

### Expected result:
- No merge commit created
- Linear history maintained
- Main pointer moves to feature/fast-forward commit

## Scenario 2: Three-Way Merge

**Situation**: Both branches have new commits since they diverged.

### Steps to test:
1. Ensure you're on main: `git checkout main`
2. Merge feature branch: `git merge feature/three-way`
3. Observe: Git creates a merge commit with two parents

### Expected result:
- Merge commit created automatically
- Both branch histories preserved
- Diamond-shaped history pattern

## Scenario 3: Merge Conflicts

**Situation**: Same lines modified in both branches.

### Steps to test:
1. Ensure you're on main: `git checkout main`
2. Attempt merge: `git merge feature/conflict-demo`
3. Observe: Git reports conflicts in main.py and config.json
4. Resolve conflicts manually
5. Complete merge: `git add . && git commit`

### Expected result:
- Git stops and asks for manual conflict resolution
- Conflict markers (<<<<<<, ======, >>>>>>) appear in files
- Manual resolution required before completing merge

## Scenario 4: Rebase vs Merge Comparison

### Rebase approach:
1. `git checkout feature/three-way`
2. `git rebase main`
3. `git checkout main`
4. `git merge feature/three-way` (will be fast-forward)

### Merge approach:
1. `git checkout main`
2. `git merge feature/three-way`

### Compare the results:
- Rebase: Linear history, no merge commits
- Merge: Preserves branch structure, shows merge commits

## Scenario 5: Squash Merge

**Purpose**: Combine all commits from feature branch into single commit.

### Steps to test:
1. `git checkout main`
2. `git merge --squash feature/fast-forward`
3. `git commit -m "Squashed feature: Add difference calculation"`

### Expected result:
- All changes combined into one commit
- Original commit history from feature branch lost
- Clean, linear history

## Useful Commands for Exploration

- `git log --oneline --graph --all` - Visualize branch structure
- `git show-branch` - Show branch relationships
- `git log --merge` - Show commits involved in merge conflicts
- `git diff HEAD~1 HEAD` - Compare last two commits
- `git reset --hard HEAD~1` - Undo last commit (be careful!)

## Practice Exercises

1. Try each merge scenario and observe the resulting git log
2. Create your own feature branches and practice merging
3. Intentionally create conflicts and practice resolving them
4. Compare the history after rebase vs merge operations
