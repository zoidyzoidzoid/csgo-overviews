#!/usr/bin/env bash
{
  echo "# Overviews"
  for i in $(echo overviews/*.jpg); do
    echo "## $(echo $i | cut -d "/" -f 2- | cut -d "." -f 1)"
    echo "![]($i)"
    echo
  done
} > overviews.md
