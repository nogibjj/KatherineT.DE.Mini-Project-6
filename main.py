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
        parser.add_argument("team")
        parser.add_argument("group")
        parser.add_argument("spi")
        parser.add_argument("global_o")
        parser.add_argument("global_d")
        parser.add_argument("sim_wins")

    if args.action == "create_record":
        parser.add_argument("group")
        parser.add_argument("spi")
        parser.add_argument("global_o")
        parser.add_argument("global_d")
        parser.add_argument("sim_wins")

    if args.action == "delete_record":
        parser.add_argument("team", type=TEXT)

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
            args.team,
            args.group,
            args.spi,
            args.global_o,
            args.global_d,
            args.sim_wins,
        )

    elif args.action == "delete_record":
        delete_record(args.team)

    elif args.action == "create_record":
        create_record(
            args.group,
            args.spi,
            args.global_o,
            args.global_d,
            args.sim_wins,
        )

    elif args.action == "read_data":
        data = read_data()
        print(data)

    else:
        print("Unknown action")


if __name__ == "__main__":
    main()
