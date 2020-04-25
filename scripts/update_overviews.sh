#!/usr/bin/env bash

BASE_DIR="$(realpath $(dirname $0)/..)"

cd "${BASE_DIR}"

for file in $(ls ${BASE_DIR}/overviews/raw/*_radar.dds); do
    target="${BASE_DIR}/overviews/$(basename "${file}" _radar.dds).jpg"
    name="$(basename "${target}" .jpg)"
    echo "Creating $(basename "${target}")"
    convert "${file}" "${target}"
    case "${name}" in
        de_lake)
	    convert -flip "${target}" "${target}"
	    ;;
    esac
    bu="${target}.bu"
    jpegtran "${target}" > "${bu}"
    mv "${bu}" "${target}"
done

for file in $(ls ${BASE_DIR}/overviews/raw/*_radar_spectate.dds); do
    target="${BASE_DIR}/overviews/$(basename "${file}" _radar_spectate.dds)_spectate.jpg"
    name="$(basename "${target}" .jpg)"
    echo "Creating $(basename "${target}")"
    convert "${file}" "${target}"
    case "${name}" in
        de_lake)
	    convert -flip "${target}" "${target}"
	    ;;
    esac
    bu="${target}.bu"
    jpegtran "${target}" > "${bu}"
    mv "${bu}" "${target}"
done
