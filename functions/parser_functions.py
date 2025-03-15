# Imports
import logging, re
from jsonschema import validate, FormatChecker, ValidationError
from datetime import datetime

# Variables entorno/globales
UPSERT_ENTRY_SCHEMA = {
    "type": "object",
    "properties": {
        "user_id": {"type": "string"},
        "entry_date": { "type": "string"},
        "entry_id": {"type": "string"},
        "entry_content": {"type": "string"}
    },
    "required": ["user_id", "entry_date", "entry_id", "entry_content"],
    "additionalProperties": False
}

# Aux Functions
def validate_datetime(value):    
    if re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d{3})?Z$", value):
        return True
    else:
        return False

# Parser Functions
def parser_upsert_entry(headers, params, body):
    # Validate schema
    try:
        validate(instance=body, schema=UPSERT_ENTRY_SCHEMA)
    except ValidationError as e:
        logging.error(f"Invalid JSON for 'upsert_entry'")
        raise ValidationError(f"Invalid JSON")

    # Parse data
    user_id = body["user_id"]
    entry_date = body["entry_date"]
    entry_id = body["entry_id"]
    entry_content = body["entry_content"]

    # Check values
    if not validate_datetime(entry_date):
        logging.error(f"Invalid value for 'entry_date'")
        raise ValidationError(f"Invalid datetime value")
    
    # Return values
    return user_id, entry_date, entry_id, entry_content