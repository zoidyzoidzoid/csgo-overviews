#!/usr/bin/env bash
{
  echo "# Overviews"
  for i in $(echo overviews/*.jpg); do
    fn="$(basename "${i}" ".jpg")"
    title="${fn}"
    if [[ "${fn}" =~ .*_spectate$ ]]; then
      title="$(basename "${fn}" _spectate) (Spectator Version)"
    fi
    echo "## ${title}"
    echo "![]($i)"
    echo
  done
} > overviews.md
