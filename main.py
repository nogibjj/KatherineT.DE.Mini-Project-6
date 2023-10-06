"""
ETL-Query script
"""
import sys
import argparse
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import (
    update_record,
    delete_record,
    create_record,
    read_data,
)


def handle_arguments(args):
    """add action based on inital calls"""
    parser = argparse.ArgumentParser(description="ETL-Query script")
    parser.add_argument(
        "action",
        choices=[
            "extract",
            "transform_load",
            "update_record",
            "delete_record",
            "create_record",
            "read_data",
        ],
    )

    args = parser.parse_args(args[:1])
    print(args.action)

    if args.action == "update_record":
        parser.add_argument("record_id")
        parser.add_argument("year")
        parser.add_argument("month")
        parser.add_argument("date_of_month")
        parser.add_argument("day_of_week")
        parser.add_argument("births")

    if args.action == "create_record":
        parser.add_argument("year")
        parser.add_argument("month")
        parser.add_argument("date_of_month")
        parser.add_argument("day_of_week")
        parser.add_argument("births")

    if args.action == "delete_record":
        parser.add_argument("record_id", type=int)

    return parser.parse_args(sys.argv[1:])


def main():
    """handles all the cli commands"""
    args = handle_arguments(sys.argv[1:])

    if args.action == "extract":
        print("Extracting data...")
        extract()

    elif args.action == "transform_load":
        print("Transforming data...")
        load()

    elif args.action == "update_record":
        update_record(
            args.record_id,
            args.year,
            args.month,
            args.date_of_month,
            args.day_of_week,
            args.births,
        )

    elif args.action == "delete_record":
        delete_record(args.record_id)

    elif args.action == "create_record":
        create_record(
            args.year,
            args.month,
            args.date_of_month,
            args.day_of_week,
            args.births,
        )

    elif args.action == "read_data":
        data = read_data()
        print(data)

    else:
        print("Unknown action")


if __name__ == "__main__":
    main()
