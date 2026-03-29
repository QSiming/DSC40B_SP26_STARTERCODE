SHELL = /usr/bin/env bash

# path to the root of the git repo
REPO_ROOT = $(shell git rev-parse --show-toplevel)

# path to the common directory
COMMON_DIR = ${REPO_ROOT}/problems/written/COMMON

# options to pass to latexmk when run interactively
INTERACTIVEOPTS = -pvc

# the command to run latexmk
TEXFOT_IGNORES = --ignore "Package fontspec Warning:"
LATEXMKCMD = texfot ${TEXFOT_IGNORES} latexmk -shell-escape -lualatex -outdir=build -interaction=nonstopmode


.PHONY: preview
preview:
	prepare-problem-preview
	cd _build/preview && ${LATEXMKCMD} ${INTERACTIVEOPTS}
	touch _build/preview/build/preview.pdf


_build/preview/build/preview.pdf: problem.tex
	${MAKE} preview INTERACTIVEOPTS= || (rm -f _build/preview/build/preview.pdf; exit 1)


.PHONY: clean
clean:
	rm -rf _build
