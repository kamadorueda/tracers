#! /usr/bin/env bash

source 'build/include/generic/shell-options.sh'

function main {
      echo '[INFO] Linting SDK' \
  && pushd sdk \
    &&  poetry run mypy \
          --ignore-missing-imports \
          --strict \
          . \
    &&  poetry run prospector \
          --strictness veryhigh \
          --without-tool pep257 \
    &&  poetry run prospector \
          --strictness veryhigh \
          --without-tool pep257 \
          ../examples \
  &&  popd \
  ||  return 1
}

main
