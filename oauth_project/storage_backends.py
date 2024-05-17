from storages.backends.s3boto3 import S3Boto3Storage

from oauth_project import settings


class StaticStorage(S3Boto3Storage):
    location = 'static'
    default_acl = 'public-read'


class MediaStorage(S3Boto3Storage):
    location = 'media'
    file_overwrite = False


class PrivateMediaStorage(S3Boto3Storage):
    location = 'media'
    default_acl = 'private'
    file_overwrite = False
    custom_domain = False

    def url(self, name):
        # Generates a signed URL
        url = self.connection.meta.client.generate_presigned_url(
            'get_object',
            Params={
                'Bucket': settings.AWS_STORAGE_BUCKET_NAME,
                'Key': name
            },
            ExpiresIn=3600  # or any other duration
        )
        return url
