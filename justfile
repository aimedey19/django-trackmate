_default:
    @just --list --unsorted

build:
    #!/bin/bash
    python -m build

deploy:
    #!/bin/bash
    twine upload dist/*
