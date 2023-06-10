#!/bin/bash
# Clone the numpy git repo and try to rewrite all python files in it
# TODO fix the commit hash but keep shallow commit somehow

mkdir -p ~/.cache/compactify/tests
cd ~/.cache/compactify/tests
rm -rf numpy
git clone --depth=1 https://github.com/numpy/numpy.git
cd numpy
compactify $(git ls-files | grep 'numpy\/core\/\w*\.py$')
