from collections.abc import Generator
from typing import Any

from dify_plugin.entities.tool import ToolInvokeMessage

from tools import monitor_base


class MonitorResumeTool(monitor_base.QueritMonitorTool):
    """Resume a paused monitor so it runs on schedule again."""

    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        monitor_id = tool_parameters.get("monitor_id")
        if not monitor_id:
            raise ValueError("monitor_id is required")
        yield from self._request("POST", f"/v1/monitors/{monitor_id}/resume")
