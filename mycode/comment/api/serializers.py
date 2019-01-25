from rest_framework.serializers import ModelSerializer, SerializerMethodField
from comment.models import Comment


class CommentSerializers(ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'title',
            'user',
            'timestamp',
            'content',
        ]
