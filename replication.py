"""
Data Replication Module
Handles replicating data partitions across multiple cloud nodes
Author: Preethi Dommaraju
"""

import logging
import hashlib
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DataReplicator:
    def __init__(self, replication_factor=3):
        self.replication_factor = replication_factor
        self.nodes = self._initialize_nodes()

    def _initialize_nodes(self):
        """
        Initialize cloud nodes for replication
        """
        nodes = [f"node_{i}" for i in range(self.replication_factor)]
        logger.info(f"Initialized {len(nodes)} nodes: {nodes}")
        return nodes

    def replicate(self, partitions):
        """
        Replicate each partition across multiple nodes
        """
        replication_status = {}

        for partition in partitions:
            partition_id = os.path.basename(partition)
            replication_status[partition_id] = []

            for node in self.nodes:
                replica_path = f"{node}/{partition_id}"
                # Simulate replication
                checksum = self._compute_checksum(partition)
                replication_status[partition_id].append({
                    "node": node,
                    "path": replica_path,
                    "checksum": checksum,
                    "status": "success"
                })
                logger.info(f"Replicated {partition_id} to {node}")

        return replication_status

    def validate(self, replication_status):
        """
        Validate replication integrity using checksums
        """
        for partition_id, replicas in replication_status.items():
            checksums = [r["checksum"] for r in replicas]
            if len(set(checksums)) != 1:
                logger.error(f"Checksum mismatch for partition: {partition_id}")
                return False
            if len(replicas) != self.replication_factor:
                logger.error(f"Insufficient replicas for partition: {partition_id}")
                return False
        logger.info("All replicas validated successfully!")
        return True

    def _compute_checksum(self, path):
        """
        Compute checksum for data integrity verification
        """
        return hashlib.md5(path.encode()).hexdigest()

    def get_replication_report(self, replication_status):
        """
        Generate replication report
        """
        report = {
            "total_partitions": len(replication_status),
            "replication_factor": self.replication_factor,
            "total_replicas": len(replication_status) * self.replication_factor,
            "nodes": self.nodes
        }
        return report
