# managed-online-endpoint-testing
Goal of this repo is to test out the real-time and batch endpoints as part of Azure ML. Future state could be
to understand how auto-scaling triggers work, and if logs are properly reported. Borrowed the source Jupyter
notebook from
[here](https://github.com/Azure/azureml-examples/blob/main/tutorials/e2e-ds-experience/e2e-ml-workflow.ipynb). Main difference is the addition of the batch deployment, and some logic to generate slightly larger inference
json and csv payloads to test the endpoints. For example, when passing a file with a 1 million records, the
real-time endpoint fails and this is ideal for a batch endpoint to process this volume.

## Steps to run locally
1. Setup the virtual environment locally. Install needed dependencies using the `make install` command.
2. Trigger the creation of resources using the `make infra` command.
3. Use the steps in the Jupyter notebook: `e2e-ml-workflow.ipynb` to follow the sequence of steps to create
   data assets, build a training pipeline, setup both real-time and batch endpoints, and then test it with
   generated data (off the original dataset).
