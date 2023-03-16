def databaseResponseModel(status: bool, action: str, message: str):
    return {
            "status": status,
            "action": action,
            "message": message
        }