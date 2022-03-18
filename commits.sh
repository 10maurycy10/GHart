#!/bin/sh
git branch -D main
git branch main
git checkout main
cd repo
rm dummyfile
while IFS= read -r line; do
	echo "${line}" >> dummyfile
	git stage dummyfile
	GIT_COMMITTER_DATE="${line}" git commit -m "test" --date "${line}"
done
