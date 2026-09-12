#!/bin/bash
LOG_FILE="health_report.log"
echo "checking system disk space.."
df -h >> $LOG_FILE
echo "check comlete! Data saved to $LOG_FILE."
