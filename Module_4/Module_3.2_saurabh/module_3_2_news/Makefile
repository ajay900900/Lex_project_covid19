# Default start and end dates if not provided
START_DATE ?= 1-1-2023
END_DATE ?= 1-12-2023

# Target to run the mapper script
run_mapper:
	@echo "Running mapper script with START_DATE=$(START_DATE) and END_DATE=$(END_DATE)"
	@python3 mapper_util_32_saurav.py | while read -r file_path; do \
		python3 mapper_32_saurav.py News/$$file_path $(START_DATE) $(END_DATE); \
	done
