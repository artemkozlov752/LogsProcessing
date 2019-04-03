# LOGS PARSING

## Description
This module implements the parsing of logs in zip format.
E.g. log-files can be placed in LogsProcessing/logs.zip/logs/

## How to launch main.py
```
1. create and source venv
2. cd LogsProcessing
3. pip3.6 install -r requirements.txt
4. python3.6 main.py --path_to_zip="./logs.zip" --print
```
If on the step 4 there is no arguments path_to_zip and print, then default values are used:
- path_to_zip="./logs.zip"
- data is not printed on console

## How to test the module
```
1. create and source venv
2. cd LogsProcessing
3. pip3.6 install -r requirements.txt
4. python3.6 -m pytest --cov=. tests/
```
## How to check logs
See `LogsProcessing/application_logs/info.log`

All necessary configs are in `LogsProcessing/configs/`

## Result
The result csv will be in the `LogsProcessing/grouped_data/grouped_data.csv`
