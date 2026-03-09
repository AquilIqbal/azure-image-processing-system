import os
import io
from azure.storage.blob import BlobServiceClient


class AzureBlobHelper:
    def __init__(self):
        # Azure Blob connection string goes here via environment variable.
        # Example: DefaultEndpointsProtocol=https;AccountName=...;AccountKey=...;EndpointSuffix=core.windows.net
        connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING", "")
        self.container_name = os.getenv("AZURE_BLOB_CONTAINER", "processed-images")
        self.blob_service_client = None
        self.container_client = None

        if connection_string:
            self.blob_service_client = BlobServiceClient.from_connection_string(connection_string)
            self.container_client = self.blob_service_client.get_container_client(self.container_name)
            self._ensure_container_exists()

    def _ensure_container_exists(self):
        if not self.container_client.exists():
            self.container_client.create_container()

    def _require_container(self):
        if not self.container_client:
            raise ValueError(
                "AZURE_STORAGE_CONNECTION_STRING is not set. "
                "Configure it before upload/download/delete operations."
            )

    def upload_image(self, blob_name, file_stream):
        self._require_container()
        file_stream.seek(0)
        blob_client = self.container_client.get_blob_client(blob=blob_name)
        blob_client.upload_blob(file_stream, overwrite=True)
        return blob_client.url

    def download_image(self, blob_name):
        self._require_container()
        blob_client = self.container_client.get_blob_client(blob=blob_name)
        data = blob_client.download_blob().readall()
        return io.BytesIO(data)

    def delete_image(self, blob_name):
        self._require_container()
        blob_client = self.container_client.get_blob_client(blob=blob_name)
        blob_client.delete_blob(delete_snapshots="include")
