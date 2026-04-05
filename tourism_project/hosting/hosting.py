from huggingface_hub import HfApi
import os

repo_id = "SuriyaSR/TourismPackagePurchasesDataset"
repo_type = "space"

api = HfApi(token=os.getenv("HF_TOKEN"))
repo_id_data = "SuriyaSR/TourismPackagePurchases"
api.upload_folder(
    folder_path="tourism_project/deployment",
    repo_id=repo_id,
    repo_type=repo_type,
    path_in_repo=repo_id,
)

print("Deployment files successfully uploaded to Hugging Face Space -",repo_id)
