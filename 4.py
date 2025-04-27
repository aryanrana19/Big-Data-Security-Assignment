import csv
import datetime

# Sample CSV data (normally this would be in a separate file)
sample_data = [
    ["UserID", "Name", "Email"],
    ["1", "Alice", "alice@example.com"],
    ["2", "Bob", "bob@example.com"],
    ["3", "Charlie", "charlie@example.com"]
]

# Create a sample CSV file
with open('sample_dataset.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(sample_data)

# Function to log access
def log_access(user_id, accessed_data):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('access_log.txt', 'a') as log_file:
        log_file.write(f"{timestamp} | UserID: {user_id} | Accessed Data: {accessed_data}\n")

# Function to simulate data access
def access_data(user_id, row_number):
    with open('sample_dataset.csv', 'r') as f:
        reader = list(csv.reader(f))
        if 0 <= row_number < len(reader):
            accessed_row = reader[row_number]
            print(f"User {user_id} accessed: {accessed_row}")
            log_access(user_id, accessed_row)
        else:
            print("Invalid row number!")

# Example simulation
access_data(user_id=101, row_number=1)  # User 101 accesses Alice's data
access_data(user_id=102, row_number=2)  # User 102 accesses Bob's data
access_data(user_id=103, row_number=3)  # User 103 accesses Charlie's data