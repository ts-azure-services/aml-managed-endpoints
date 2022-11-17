infra:
	./setup/aml-workspace.sh

install:
	#conda create -n moe python=3.8 -y; conda activate moe
	pip install python-dotenv
	pip install azure-ai-ml
	pip install notebook
	pip install pandas
	pip install azure-identity


#rec_count=100000
gen_records:
	./test-endpoint/remove-json.sh #clean up records
	python ./test-endpoint/sample_data_generator.py --number_of_records 10000 #$(rec_count)
	python ./test-endpoint/sample_data_generator.py --number_of_records 100000 #$(rec_count)
	#python ./test-endpoint/sample_data_generator.py --number_of_records 1000000 #$(rec_count)
