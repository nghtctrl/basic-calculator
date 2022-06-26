test:
	python3 -m src.unit_tests.run

clean:
	rm -r src/__pycache__
	rm -r src/parser/__pycache__
	rm -r src/unit_tests/__pycache__
