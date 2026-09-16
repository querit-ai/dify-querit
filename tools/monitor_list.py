from collections.abc import Generator
from typing import Any

from dify_plugin.entities.tool import ToolInvokeMessage

from tools import monitor_base


class MonitorListTool(monitor_base.QueritMonitorTool):
    """List monitors with optional status / name filters and pagination."""

    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        params = {
            "status": tool_parameters.get("status"),
            "name": tool_parameters.get("name"),
            "page": tool_parameters.get("page"),
            "page_size": tool_parameters.get("page_size"),
        }
        yield from self._request("GET", "/v1/monitors", params=params)
