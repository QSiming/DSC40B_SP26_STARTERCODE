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

# the exam version to build
VERSION = A

# the command to run latexmk
LATEXMKCMD = latexmk -shell-escape -lualatex -outdir=build -interaction=nonstopmode --file-line-error

.PHONY: solution
solution:
	${LATEXMKCMD} ${INTERACTIVEOPTS} \
		-jobname=solution-${VERSION} \
		-usepretex='\def\version{${VERSION}}' \
		exam.tex
	touch build/solution.pdf # update timestamp; latexmk may not


.PHONY: exam
exam:
	${LATEXMKCMD} ${INTERACTIVEOPTS} \
		-jobname=exam-${VERSION} \
		-usepretex='\def\hidesoln{1}\def\version{${VERSION}}' \
		exam.tex
	touch build/exam.pdf # update timestamp; latexmk may not


all: build/exam-A.pdf build/solution-A.pdf build/exam-B.pdf build/solution-B.pdf

build/exam-A.pdf: ${EXAM_DEPENDENCIES}
	${MAKE} exam INTERACTIVEOPTS= VERSION=A

build/exam-B.pdf: ${EXAM_DEPENDENCIES}
	${MAKE} exam INTERACTIVEOPTS= VERSION=B

build/solution-A.pdf: ${EXAM_DEPENDENCIES}
	${MAKE} solution INTERACTIVEOPTS= VERSION=A

build/solution-B.pdf: ${EXAM_DEPENDENCIES}
	${MAKE} solution INTERACTIVEOPTS= VERSION=B

.PHONY: clean
clean:
	rm -rf build
