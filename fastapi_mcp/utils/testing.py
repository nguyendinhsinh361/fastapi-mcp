import json
from typing import Any, Dict, Optional

from fastapi import FastAPI
from fastapi.testclient import TestClient

from fastapi_mcp.server import AsyncClientProtocol


class FastAPITestClient(AsyncClientProtocol):
    def __init__(self, app: FastAPI):
        self.client = TestClient(app, raise_server_exceptions=False)

    async def get(
        self, url: str, *, params: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None
    ) -> Any:
        response = self.client.get(url, params=params, headers=headers)
        return self._wrap_response(response)

    async def post(
        self,
        url: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        json: Optional[Any] = None,
    ) -> Any:
        response = self.client.post(url, params=params, headers=headers, json=json)
        return self._wrap_response(response)

    async def put(
        self,
        url: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        json: Optional[Any] = None,
    ) -> Any:
        response = self.client.put(url, params=params, headers=headers, json=json)
        return self._wrap_response(response)

    async def delete(
        self, url: str, *, params: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None
    ) -> Any:
        response = self.client.delete(url, params=params, headers=headers)
        return self._wrap_response(response)

    async def patch(
        self,
        url: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        json: Optional[Any] = None,
    ) -> Any:
        response = self.client.patch(url, params=params, headers=headers, json=json)
        return self._wrap_response(response)

    def _wrap_response(self, response: Any) -> Any:
        response.json = (
            lambda: json.loads(response.content) if hasattr(response, "content") and response.content else None
        )
        return response
