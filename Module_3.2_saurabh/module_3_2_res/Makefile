# Define default values for variables
START_DATE ?= 1-1-2023
END_DATE ?= 1-12-2023

# Target for running the mapper script
run_mapper:
	@echo "Running mapper script for files from START_DATE=$(START_DATE) to END_DATE=$(END_DATE)"
	@python3 mapper_util.py | while read -r file_path; do \
		python3 mapper.py Responses/$$file_path $(START_DATE) $(END_DATE); \
	done
