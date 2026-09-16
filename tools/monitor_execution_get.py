from collections.abc import Generator
from typing import Any

from dify_plugin.entities.tool import ToolInvokeMessage

from tools.monitor_base import QueritMonitorTool


class MonitorExecutionGetTool(QueritMonitorTool):
    """Get the details of a single execution, including its result events."""

    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        monitor_id = tool_parameters.get("monitor_id")
        execution_id = tool_parameters.get("execution_id")
        if not monitor_id:
            raise ValueError("monitor_id is required")
        if not execution_id:
            raise ValueError("execution_id is required")
        yield from self._request(
            "GET", f"/v1/monitors/{monitor_id}/executions/{execution_id}"
        )
