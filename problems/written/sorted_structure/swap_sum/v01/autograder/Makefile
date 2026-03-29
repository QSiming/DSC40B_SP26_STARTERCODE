.PHONY: public
public: _structure
	cp tests/__init__.py tests/test_public.py build/tests
	cd build && zip -r setup-public.zip *


.PHONY: private
private: _structure
	cp tests/__init__.py tests/test_private.py build/tests
	cd build && zip -r setup-private.zip *


.PHONY: _structure
_structure:
	rm -rf build
	mkdir -p build
	cp setup/* build
	mkdir -p build/tests


.PHONY: test
test:
	cp -r tests solution
	cd solution && python3 -m unittest
	rm -rf solution/tests
