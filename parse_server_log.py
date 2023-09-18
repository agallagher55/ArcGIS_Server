import re

from pprint import pprint


def parse_log(log_file):
    """
    Parses the provided log lines to extract message type, code, method, and message details.

    Args:
        log_lines (list): List of strings representing the log lines.

    Returns:
        dict: A dictionary structured by message type, with nested dictionaries for code, method, and message.
    """

    result = {}

    with open(log_file, "r") as lfile:
        log_lines = lfile.readlines()

    for line in log_lines:
        # Extract the message type (like 'INFO', 'DEBUG', etc.)
        type_match = re.search(r"type='(.*?)'", line)

        if not type_match:
            continue

        msg_type = type_match.group(1)

        # Extract code, method name, and the message
        code_match = re.search(r"code='(.*?)'", line)
        method_match = re.search(r"method='(.*?)'", line)
        msg_match = re.search(r"'>\s*(.*?)\s*</Msg>", line)
        target_match = re.search(r"target='(.*?)'", line)

        code = code_match.group(1) if code_match else None
        method = method_match.group(1) if method_match else None
        target = target_match.group(1) if target_match else None
        message = msg_match.group(1) if msg_match else None

        # Populate the dictionary
        if msg_type not in result:
            result[msg_type] = []

        result[msg_type].append({
            "code": code,
            "method": method,
            "message": message,
            "target": target,
        })

    return result


if __name__ == "__main__":
    # Test on the encroachment_log_contents
    files = [
        r"T:\work\giss\monthly\202309sep\gallaga\attribute assistant\server_errors\Encroachment.MapServer-20230915.121344-9676-28216.0.log",
    ]

    for logfile in files:
        parsed_log_data = parse_log(logfile)
        pprint(parsed_log_data)
