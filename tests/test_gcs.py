"""Tests for utils.gcs module."""

import unittest
from unittest.mock import patch, MagicMock

from utils.gcs import is_gcs_uri, parse_gcs_uri, download_from_gcs, upload_to_gcs, delete_gcs_blobs


class TestIsGcsUri(unittest.TestCase):
    def test_valid_gs_uri(self):
        self.assertTrue(is_gcs_uri("gs://bucket/path"))

    def test_local_path(self):
        self.assertFalse(is_gcs_uri("/local/path"))

    def test_s3_uri(self):
        self.assertFalse(is_gcs_uri("s3://bucket"))

    def test_empty_string(self):
        self.assertFalse(is_gcs_uri(""))


class TestParseGcsUri(unittest.TestCase):
    def test_full_path(self):
        bucket, blob = parse_gcs_uri("gs://my-bucket/path/to/file.opus")
        self.assertEqual(bucket, "my-bucket")
        self.assertEqual(blob, "path/to/file.opus")

    def test_simple_path(self):
        bucket, blob = parse_gcs_uri("gs://bucket/file")
        self.assertEqual(bucket, "bucket")
        self.assertEqual(blob, "file")

    def test_non_gs_uri_raises(self):
        with self.assertRaises(ValueError):
            parse_gcs_uri("s3://bucket/file")

    def test_http_uri_raises(self):
        with self.assertRaises(ValueError):
            parse_gcs_uri("https://storage.googleapis.com/bucket/file")


class TestDownloadFromGcs(unittest.TestCase):
    @patch("utils.gcs.get_storage_client")
    def test_download(self, mock_get_client):
        mock_client = MagicMock()
        mock_get_client.return_value = mock_client
        mock_bucket = MagicMock()
        mock_client.bucket.return_value = mock_bucket
        mock_blob = MagicMock()
        mock_bucket.blob.return_value = mock_blob

        download_from_gcs("gs://my-bucket/path/file.opus", "/tmp/file.opus", "proj-123")

        mock_get_client.assert_called_once_with("proj-123")
        mock_client.bucket.assert_called_once_with("my-bucket")
        mock_bucket.blob.assert_called_once_with("path/file.opus")
        mock_blob.download_to_filename.assert_called_once_with("/tmp/file.opus")


class TestUploadToGcs(unittest.TestCase):
    @patch("utils.gcs.get_storage_client")
    def test_upload(self, mock_get_client):
        mock_client = MagicMock()
        mock_get_client.return_value = mock_client
        mock_bucket = MagicMock()
        mock_client.bucket.return_value = mock_bucket
        mock_blob = MagicMock()
        mock_bucket.blob.return_value = mock_blob

        upload_to_gcs("/tmp/file.opus", "gs://my-bucket/path/file.opus", "proj-123")

        mock_get_client.assert_called_once_with("proj-123")
        mock_client.bucket.assert_called_once_with("my-bucket")
        mock_bucket.blob.assert_called_once_with("path/file.opus")
        mock_blob.upload_from_filename.assert_called_once_with("/tmp/file.opus")


class TestDeleteGcsBlobs(unittest.TestCase):
    @patch("utils.gcs.get_storage_client")
    def test_delete_multiple(self, mock_get_client):
        mock_client = MagicMock()
        mock_get_client.return_value = mock_client
        mock_bucket = MagicMock()
        mock_client.bucket.return_value = mock_bucket
        mock_blob = MagicMock()
        mock_bucket.blob.return_value = mock_blob

        uris = ["gs://bucket/a.opus", "gs://bucket/b.opus"]
        delete_gcs_blobs(uris, "proj-123")

        self.assertEqual(mock_blob.delete.call_count, 2)

    @patch("utils.gcs.get_storage_client")
    def test_delete_empty_list(self, mock_get_client):
        mock_client = MagicMock()
        mock_get_client.return_value = mock_client

        delete_gcs_blobs([], "proj-123")
        mock_client.bucket.assert_not_called()


if __name__ == "__main__":
    unittest.main()
