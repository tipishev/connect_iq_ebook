TESTS_PATH="connect_iq_ebook.tests"
INPUT_TEXT_PATH="connect_iq_ebook/tests/catch22.txt"

test:
	python -m unittest $(TESTS_PATH)

book:
	make-connect-iq-ebook -d fenix5 -i $(INPUT_TEXT_PATH)
