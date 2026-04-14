import os
import json
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.data_treatment import (
    clean_annotations,
    change_fieldtypes,
    normalize_pub,
    normalize_docile,
)

load_dotenv()

#################
# DOCILE DATASET
#################


def process_docile(json_path):

    clean = clean_annotations(json_path)
    processed_annotation = change_fieldtypes(clean)
    final_annotation = normalize_docile(processed_annotation)

    return final_annotation


########################
# PUB-TABLES 1M DATASET
########################


def process_pub(json_path):

    with open(json_path, "r") as f:
        data = json.load(f)
        final_annotation = normalize_pub(data)

    return final_annotation


####################
# FOR BOTH DATASETS
####################


def invoke_model(Dataset_Generation):

    llm_url = os.getenv("LLM_URL")
    llm_model = os.getenv("LLM_MODEL")
    api_key = os.getenv("API_KEY")
    llm_provider = os.getenv("LLM_PROVIDER")

    model = init_chat_model(
        model=llm_model,
        base_url=llm_url,
        api_key=api_key,
        temperature=0,
        timeout=60,
        max_retries=3,
        model_provider=llm_provider,
    )

    structured_model = model.with_structured_output(Dataset_Generation)

    return structured_model


def obtain_query(structured_model, processed_annotation):

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "Only answer the user's query. Do not introduce your answer, only answer what you have been asked",
            ),
            (
                "human",
                """Based on {processed_ground_truth}, which is a perfect parsed table, you must:
        1) Develop a query that would be relevant for a company (for example: retrieve all transactions of type 'X' and select from them fields 'Y' and 'Z', ensuring you do not select all available lines). You should not mention the fields from the {processed_ground_truth}, just make it in a conversational way.
        2) Then, build a pydantic model according to this query. It must be specific and have a description for each field. Then you should create a new pydantic model which elements are a list of the elements of the pydantic model created in 2). Values of "unit_price_gross" and "price_gross" must be a Decimal, not a string. Import necessary python dependencies. 
        3) Create the ground truth according to the query and the pydantic model created. The value of "unit_price_gross" and "price_gross" must be numbers, not strings""",
            ),
        ]
    )

    chain = prompt | structured_model

    response = chain.invoke(
        {"processed_ground_truth": json.dumps(processed_annotation)}
    )

    return response
