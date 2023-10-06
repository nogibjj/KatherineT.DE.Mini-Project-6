"""handles cli commands"""
import sys
import argparse
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import (
    update_record,
    delete_record,
    create_record,
    general_query,
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
            "general_query",
            "read_data",
        ],
    )

    args = parser.parse_args(args[:1])
    print(args.action)
    
    if args.action == "update_record":
        parser.add_argument("year", type=int)
        parser.add_argument("month", type=int)
        parser.add_argument("date_of_month", type=int)
        parser.add_argument("day_of_week", type=int)
        parser.add_argument("births", type=int)

    if args.action == "create_record":
        parser.add_argument("year", type=int)
        parser.add_argument("month", type=int)
        parser.add_argument("date_of_month", type=int)
        parser.add_argument("day_of_week", type=int)
        parser.add_argument("birth", type=int)

    if args.action == "general_query":
        parser.add_argument("query")

    if args.action == "delete_record":
        parser.add_argument("record_id", type=int)

    # parse again with ever
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
        print(args)
        update_record(
            args.year,
            args.month,
            args.date_of_month,
            args.day_of_week,
            args.births,
            args.record_id,
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
    elif args.action == "general_query":
        general_query(args.query)
    elif args.action == "read_data":
        data = read_data()
        print(data)
    else:
        print(f"Unknown action: {args.action}")


if __name__ == "__main__":
    main()
