"""Google Cloud Storage file operation helpers."""

from urllib.parse import urlparse

from google.cloud import storage


def is_gcs_uri(path: str) -> bool:
    """Check whether a path is a GCS URI (gs://...)."""
    return path.startswith("gs://")


def parse_gcs_uri(uri: str) -> tuple[str, str]:
    """Parse a gs:// URI into (bucket, blob_path)."""
    parsed = urlparse(uri)
    if parsed.scheme != "gs":
        raise ValueError(f"Expected gs:// URI, got: {uri}")
    return parsed.netloc, parsed.path.lstrip("/")


def get_storage_client(project_id: str) -> storage.Client:
    """Create a GCS client with the given project ID."""
    return storage.Client(project=project_id)


def download_from_gcs(uri: str, local_path: str, project_id: str):
    """Download a file from GCS to a local path."""
    bucket_name, blob_path = parse_gcs_uri(uri)
    client = get_storage_client(project_id)
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(blob_path)
    blob.download_to_filename(local_path)
    print(f"Downloaded {uri} -> {local_path}")


def upload_to_gcs(local_path: str, uri: str, project_id: str):
    """Upload a local file to GCS."""
    bucket_name, blob_path = parse_gcs_uri(uri)
    client = get_storage_client(project_id)
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(blob_path)
    blob.upload_from_filename(local_path)
    print(f"Uploaded {local_path} -> {uri}")


def delete_gcs_blobs(uris: list[str], project_id: str):
    """Delete a list of GCS URIs."""
    client = get_storage_client(project_id)
    for uri in uris:
        bucket_name, blob_path = parse_gcs_uri(uri)
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(blob_path)
        blob.delete()
        print(f"Deleted {uri}")
