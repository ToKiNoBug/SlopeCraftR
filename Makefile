PACKAGE_NAME = SlopeCraftR

.PHONY: all cli gui

all: cli gui

cli: $(PACKAGE_NAME)-CLI.py
	pyinstaller -c -F -p . $(PACKAGE_NAME)-CLI.py

gui: $(PACKAGE_NAME)-GUI.py
	pyinstaller -w -F -p . $(PACKAGE_NAME)-GUI.py
