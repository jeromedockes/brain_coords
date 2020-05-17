#!/bin/bash -x

src_dir=$(pwd)
tests_dir=$(mktemp -d)
pushd "$tests_dir"
pytest --pyargs brain_coords --cov=brain_coords --cov-report=xml
cp .coverage coverage.xml "$src_dir"
popd
