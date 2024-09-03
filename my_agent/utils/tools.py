from langchain_core.tools import tool
# from langchain_community.tools.tavily_search import TavilySearchResults
import requests
notion_token = "secret_uEqMcm68e3DBveKpK6UmmiXYTAew9T2CrONOXINhKT9"
block_id = "7c397a7e-de7b-417c-835b-67524029a5cb"


@tool
def get_coolest_cities():
    """Get a list of coolest cities"""
    return "nyc, sf"

@tool
def create_a_notion_task(description: str):
    """Create a task in Notion"""
    """
    Add a to-do list item to a Notion block.
    
    Parameters:
    - block_id: The ID of the block where the to-do item will be added.
    - task_description: The text description of the task.
    - notion_token: Your Notion API integration token.
    """
    url = f"https://api.notion.com/v1/blocks/{block_id}/children"
    
    headers = {
        "Authorization": f"Bearer {notion_token}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"  # Use the latest Notion API version
    }
    
    data = {
        "children": [
            {
                "object": "block",
                "type": "to_do",
                "to_do": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": description
                            }
                        }
                    ]
                }
            }
        ]
    }
    
    response = requests.patch(url, headers=headers, json=data)
    
    if response.status_code == 200:
        return f"Created a task in Notion with \ndescription: {description}"
    else:
        return f"Failed to add to-do item. Status code: {response.status_code}"

tools = [get_coolest_cities, create_a_notion_task]