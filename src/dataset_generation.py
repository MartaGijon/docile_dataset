import os
from docile_pub_generation_functions import (
    invoke_model,
    process_docile,
    process_pub,
    obtain_query,
)
from src.pydantic_schemas import Dataset_Generation
from save_llm_response import save_llm_output

DOCILE_PATH = "data/docile/annotations"
PUB_PATH = "data/pub/annotations"


def process_data():

    structured_model = invoke_model(Dataset_Generation)

    for PATH in [DOCILE_PATH, PUB_PATH]:
        if PATH == DOCILE_PATH:
            print("PROCESSING DOCILE ANNOTATIONS")

            data_type = "docile"
            n = 0
            for filename in os.listdir(PATH):
                print(f"PROCESSING ANNOTATION NUMBER {n + 1}")

                if filename.endswith(".json"):
                    name_without_extension = filename.replace(".json", "")
                    print(f"Processing {filename}")
                    json_path = os.path.join(PATH, filename)

                    processed_annotation = process_docile(json_path)

                    response = obtain_query(structured_model, processed_annotation)
                    save_llm_output(response, name_without_extension, data_type)

                    n += 1

        elif PATH == PUB_PATH:
            print("PROCESSING PUB-TABLES 1M ANNOTATIONS")

            data_type = "pub"
            n = 0
            for filename in os.listdir(PATH):
                print(f"PROCESSING ANNOTATION NUMBER {n + 1}")

                if filename.endswith(".json"):
                    name_without_extension = filename.replace(".json", "")
                    print(f"Processing {filename}")
                    json_path = os.path.join(PATH, filename)

                    processed_annotation = process_pub(json_path)

                    response = obtain_query(structured_model, processed_annotation)
                    save_llm_output(response, name_without_extension, data_type)

                    n += 1

    print("GENERATION PROCESS HAS FINISHED SUCCESSFULLY")


if __name__ == "__main__":
    process_data()
