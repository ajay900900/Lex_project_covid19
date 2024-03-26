# Define the variables
START_DATE ?= 1-1-2020
END_DATE ?= 1-12-2023

# Define the target to run the mapper script
run_mapper:
	@python3 mapper_util.py | while read -r file_path; do \
        python3 mapper.py ../News/$$file_path $$START_DATE $$END_DATE; \
    done