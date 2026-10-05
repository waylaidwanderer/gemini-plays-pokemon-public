import sys
from mgba import _send_request


def _call_tool(name, args=None):
    res = _send_request("/api/tool", {"name": name, "args": args or {}})
    if isinstance(res, dict):
        if "result" in res:
            return res["result"]
        if "error" in res:
            return f"Error: {res['error']}"
    return res


def output(data):
    """
    Sends arbitrary structured data back to the harness.
    Objects containing an "image" key with a relative sandbox path
    will have their visual images automatically loaded into the agent's turn context.
    """
    return _send_request("/api/output", {"data": data})


def press_buttons(buttons, num_turns=None, current_position=None):
    if isinstance(buttons, str):
        buttons = [buttons]
    args = {"buttons": list(buttons)}
    if num_turns is not None:
        args["num_turns"] = num_turns
    if current_position is not None:
        args["current_position"] = current_position
    return _call_tool("press_buttons", args)


def speak(message, expression="neutral", num_turns=None, current_position=None):
    args = {"message": message, "expression": expression}
    if num_turns is not None:
        args["num_turns"] = num_turns
    if current_position is not None:
        args["current_position"] = current_position
    return _call_tool("speak", args)


def update_objectives(
    primary_goal=None,
    secondary_goal=None,
    tertiary_goal=None,
    navigation_goal=None,
):
    args = {}
    if primary_goal is not None:
        args["primary_goal"] = primary_goal
    if secondary_goal is not None:
        args["secondary_goal"] = secondary_goal
    if tertiary_goal is not None:
        args["tertiary_goal"] = tertiary_goal
    if navigation_goal is not None:
        args["navigation_goal"] = navigation_goal
    return _call_tool("update_objectives", args)


def crop(x, y, width, height, label=None):
    args = {"x": x, "y": y, "width": width, "height": height}
    if label is not None:
        args["label"] = label
    return _call_tool("crop", args)


def read_notepad(path):
    return _call_tool("read_notepad", {"path": path})


def load_notepads(paths):
    if isinstance(paths, str):
        paths = [paths]
    return _call_tool("load_notepads", {"paths": list(paths)})


def unload_notepads(paths):
    if isinstance(paths, str):
        paths = [paths]
    return _call_tool("unload_notepads", {"paths": list(paths)})


def search_notepads(query, search_type="fuzzy"):
    return _call_tool("search_notepads", {"query": query, "search_type": search_type})


def notepad_edit(action, old_text="", new_text="", expected_count=None, path="Main"):
    args = {
        "action": action,
        "old_text": old_text,
        "new_text": new_text,
        "path": path,
    }
    if expected_count is not None:
        args["expected_count"] = expected_count
    return _call_tool("notepad_edit", args)


def delete_notepad(path):
    return _call_tool("delete_notepad", {"path": path})


def read_file(path):
    return _call_tool("read_file", {"path": path})


def write_file(path, content):
    return _call_tool("write_file", {"path": path, "content": content})


def edit_file(path, old_text, new_text):
    return _call_tool(
        "edit_file",
        {"path": path, "old_text": old_text, "new_text": new_text},
    )


def delete_file(path):
    return _call_tool("delete_file", {"path": path})


def define_agent(agent_name, agent_description, agent_system_prompt):
    return _call_tool(
        "define_agent",
        {
            "agent_name": agent_name,
            "agent_description": agent_description,
            "agent_system_prompt": agent_system_prompt,
        },
    )


def delete_agent(agent_name):
    return _call_tool("delete_agent", {"agent_name": agent_name})


def invoke_subagent(
    agent_name,
    instructions,
    agent_description=None,
    agent_system_prompt=None,
    abort_if=None,
    max_turns=None,
    save=None,
):
    args = {
        "agent_name": agent_name,
        "instructions": instructions,
    }
    if agent_description is not None:
        args["agent_description"] = agent_description
    if agent_system_prompt is not None:
        args["agent_system_prompt"] = agent_system_prompt
    if abort_if is not None:
        args["abort_if"] = abort_if
    if max_turns is not None:
        args["max_turns"] = max_turns
    if save is not None:
        args["save"] = save
    return _call_tool("invoke_subagent", args)


def report_outcome(summary):
    return _call_tool("report_outcome", {"summary": summary})


def new_context(summary):
    return _call_tool("new_context", {"summary": summary})


def stun_npc(effect="stun"):
    return _call_tool("stun_npc", {"effect": effect})


def call_tool(name, **kwargs):
    return _call_tool(name, kwargs)


try:
    import builtins
    builtins.output = output
    builtins.tools = sys.modules[__name__]
    builtins.mgba = sys.modules.get("mgba")
except Exception:
    pass
