"""
Division & Replication of Data for Optimal Performance & Security
Author: Preethi Dommaraju
"""

from partition import DataPartitioner
from replication import DataReplicator

def main():
    # Initialize partitioner and replicator
    partitioner = DataPartitioner(num_partitions=4)
    replicator = DataReplicator(replication_factor=3)

    # Sample dataset path
    dataset_path = "data/sample_dataset.csv"

    print("Starting Data Division & Replication Pipeline...")
    print("=" * 50)

    # Step 1: Partition data
    print("[1/3] Partitioning data...")
    partitions = partitioner.partition(dataset_path)
    print(f"✅ Data divided into {len(partitions)} partitions")

    # Step 2: Replicate partitions across nodes
    print("[2/3] Replicating partitions across nodes...")
    replication_status = replicator.replicate(partitions)
    print(f"✅ Partitions replicated with factor {replicator.replication_factor}")

    # Step 3: Validate replication
    print("[3/3] Validating replication...")
    is_valid = replicator.validate(replication_status)
    if is_valid:
        print("✅ Replication validated successfully!")
    else:
        print("❌ Replication validation failed!")

    print("=" * 50)
    print("Pipeline completed successfully!")

if __name__ == "__main__":
    main()
