TESTS_PATH="connect_iq_ebook.tests"
# TODO have all path settings in settings.py
INPUT_TEXT_PATH="test.txt"
CONNECTIQ_SDK_DIR="/home/user/connectiq/connectiq-sdk-lin-3.1.9-2020-06-24-1cc9d3a70"
PRG_NAME="test.prg"
DEVICE_ID="fenix5"

BIN=./venv/bin

test:
	$(BIN)/python -m unittest $(TESTS_PATH)

book:
	$(BIN)/make-connect-iq-ebook -d $(DEVICE_ID) -i $(INPUT_TEXT_PATH)

simulate:
	$(CONNECTIQ_SDK_DIR)/bin/simulator &
	$(CONNECTIQ_SDK_DIR)/bin/monkeydo $(PRG_NAME) $(DEVICE_ID)

# TODO reuse 'make book' and 'make simulate' without copypaste
reload:
	killall simulator  || true
	$(BIN)/make-connect-iq-ebook -d $(DEVICE_ID) -i $(INPUT_TEXT_PATH)
	$(CONNECTIQ_SDK_DIR)/bin/simulator &
	$(CONNECTIQ_SDK_DIR)/bin/monkeydo $(PRG_NAME) $(DEVICE_ID)

load:
	cp $(PRG_NAME) /media/user/GARMIN/GARMIN/APPS/
