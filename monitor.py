import psutil
import time
import signal
from datetime import datetime

loads = []


def signal_handler(sig, frame):
    print("Process killed by signal:", sig)
    # Dynamic filename to avoid overwriting
    filename = f"/home/farjad/Desktop/temp_acmse/cpu_time_cnn_results.csv"
    with open(filename, "w") as f:
        f.write("time_stamp,cpu_percent\n")
        for row in loads:
            f.write(f"{row[0]},{row[1]}\n")
    loads.clear()  # Clear the list after writing to the file

def is_valid_timestamp(timestamp):
    try:
        datetime.strptime(timestamp, "%H:%M:%S.%f")
        return True
    except ValueError:
        return False

def main():
    signal.signal(signal.SIGTERM, signal_handler)

    try:
        while True:
            now = datetime.now()
            sampling_time = now.strftime("%H:%M:%S.%f")[:-3]
            cpu_percent = psutil.cpu_percent(interval=1)

            if is_valid_timestamp(sampling_time):
                loads.append((sampling_time, cpu_percent))
                last_timestamp = sampling_time

    except KeyboardInterrupt:
        print("Process interrupted by keyboard")

    except Exception as e:
        print("Unexpected error:", e)

    finally:
        signal_handler(None, None)

if __name__ == "__main__":
    main()
