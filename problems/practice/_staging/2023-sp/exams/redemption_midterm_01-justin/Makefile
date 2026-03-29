SHELL = /usr/bin/env bash


# path to the root of the git repo
REPO_ROOT = $(shell git rev-parse --show-toplevel)

# files used to determine if artifacts need to be rebuilt;
# we'll follow symlinks to find changed files in the problems directory
# we'll only search for files and directories, because the problems directory may
# contain relative symlinks that will not be resolvable with the current working directory;
# make will think these dependencies cannot be built.
EXAM_DEPENDENCIES = $(shell fd . --no-ignore --exclude build --exclude '*.tex.input' --follow --type f --type d)

# options to pass to latexmk when run interactively
INTERACTIVEOPTS = -pvc

# the command to run latexmk
LATEXMKCMD = latexmk -shell-escape -lualatex -outdir=build -interaction=nonstopmode


.PHONY: solution
solution:
	${LATEXMKCMD} ${INTERACTIVEOPTS} \
		-jobname=solution \
		exam.tex
	touch build/solution.pdf # update timestamp; latexmk may not


.PHONY: exam
exam:
	${LATEXMKCMD} ${INTERACTIVEOPTS} \
		-jobname=exam \
		-usepretex='\def\hidesoln{1}' \
		exam.tex
	touch build/exam.pdf # update timestamp; latexmk may not


all: build/exam.pdf build/solution.pdf

build/exam.pdf: ${EXAM_DEPENDENCIES}
	${MAKE} exam INTERACTIVEOPTS= VERSION=A

build/solution.pdf: ${EXAM_DEPENDENCIES}
	${MAKE} solution INTERACTIVEOPTS= VERSION=A

.PHONY: clean
clean:
	rm -rf build
