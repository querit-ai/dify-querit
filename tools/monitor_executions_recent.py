from collections.abc import Generator
from typing import Any

from dify_plugin.entities.tool import ToolInvokeMessage

from tools.monitor_base import QueritMonitorTool


class MonitorExecutionsRecentTool(QueritMonitorTool):
    """Fetch the most recent executions together with their result content.

    This is the main endpoint for retrieving results; the new results of each
    execution are in ``events[].payload``.
    """

    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        monitor_id = tool_parameters.get("monitor_id")
        if not monitor_id:
            raise ValueError("monitor_id is required")
        params = {"limit": tool_parameters.get("limit")}
        yield from self._request(
            "GET", f"/v1/monitors/{monitor_id}/executions/recent", params=params
        )
