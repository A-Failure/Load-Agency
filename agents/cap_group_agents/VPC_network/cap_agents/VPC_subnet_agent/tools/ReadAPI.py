
from agency_swarm.tools import BaseTool
from pydantic import Field
import os

class ReadAPI(BaseTool):


    def run(self):
        api =[
    {
        "api_name": "创建子网",
        "introduction": "用于创建子网。"
    },
    {
        "api_name": "查询子网",
        "introduction": "用于查询子网。"
    },
    {
        "api_name": "查询子网列表",
        "introduction": "用于查询子网列表。"
    },
    {
        "api_name": "更新子网",
        "introduction": "用于更新子网。"
    },
    {
        "api_name": "删除子网",
        "introduction": "用于删除子网。"
    }
]
        return api