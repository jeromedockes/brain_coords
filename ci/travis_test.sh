#!/bin/bash -x

src_dir=$(pwd)
mkdir -p "$TEST_DIR"
cd "$TEST_DIR"
pytest -v --pyargs brain_coords --cov=brain_coords --cov-report=xml
cp .coverage coverage.xml "$src_dir"
