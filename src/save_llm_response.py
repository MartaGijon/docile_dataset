import os
import json


def save_llm_output(response, file_name):
    # 1. Define folder names
    folders = {
        "prompts": "dataset_generation/prompts",
        "pydantic": "dataset_generation/pydantic",
        "ground_truth": "dataset_generation/ground_truth",
    }

    # Create the folders if they don't exist
    for folder in folders.values():
        os.makedirs(folder, exist_ok=True)

    # 2. Define the contents
    # Content 1: Prompt saved as a Python variable
    prompt_content = f"query= '{str(response.query)}'"

    # Content 2: Pydantic classes with their necessary imports
    pydantic_content = response.pydantic_model

    # Content 3: Original Ground Truth dictionary
    ground_truth_data = response.ground_truth_json

    # 3. Full file paths
    prompt_path = os.path.join(folders["prompts"], f"{file_name}.py")
    pydantic_path = os.path.join(folders["pydantic"], f"{file_name}.py")
    json_path = os.path.join(folders["ground_truth"], f"{file_name}.json")

    # 4. Save the files
    # Write file 1
    with open(prompt_path, "w", encoding="utf-8") as f:
        f.write(prompt_content)
    # Write file 2
    with open(pydantic_path, "w", encoding="utf-8") as f:
        f.write(pydantic_content)
    # Write file 3 (using json.dump for proper formatting)
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(ground_truth_data, f, indent=4)

    print(f"✅ Files successfully generated for '{file_name}':")
    print(f"  - {prompt_path}")
    print(f"  - {pydantic_path}")
    print(f"  - {json_path}")
