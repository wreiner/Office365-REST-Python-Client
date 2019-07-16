from office365.runtime.client_object_collection import ClientObjectCollection
from office365.outlookservices.attachment import Attachment


class AttachmentCollection(ClientObjectCollection):
    """Attachment collection"""

    def __init__(self, context, resource_path=None):
        super(AttachmentCollection, self).__init__(context, Attachment, resource_path)
