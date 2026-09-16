from collections.abc import Generator
from typing import Any

from dify_plugin.entities.tool import ToolInvokeMessage

from tools.monitor_base import QueritMonitorTool


class MonitorUpdateTool(QueritMonitorTool):
    """Update a monitor. At least one of name / period / query must be provided.

    Note: ``search`` is replaced as a whole object by the API, not merged. When
    ``query`` is provided this tool rebuilds the whole search object, so include
    ``count`` again if you want to keep it.
    """

    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        monitor_id = tool_parameters.get("monitor_id")
        if not monitor_id:
            raise ValueError("monitor_id is required")

        body: dict[str, Any] = {}
        if tool_parameters.get("name"):
            body["name"] = tool_parameters["name"]
        if tool_parameters.get("period"):
            body["schedule"] = {"type": "interval", "period": tool_parameters["period"]}
        if tool_parameters.get("query"):
            search: dict[str, Any] = {"query": tool_parameters["query"]}
            count = tool_parameters.get("count")
            if count is not None:
                search["count"] = int(count)
            body["search"] = search

        if not body:
            raise ValueError("Provide at least one of name / period / query to update")

        yield from self._request("POST", f"/v1/monitors/{monitor_id}", json_body=body)
