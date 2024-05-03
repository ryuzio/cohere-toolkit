from enum import StrEnum

from community.tools import Category, ManagedTool
from community.tools.function_tools import (
    GeoNamesFunctionTool,
    WolframAlphaFunctionTool,
)
from community.tools.retrieval import (
    ArxivRetriever,
    ConnectorRetriever,
    LlamaIndexUploadPDFRetriever,
    PubMedRetriever,
)


class CommunityToolName(StrEnum):
    Arxiv = "Arxiv"
    Connector = "Connector"
    Pub_Med = "Pub Med"
    File_Upload_LlamaIndex = "File Reader - LlamaIndex"
    Wolfram_Alpha = "Wolfram_Alpha"
    GeoNames = "GeoNames"


COMMUNITY_TOOLS = {
    CommunityToolName.Arxiv: ManagedTool(
        name=CommunityToolName.Arxiv,
        implementation=ArxivRetriever,
        is_visible=True,
        is_available=ArxivRetriever.is_available(),
        error_message="ArxivRetriever is not available.",
        category=Category.DataLoader,
        description="Retrieves documents from Arxiv.",
    ),
    CommunityToolName.Connector: ManagedTool(
        name=CommunityToolName.Connector,
        implementation=ConnectorRetriever,
        is_visible=True,
        is_available=ConnectorRetriever.is_available(),
        error_message="ConnectorRetriever is not available.",
        category=Category.DataLoader,
        description="Connects to a data source.",
    ),
    CommunityToolName.Pub_Med: ManagedTool(
        name=CommunityToolName.Pub_Med,
        implementation=PubMedRetriever,
        is_visible=True,
        is_available=PubMedRetriever.is_available(),
        error_message="PubMedRetriever is not available.",
        category=Category.DataLoader,
        description="Retrieves documents from Pub Med.",
    ),
    CommunityToolName.File_Upload_LlamaIndex: ManagedTool(
        name=CommunityToolName.File_Upload_LlamaIndex,
        implementation=LlamaIndexUploadPDFRetriever,
        is_visible=True,
        is_available=LlamaIndexUploadPDFRetriever.is_available(),
        error_message="LlamaIndexUploadPDFRetriever is not available.",
        category=Category.FileLoader,
        description="Retrieves documents from a file using LlamaIndex.",
    ),
    CommunityToolName.Wolfram_Alpha: ManagedTool(
        name=CommunityToolName.Wolfram_Alpha,
        implementation=WolframAlphaFunctionTool,
        is_visible=False,
        is_available=WolframAlphaFunctionTool.is_available(),
        error_message="WolframAlphaFunctionTool is not available, please set the WOLFRAM_APP_ID environment variable.",
        category=Category.Function,
        description="Evaluate arithmetic expressions.",
    ),
    CommunityToolName.GeoNames: ManagedTool(
        name=CommunityToolName.GeoNames,
        implementation=GeoNamesFunctionTool,
        parameter_definitions={
            "name": {
                "description": "Name of the place to query",
                "type": "str",
                "required": True,
            },
            "country": {
                "description": "Country of the place for qeury context",
                "type": "str",
                "required": False,
            },
        },
        is_visible=True,
        is_available=GeoNamesFunctionTool.is_available(),
        error_message="GeoNamesFunctionTool is not available, please set the GEONAMES_USERNAME environment variable.",
        category=Category.Function,
        description="Query GeoNames.org for location information for a place.",
    ),
}

# For main.py cli setup script
COMMUNITY_TOOLS_SETUP = {
    CommunityToolName.Wolfram_Alpha: {
        "secrets": [
            "WOLFRAM_ALPHA_APP_ID",
        ],
    },
    CommunityToolName.GeoNames: {
        "secrets": [
            "GEONAMES_USERNAME",
        ],
    },
}
