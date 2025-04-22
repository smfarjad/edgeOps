#!/bin/bash


function time_function() {
    # Start monitor.py in the background
    nohup python3 monitor.py &> /dev/null &
    program1_pid=$!
    echo "Monitoring started (PID: $program1_pid)"

    sleep 30
    local start_time=$(date +%s.%N)
    python3 inference.py >> mem_record_cnn-bb.txt # replace the filename acc to your preference
    local end_time=$(date +%s.%N)
    sleep 30

    # Kill monitor.py background process
    kill -TERM "$program1_pid"
    sleep 30

    csv_files=(*.csv)

    if [[ ${#csv_files[@]} -eq 0 ]]; then
        echo "No CSV files found in the current directory."
        exit 1
    fi

    # If multiple CSV files found, select the first one
    csv_file="${csv_files[0]}"

    # Create new folder if it doesn't exist
    mkdir -p new_folder

    # Create new CSV file name
    local start_time_str=$(date -d "@$start_time" +%Y-%m-%d_%H:%M:%S.%N)
    local end_time_str=$(date -d "@$end_time" +%Y-%m-%d_%H:%M:%S.%N)
    local new_name="${start_time_str}_to_${end_time_str}.csv"

    # Create the CSV file with headers
    mv "$csv_file" new_folder/"$new_name"

}

# Run the script for 10 times
for ((i=0; i<10; i++))
do
    time_function     
done
