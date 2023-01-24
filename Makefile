install:
	pip install .

test:
	folder_sync test_source/ test_replica/ 10 logs/log.txt