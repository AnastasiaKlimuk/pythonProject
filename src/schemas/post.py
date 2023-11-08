POST_SCHEMA = {  ##JSON-Schema - задает структуру документа
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "title": {"type": "string"}
    },
    "required": ["id"]
}