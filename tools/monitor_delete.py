from collections.abc import Generator
from typing import Any

from dify_plugin.entities.tool import ToolInvokeMessage

from tools import monitor_base


class MonitorDeleteTool(monitor_base.QueritMonitorTool):
    """Delete a monitor."""

    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        monitor_id = tool_parameters.get("monitor_id")
        if not monitor_id:
            raise ValueError("monitor_id is required")
        yield from self._request("DELETE", f"/v1/monitors/{monitor_id}")
