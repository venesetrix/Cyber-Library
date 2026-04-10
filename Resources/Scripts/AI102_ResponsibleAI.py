from azure.ai.ml import MLClient, Input
from azure.ai.ml.dsl import pipeline
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv
import os

# AI-102 Prep - Azure Machine Learning SDK v2 for Responsible AI insights
# WARNING: NOT WORKING!

# Helper function to setup the ML Client
def getMLClient():

    load_dotenv()
   
    try:
        subid = os.getenv("AZURE_SUBSCRIPTION_ID")
        resGroup = os.getenv("AZURE_RESOURCE_GROUP")
        workspace = os.getenv("AZURE_ML_WORKSPACE_NAME")
    except KeyError:
        print("[-] Missing environment variable")
        print("[-] Set them before running this sample.")
        return False
    
    mlClient = MLClient(DefaultAzureCredential(), subid, resGroup, workspace)

    return mlClient

MLCLIENT = getMLClient()

@pipeline()
def rai_pipeline(model, train_data, test_data):

    rai_component = MLCLIENT.components.get(
            name="rai_insights_constructor",
            version="0.1.0"
    )

    rai_job = rai_component(
        model_input=model,
        train_data=train_data,
        test_data=test_data,
        target_column_name="label"
    )
    return {
        "rai_insights": rai_job.outputs.rai_insights_dashboard
    }

def defineResponsibleAIinsights():

    job = MLCLIENT.jobs.create_or_update(
        rai_pipeline(
            model=Input(type="mlflow_model", path="azureml:model@latest"),
            train_data=Input(type="mltable", path="azureml:train@latest"),
            test_data=Input(type="mltable", path="azureml:test@latest"),
        ),
        experiment_name="rai-demo"
    )

if __name__ == "__main__":

    defineResponsibleAIinsights()