run_mapper:
	@read -p "Enter a country name: " user_country; \
	python3 query_data.py | grep -E "^$$user_country" | while read -r file_path; do \
		country_name=$(echo "$$file_path" | cut -d'_' -f1); \
		echo "Processing file: $$file_path"; \
		python3 mapper.py "./$$file_path" "$$country_name"; \
	done


