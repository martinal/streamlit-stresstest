#!/bin/bash
set -e
source $(pwd)/venv/bin/activate
export PYTHONPATH=$(pwd)/libs

streamlit run main.py \
	--runner.magicEnabled=False \
	--runner.fastReruns=True \
	--logger.level=warning \
	--logger.enableRich=True \
	--server.runOnSave=True \
	--browser.gatherUsageStats=False
