#!/usr/bin/env python3

import fiftyone as fo
import fiftyone.types as types
import json
import click
import time

# The env file
env_json = json.load(open('env.json'))
# The directory containing the source images
input_data_path = env_json["input"]["data_path"]
# The path to the labels dir
input_labels_path = env_json["input"]["labels_path"]
# The type of the dataset being imported
# for example
input_dataset_type = getattr(fo.types, env_json["input"]["dataset_type"])

unix_time = str(int(time.time()))
export_path = "/" + unix_time

export_data_path = env_json["export"]["data_path"] + export_path
export_labels_path = env_json["export"]["labels_path"]
export_label_field = env_json["export"]["label_field"]
export_dataset_type = getattr(fo.types, env_json["export"]["dataset_type"])

launch_app_address = str(env_json["launch_app"]["address"])
launch_app_port = int(env_json["launch_app"]["port"])


@click.group()
def command():
    pass


def launch_app():
    print("launch_app start")
    # Import the dataset
    dataset = fo.Dataset.from_dir(
        dataset_type=input_dataset_type,
        data_path=input_data_path,
        labels_path=input_labels_path,
        # max_samples=2000,
        name=unix_time,
    )
    session = fo.launch_app(
        dataset=dataset,
        address=launch_app_address,
        port=launch_app_port,
    )
    session.wait()
    print("launch_app end")


def convert_exec():
    print("dataset labels convert desired format")
    # Import the dataset
    dataset = fo.Dataset.from_dir(
        dataset_type=input_dataset_type,
        data_path=input_data_path,
        labels_path=input_labels_path,
        max_samples=10000,
        name=unix_time,
    )
    dataset.export(
        export_dir=export_data_path,
        dataset_type=export_dataset_type,
        labels_path=export_labels_path,
        label_field=export_label_field,
    )
    print("dataset labels converted")
    return dataset


@command.command(name="launch")
def launch():
    print("launch start")
    dataset = fo.Dataset.from_dir(
        dataset_type=input_dataset_type,
        data_path=input_data_path,
        labels_path=input_labels_path,
    )
    session = fo.launch_app(
        dataset=dataset,
        address=launch_app_address,
        port=launch_app_port,
    )
    session.wait()
    print("launch end")


@command.command(name="convert")
def convert():
    convert_exec()


if __name__ == "__main__":
    command()
    # launch()

