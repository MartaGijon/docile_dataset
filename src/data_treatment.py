import json


# ---------------------------------------------
# DOCILE DATASET
# ---------------------------------------------


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


def change_fieldtypes(clean_annotation):
    extractions = []

    mapping = {
        "line_item_date": "date",
        "line_item_quantity": "quantity",
        "line_item_amount_gross": "price_gross",
        "line_item_unit_price_gross": "unit_price_gross",
        "line_item_position": "position",
        "line_item_code": "code",
        "line_item_description": "description",
        "line_item_currency": "currency",
        "line_item_amount_net": "amount_net",
        "line_item_unit_price_net": "unit_price_net",
    }

    for element in clean_annotation["extractions"]:
        fieldtype = element.get("fieldtype")
        text = element.get("text")

        if fieldtype in mapping:
            extractions.append({"fieldtype": mapping[fieldtype], "text": text})

    return extractions


def normalize_docile(clean_processed):
    """
    Normaliza el texto basándose en el valor de 'fieldtype'.
    """
    for item in clean_processed:
        # Obtenemos el tipo de campo y el texto de forma segura
        fieldtype = item.get("fieldtype")
        text_value = item.get("text")
        # Nos aseguramos de que haya texto para evitar errores
        if isinstance(text_value, str):
            # 1. Limpieza si es una descripción
            if fieldtype == "description":
                text_without_escapes = text_value.replace("\n", " ")
                item["text"] = " ".join(text_without_escapes.split())
            # 2. Limpieza si es una fecha
            elif (
                fieldtype == "date"
                or fieldtype == "transaction_date"
                or fieldtype == "start_date"
                or fieldtype == "end_date"
            ):
                item["text"] = text_value.replace("\u2013", "/").replace("-", "/")
    return clean_processed


def limpiar_docile(texto):
    """Aplica las reglas de limpieza a un texto individual."""
    if not isinstance(texto, str):
        return texto
    # Quitar las dobles barras si las hubiera
    limpio = texto.replace("-", "/")
    # Planchar cualquier salto de línea (\n, \r) y espacios múltiples

    return limpio


# --- 2. El explorador ciego (Recursividad) ---
def recorrer_y_limpiar_docile(datos):
    """Viaja por todo el JSON buscando strings para limpiarlos, sin importar las claves."""
    # CASO A: Es un diccionario -> miramos todas sus claves y valores
    if isinstance(datos, dict):
        for clave, valor in datos.items():
            # Volvemos a llamar a la función para cada valor
            datos[clave] = recorrer_y_limpiar_docile(valor)
    # CASO B: Es una lista -> miramos todos sus elementos
    elif isinstance(datos, list):
        for i in range(len(datos)):
            # Volvemos a llamar a la función para cada elemento
            datos[i] = recorrer_y_limpiar_docile(datos[i])
    # CASO C: Hemos llegado al fondo de la caja y es un texto -> ¡Lo limpiamos!
    elif isinstance(datos, str):
        return limpiar_docile(datos)
    # CASO D: Es un número, booleano, nulo, etc -> Lo devolvemos sin tocar
    return datos


# --- 3. La función principal (La puerta de entrada) ---
def normalize_docile_post(data):
    """Asegura que los datos estén bien formateados antes de soltar al explorador."""
    if isinstance(data, str):
        try:
            data = json.loads(data)
        except json.JSONDecodeError:
            pass  # Si es un string normal (no un JSON), seguimos adelante

    return recorrer_y_limpiar_docile(data)


################
# PUB-TABLES 1M
################


def limpiar_texto(texto):
    """Aplica las reglas de limpieza a un texto individual."""
    if not isinstance(texto, str):
        return texto
    # Quitar las dobles barras si las hubiera
    limpio = texto.replace("\\n", " ")
    # Planchar cualquier salto de línea (\n, \r) y espacios múltiples
    limpio = " ".join(limpio.split())
    # Sustituir guiones y símbolos especiales
    limpio = (
        limpio.replace("\u2013", "-").replace("\u2664", "<=").replace("\u2665", ">=")
    )
    return limpio


# --- 2. El explorador ciego (Recursividad) ---
def recorrer_y_limpiar(datos):
    """Viaja por todo el JSON buscando strings para limpiarlos, sin importar las claves."""
    # CASO A: Es un diccionario -> miramos todas sus claves y valores
    if isinstance(datos, dict):
        for clave, valor in datos.items():
            # Volvemos a llamar a la función para cada valor
            datos[clave] = recorrer_y_limpiar(valor)
    # CASO B: Es una lista -> miramos todos sus elementos
    elif isinstance(datos, list):
        for i in range(len(datos)):
            # Volvemos a llamar a la función para cada elemento
            datos[i] = recorrer_y_limpiar(datos[i])
    # CASO C: Hemos llegado al fondo de la caja y es un texto -> ¡Lo limpiamos!
    elif isinstance(datos, str):
        return limpiar_texto(datos)
    # CASO D: Es un número, booleano, nulo, etc -> Lo devolvemos sin tocar
    return datos


# --- 3. La función principal (La puerta de entrada) ---
def normalize_pub(data):
    """Asegura que los datos estén bien formateados antes de soltar al explorador."""
    if isinstance(data, str):
        try:
            data = json.loads(data)
        except json.JSONDecodeError:
            pass  # Si es un string normal (no un JSON), seguimos adelante

    return recorrer_y_limpiar(data)
