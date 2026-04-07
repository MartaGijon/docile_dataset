import json


def clean_annotations(json_path):
    """
    Clean annotations so only data from table and not data related to structure remain.
    """
    with open(json_path, "r") as f:
        d = json.load(f)

    clean_d = {"line_item_extractions": d.get("line_item_extractions", [])}

    line_items = clean_d.get("line_item_extractions", [])
    clean_annotation = [
        {"fieldtype": item.get("fieldtype"), "text": item.get("text")}
        for item in line_items
    ]

    return {"extractions": clean_annotation}


def change_fieltypes(clean_annotation):
    """
    Changes keys from clean annotations file, so "line_item_" is removed from keys.
    """
    extractions = []
    n = 0

    for element in clean_annotation["extractions"]:
        dicts = list(element.items())

        for element in dicts:
            if element[0] == "fieldtype":
                if element[1] == "line_item_date":
                    extractions.append({"fieldtype": "date"})
                elif element[1] == "line_item_quantity":
                    extractions.append({"fieldtype": "quantity"})
                elif element[1] == "line_item_amount_gross":
                    extractions.append({"fieldtype": "price_gross"})
                elif element[1] == "line_item_unit_price_gross":
                    extractions.append({"fieldtype": "unit_price_gross"})
                elif element[1] == "line_item_position":
                    extractions.append({"fieldtype": "position"})
                elif element[1] == "line_item_code":
                    extractions.append({"fieldtype": "code"})
            if element[0] == "text":
                extractions[n]["text"] = element[1]
        n += 1

    return extractions
