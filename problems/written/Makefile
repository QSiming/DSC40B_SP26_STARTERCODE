.PHONY: previews
previews:
	fd --type d 'v\d\d$$' --exec bash -c "echo Working on {} && cd {} && make _build/preview/build/preview.pdf"
