"""
Data Partitioning Module
Handles splitting large datasets into optimized fragments using Apache Spark
Author: Preethi Dommaraju
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DataPartitioner:
    def __init__(self, num_partitions=4):
        self.num_partitions = num_partitions
        self.spark = SparkSession.builder \
            .appName("DataPartitioner") \
            .config("spark.executor.memory", "4g") \
            .getOrCreate()

    def partition(self, dataset_path):
        """
        Partition large dataset into fragments for distributed processing
        """
        logger.info(f"Loading dataset from: {dataset_path}")
        df = self.spark.read.csv(dataset_path, header=True, inferSchema=True)

        logger.info(f"Total records: {df.count()}")
        logger.info(f"Partitioning into {self.num_partitions} fragments...")

        # Repartition data
        partitioned_df = df.repartition(self.num_partitions)

        # Save partitions
        partitions = []
        for i in range(self.num_partitions):
            partition_path = f"output/partition_{i}"
            partitioned_df.write.parquet(partition_path, mode="overwrite")
            partitions.append(partition_path)
            logger.info(f"Partition {i} saved to: {partition_path}")

        return partitions

    def validate_partitions(self, partitions):
        """
        Validate all partitions are correctly created
        """
        for partition in partitions:
            df = self.spark.read.parquet(partition)
            if df.count() == 0:
                logger.error(f"Empty partition found: {partition}")
                return False
        logger.info("All partitions validated successfully!")
        return True

    def get_partition_stats(self, partitions):
        """
        Get statistics for each partition
        """
        stats = []
        for i, partition in enumerate(partitions):
            df = self.spark.read.parquet(partition)
            stats.append({
                "partition_id": i,
                "record_count": df.count(),
                "path": partition
            })
        return stats
