from arc_agi_babies.config.settings import settings

def wrap_success(result):
    return {
        "status": "success",
        "result": result,
    }

def wrap_error(error, process_name=""):
    if process_name == "":
        return {
            "status": "failed",
            "error": str(error),
        }
    else:
        return {
            "status": "failed",
            "error": f"An error occured during {process_name}: {str(error)}",
        }