from collections.abc import Generator
from typing import Any

from dify_plugin.entities.tool import ToolInvokeMessage

from tools.monitor_base import QueritMonitorTool


class MonitorGetTool(QueritMonitorTool):
    """Get the full details of a single monitor, including its search config."""

    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        monitor_id = tool_parameters.get("monitor_id")
        if not monitor_id:
            raise ValueError("monitor_id is required")
        yield from self._request("GET", f"/v1/monitors/{monitor_id}")
