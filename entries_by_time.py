import re
import datetime


def extract_timestamps_and_messages(log_lines):
    """
    Extracts timestamps and associated messages from the log lines.

    Args:
        log_lines (list): List of strings representing the log lines.

    Returns:
        list: A list of tuples where each tuple contains a timestamp and the associated message.
    """
    extracted_data = []

    for line in log_lines:
        # Extract the timestamp and message
        # timestamp_match = re.search(r"<(.*?)\s\w{3}>", line)
        timestamp_match = re.search(r"time='(.*?)'", line)
        msg_match = re.search(r"'>\s*(.*?)\s*</Msg>", line)

        timestamp = timestamp_match.group(1) if timestamp_match else None
        message = msg_match.group(1) if msg_match else None

        if timestamp:
            timestamp_obj = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S,%f')
            extracted_data.append((timestamp_obj, message))

    return extracted_data


if __name__ == "__main__":
    log_file = r"T:\work\giss\monthly\202309sep\gallaga\attribute assistant\server_errors\TrafficStudy.MapServer-20230915.115412-14892-16404.0.log"

    # Re-reading the log contents
    with open(log_file, "r") as file:
        traffic_study_log_contents = file.readlines()

    timestamps_and_messages = extract_timestamps_and_messages(traffic_study_log_contents)

    # Calculate the time differences between consecutive log entries
    time_differences = []

    for i in range(1, len(timestamps_and_messages)):
        diff = timestamps_and_messages[i][0] - timestamps_and_messages[i - 1][0]
        time_differences.append((diff, timestamps_and_messages[i - 1][1], timestamps_and_messages[i][1]))

    # Sort the time differences in descending order
    sorted_time_differences = sorted(time_differences, key=lambda x: x[0], reverse=True)

    # Display the top 5 processes with the most time taken
    top_processes = sorted_time_differences[:10]

    for process in top_processes:
        print(top_processes)
