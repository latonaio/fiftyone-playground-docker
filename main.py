#!/usr/bin/env python3
from pip import main
import fiftyone as fo


# The directory containing the source images
data_path = "dataset/export/cats-all/images"
# The path to the labels dir
labels_path ="dataset/export/cats-all/labels"
# The type of the dataset being imported
dataset_type = fo.types.KITTIDetectionDataset  # for example


# def LaunchApp():

#     session = fo.launch_app(dataset)
#     session.wait()


def LaunchApp():
    # Import the dataset
    dataset = fo.Dataset.from_dir(
        dataset_type=dataset_type,
        data_path=data_path,
        labels_path=labels_path,
        # max_samples=2000,
    )
#     dataset = fo.zoo.load_zoo_dataset(
#         "open-images-v6",
#         split="validation",
#         label_types=["detections", "segmentations"],
#         classes=["Cat"],
#         max_samples=300,
#     )

    session = fo.launch_app(
        dataset=dataset,
        address="0.0.0.0",
        port=5678,
        )
    session.wait()

def analysis():
    # The directory containing the source images
    data_path = "dataset/import/all/images"
    # The path to the COCO labels JSON file
    labels_path ="dataset/import/all/labels"
    # The type of the dataset being imported
    dataset_type = fo.types.VOCDetectionDataset  # for example


    # Import the dataset
    dataset = fo.Dataset.from_dir(
        dataset_type=dataset_type,
        data_path=data_path,
        labels_path=labels_path,
        # max_samples=100,
    )

    export_dir="dataset/export/cats-all"
    export_dataset_type=fo.types.KITTIDetectionDataset

    dataset.export(
        export_dir=export_dir,
        dataset_type=export_dataset_type,
        data_path="images",
        labels_path="labels",
        label_field="ground_truth",
    )





# def main():
#     dataset = fo.zoo.load_zoo_dataset(
#         split="validation",
#         label_types=["detections", "segmentations"],
#         classes=["Cat"],
#         max_samples=300,
#     )
#     session = fo.launch_app(dataset)
#     session.wait()

def convert():
    # The directory containing the source images
    data_path = "../dataset/images"

    # The path to the COCO labels JSON file
    labels_path = "../dataset/annotations/xmls"
    # The type of the dataset being imported
    dataset_type = fo.types.VOCDetectionDataset  # for example

    # Import the dataset
    dataset = fo.Dataset.from_dir(
        dataset_type=dataset_type,
        data_path=data_path,
        labels_path=labels_path,
        max_samples=10000,
    )

    export_dir="../dataset/export"
    export_dataset_type=fo.types.KITTIDetectionDataset

    dataset.export(
        export_dir=export_dir,
        dataset_type=export_dataset_type,
        labels_path="../dataset/export/labels",
        label_field="ground_truth",
    )



    # session = fo.launch_app(dataset)
    # session.wait()



if __name__ == "__main__":
    LaunchApp()