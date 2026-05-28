from huggingface_hub import HfApi
import os

api = HfApi(token=os.getenv("HF_TOKEN"))
from huggingface_hub.errors import HfHubHTTPError
repo_id = "ksckaushal/Tourism-Package-Prediction"

# 1. Safely ensure the space exists with Streamlit SDK configured
try:
    print(f"Checking/Creating Space repo: {repo_id}")
    api.create_repo(
        repo_id=repo_id,
        repo_type="space",
        space_sdk="streamlit",  # Forces HF to expect a streamlit app
        private=False
    )
except HfHubHTTPError as e:
    if e.response.status_code == 409:
        print("Space already exists. Proceeding to deployment...")
    else:
        raise e
api.upload_folder(
    folder_path="tourism_project/deployment",     # the local folder containing your files
    repo_id="ksckaushal/Tourism-Package-Prediction",          # the target repo
    repo_type="space",                      # dataset, model, or space
    path_in_repo="",                          # optional: subfolder path inside the repo
)
