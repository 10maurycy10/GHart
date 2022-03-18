while IFS= read -r line; do
	date -d "${line}"
done
