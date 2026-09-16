from collections.abc import Generator
from typing import Any, Optional
import json

import requests

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

BASE_URL = "https://api.querit.ai"


class QueritMonitorTool(Tool):
    """Base class shared by all Querit Monitor tools.

    Provides a single HTTP helper that handles authentication, request
    dispatch and consistent error reporting so each concrete tool only needs
    to assemble its parameters and delegate to ``_request``.
    """

    def _request(
        self,
        method: str,
        path: str,
        params: Optional[dict[str, Any]] = None,
        json_body: Optional[dict[str, Any]] = None,
    ) -> Generator[ToolInvokeMessage, None, None]:
        """Call the Querit Monitor API and yield the response.

        Args:
            method: HTTP method, one of GET / POST / DELETE.
            path: Path relative to the API base URL, e.g. ``/v1/monitors``.
            params: Optional query-string parameters; empty values are dropped.
            json_body: Optional JSON request body.
        """
        api_key = self.runtime.credentials.get("querit_api_key")
        if not api_key:
            raise ValueError("Querit API key is not configured~")

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }
        clean_params = {k: v for k, v in (params or {}).items() if v not in (None, "")}

        try:
            response = requests.request(
                method,
                f"{BASE_URL}{path}",
                headers=headers,
                params=clean_params or None,
                json=json_body,
                timeout=120,
            )
            response.raise_for_status()
            data = response.json()
            yield self.create_json_message(data)
            yield self.create_text_message(json.dumps(data, ensure_ascii=False))
        except requests.RequestException as e:
            error_message = f"Error when calling Querit Monitor API: {str(e)}"
            response = getattr(e, "response", None)
            if response is not None:
                error_message += f" - Status code: {response.status_code}"
                error_message += f" - Response: {response.text}"
            yield self.create_json_message({"status": "error", "error": error_message})
            yield self.create_text_message(f"Error: {error_message}")
        except Exception as e:
            error_message = f"Error: {str(e)}"
            yield self.create_json_message({"status": "error", "error": error_message})
            yield self.create_text_message(f"Error: {error_message}")
