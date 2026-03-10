#!/usr/bin/env bash

target_date=$(gdate --iso-8601=date --date "$1")

cat <<EOF >./content/Weeknotes/"$target_date".md
Title: Weeknotes

Weeknotes for the week finishing $(gdate --date="$target_date" "+%A,%e %B %G").
EOF
