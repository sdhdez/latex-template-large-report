#!/bin/sh

latexmk -synctex=1 \
    -interaction=nonstopmode \
    -file-line-error \
    -xelatex \
    -shell-escape \
    -outdir=./ \
    "$@" \
    main.tex
