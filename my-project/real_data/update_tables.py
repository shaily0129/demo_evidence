# import requests
# import duckdb
# from datetime import date
# import argparse

# API_URL = 'http://100.25.26.186:8002/tools/holiday/book'

# def fetch_and_update_data(request_data):
#     response = requests.post(API_URL, json=request_data)
#     if response.status_code == 200:
#         data = response.json()
#         if data['complete']:
#             conn = duckdb.connect('my-project/sources/new_booking/holiday_bookings.db')
#             conn.execute('''
#                 INSERT INTO bookings (request_id, name, country, age, insurance, booking_id, date)
#                 VALUES (?, ?, ?, ?, ?, ?, ?)
#             ''', (
#                 data['request_id'],
#                 data['params']['name'],
#                 data['params']['country'],
#                 int(data['params']['age']),
#                 data['params']['insurance'] == 'true',
#                 data['booking_id'],
#                 date.today()
#             ))
#             conn.close()

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="Update DuckDB with booking data from API")
#     parser.add_argument('--request_id', required=True, help="Request ID")
#     parser.add_argument('--name', required=True, help="Name")
#     parser.add_argument('--country', required=True, help="Country")
#     parser.add_argument('--age', required=True, help="Age")
#     parser.add_argument('--insurance', required=True, help="Insurance")

#     args = parser.parse_args()

#     request_data = {
#         "request_id": args.request_id,
#         "params": {
#             "name": args.name,
#             "country": args.country,
#             "age": args.age,
#             "insurance": args.insurance
#         }
#     }
#     fetch_and_update_data(request_data)

import requests
import duckdb
from datetime import date
import argparse
import subprocess

API_URL = "http://100.25.26.186:8002/tools/holiday/book"


def fetch_and_update_data(request_data):
    response = requests.post(API_URL, json=request_data)
    if response.status_code == 200:
        data = response.json()
        if data["complete"]:
            conn = duckdb.connect("my-project/sources/new_booking/holiday_bookings.db")
            conn.execute(
                """
                INSERT INTO bookings (request_id, name, country, age, insurance, booking_id, date)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
                (
                    data["request_id"],
                    data["params"]["name"],
                    data["params"]["country"],
                    int(data["params"]["age"]),
                    data["params"]["insurance"] == "true",
                    data["booking_id"],
                    date.today(),
                ),
            )
            conn.close()
            update_evidence()


def update_evidence():
    subprocess.run(
        ["npm", "run", "sources"], cwd="/Users/shailygoyal/Desktop/demo_evidence/my-project"
    )
    subprocess.run(
        ["npm", "run", "dev"],
        cwd="/Users/shailygoyal/Desktop/demo_evidence/my-project",
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Update DuckDB with booking data from API"
    )
    parser.add_argument("--request_id", required=True, help="Request ID")
    parser.add_argument("--name", required=True, help="Name")
    parser.add_argument("--country", required=True, help="Country")
    parser.add_argument("--age", required=True, help="Age")
    parser.add_argument("--insurance", required=True, help="Insurance")

    args = parser.parse_args()

    request_data = {
        "request_id": args.request_id,
        "params": {
            "name": args.name,
            "country": args.country,
            "age": args.age,
            "insurance": args.insurance,
        },
    }
    fetch_and_update_data(request_data)
