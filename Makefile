install:
	pip install .

test:
	folder_sync test_source/ test_replice/ 10 logs/log.txt