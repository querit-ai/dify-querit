from collections.abc import Generator
from typing import Any

from dify_plugin.entities.tool import ToolInvokeMessage

from tools.monitor_base import QueritMonitorTool


class MonitorExecutionsTool(QueritMonitorTool):
    """List a monitor's execution records (metadata only, no search results)."""

    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        monitor_id = tool_parameters.get("monitor_id")
        if not monitor_id:
            raise ValueError("monitor_id is required")
        params = {
            "page": tool_parameters.get("page"),
            "page_size": tool_parameters.get("page_size"),
        }
        yield from self._request("GET", f"/v1/monitors/{monitor_id}/executions", params=params)
