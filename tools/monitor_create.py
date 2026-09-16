from collections.abc import Generator
from typing import Any

from dify_plugin.entities.tool import ToolInvokeMessage

from tools import monitor_base


class MonitorCreateTool(monitor_base.QueritMonitorTool):
    """Create a scheduled search monitor."""

    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        name = tool_parameters.get("name")
        query = tool_parameters.get("query")
        period = tool_parameters.get("period")
        if not name:
            raise ValueError("name is required")
        if not query:
            raise ValueError("query is required")
        if not period:
            raise ValueError("period is required")

        search: dict[str, Any] = {"query": query}
        count = tool_parameters.get("count")
        if count is not None:
            search["count"] = int(count)
        if tool_parameters.get("need_content"):
            search["needContent"] = True

        body = {
            "name": name,
            "schedule": {"type": "interval", "period": period},
            "search": search,
        }
        yield from self._request("POST", "/v1/monitors", json_body=body)
