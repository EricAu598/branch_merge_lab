#!/bin/bash

echo "=== Branch Merge Lab - Current State ==="
echo ""

echo "📊 Branch Overview:"
git branch -a
echo ""

echo "📈 Commit Graph (All Branches):"
git log --oneline --graph --all --decorate
echo ""

echo "🔍 Branch Relationships:"
git show-branch --all
echo ""

echo "📋 Current Branch Status:"
echo "Current branch: $(git branch --show-current)"
echo "Total commits: $(git rev-list --all --count)"
echo ""

echo "🎯 Ready to test merge scenarios!"
echo "See MERGE_SCENARIOS.md for detailed instructions."
