TESTS_PATH="connect_iq_ebook.tests"
# TODO have all path settings in settings.py
INPUT_TEXT_PATH="connect_iq_ebook/tests/catch22.txt"
CONNECTIQ_BIN_DIR="/home/user/connectiq/connectiq-sdk-lin-3.0.11-2019-4-30-cd45859/bin"
PRG_PATH="/home/user/fascinus/app/news.prg"
DEVICE_ID="fenix5"

test:
	python -m unittest $(TESTS_PATH)

book:
	make-connect-iq-ebook -d $(DEVICE_ID) -i $(INPUT_TEXT_PATH)

simulate:
	cd $(CONNECTIQ_BIN_DIR) && ./simulator &
	cd $(CONNECTIQ_BIN_DIR) && ./monkeydo $(PRG_PATH) $(DEVICE_ID)
