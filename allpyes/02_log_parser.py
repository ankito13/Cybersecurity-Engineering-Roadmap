#!/usr/bin/env python3

log_file = "health_report.log"

try:
    # open the log file in read mode ("r")
    with open(log_file, "r") as file:
        lines = file.readlines()

    print(f"[*] succesfully opened {log_file}.")
    print(f"[*] total lines to scan: {len(lines)}\n")

    #Iterate through each line to find specific disk usage data
    for line in lines:
        if "G" in line: #Looking for gigabyte sizes from your df -h  output
            # .strip() remove invisible newline characters (\n)
            clean_line = line.strip()
            print(f"[MATCH] {clean_line}")

except FileNotFoundError:
    print(f"[ERROR] The file'{log_file}' was not fond.")
