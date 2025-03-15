# Imports
import azure.functions as func
import functions.parser_functions as pf

# Azure Functions
app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="af_upsert_entry", methods=["POST"])
def af_upsert_entry(req: func.HttpRequest) -> func.HttpResponse:
    """
    Crear o actualizar el contenido de una entrada.
    """
    # Parser request
    try:
        user_id, entry_date, entry_id, entry_content = pf.parser_upsert_entry(req.headers, req.params, req.get_json())
    except Exception as e:
        return func.HttpResponse(str(e), status_code=400)
    