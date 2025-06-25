from pydantic import BaseModel, Field

class APIResponse(BaseModel):

    message: str = Field(description="Response of the API call")