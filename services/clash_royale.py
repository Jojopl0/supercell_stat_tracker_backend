import httpx
from typing import Optional
from app.utils.config import settings
from app.models.player import ClashRoyalePlayer

class ClashRoyaleService:
    def __init__(self):
        self.base_url = settings.CLASH_ROYALE_BASE_URL
        self.headers = {
            "Authorization": f"Bearer {settings.CLASH_ROYALE_API_KEY}",
            "Accept": "application/json"
        }
    
    async def get_player(self, player_tag: str) -> Optional[ClashRoyalePlayer]:
        """Fetch player data from Clash Royale API"""
        if not player_tag.startswith('#'):
            player_tag = f"#{player_tag}"
        
        # URL encode the # symbol
        encoded_tag = player_tag.replace('#', '%23')
        
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(
                    f"{self.base_url}/players/{encoded_tag}",
                    headers=self.headers,
                    timeout=10.0
                )
                response.raise_for_status()
                data = response.json()
                return ClashRoyalePlayer(**data)
            except httpx.HTTPStatusError as e:
                print(f"HTTP error occurred: {e}")
                return None
            except Exception as e:
                print(f"An error occurred: {e}")
                return None
    
    async def get_player_battles(self, player_tag: str, limit: int = 25):
        """Fetch recent battles for a player"""
        if not player_tag.startswith('#'):
            player_tag = f"#{player_tag}"
        
        encoded_tag = player_tag.replace('#', '%23')
        
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(
                    f"{self.base_url}/players/{encoded_tag}/battlelog",
                    headers=self.headers,
                    timeout=10.0
                )
                response.raise_for_status()
                return response.json()
            except Exception as e:
                print(f"Error fetching battles: {e}")
                return None