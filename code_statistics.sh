#!/usr/bin/env bash

bundle exec github-linguist
echo
echo
cloc --exclude-list-file=.clocignore src other
