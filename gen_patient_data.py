#!/usr/bin/env python3

import csv
import datetime
import logging
import random
import sys


MINUTES_IN_TWO_DAYS = 2 * 24 * 60


logger = logging.getLogger(__name__)


def gen_patient_data():
    patients = [("1", "Jane"), ("2", "John")]
    now = datetime.datetime.utcnow().replace(second=0, microsecond=0)
    base_time = now - datetime.timedelta(minutes=MINUTES_IN_TWO_DAYS)
    for minute in range(MINUTES_IN_TWO_DAYS):
        event_time = base_time + datetime.timedelta(minutes=minute)
        event_time_iso8601 = f"{event_time.isoformat()}Z"
        for patient_id, patient_name in patients:
            yield (
                patient_id,
                patient_name,
                "HR",
                random.randint(60, 120),
                "beats/minute",
                event_time_iso8601
            )
            yield (
                patient_id,
                patient_name,
                "RR",
                random.randint(5, 20),
                "breaths/minute",
                event_time_iso8601
            )


def dump_patient_data(f, data):
    writer = csv.writer(f)
    writer.writerow(["PATIENT ID", "PATIENT NAME", "EVENT TYPE", "EVENT VALUE", "EVENT UNIT", "EVENT TIME"])
    writer.writerows(data)


def main():
    logging.basicConfig(level=logging.DEBUG)
    data = gen_patient_data()
    dump_patient_data(sys.stdout, data)


if __name__ == "__main__":
    main()
