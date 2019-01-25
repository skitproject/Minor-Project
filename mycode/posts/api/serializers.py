from rest_framework.serializers import ModelSerializer, SerializerMethodField  # , HyperlinkedIdentityField
from posts.models import post


class PostCreateSerializers(ModelSerializer):
    class Meta:
        model = post
        fields = [
            'title',
            'user',
            'timestamp',
            'content',
        ]


class PostDetailSerializers(ModelSerializer):
    user = SerializerMethodField()
    image = SerializerMethodField()

    class Meta:
        model = post
        fields = ['title', 'slug', 'user', 'timestamp', 'content', 'image']

    def get_user(self, obj):
        return str(obj.user.username)

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image


class PostListSerializers(ModelSerializer):
    # url = HyperlinkedIdentityField(
    #     view_name='apii:detail',
    #     lookup_field='slug'
    #     )

    user = SerializerMethodField()

    class Meta:
        model = post
        fields = [
            'title',
            'slug',
            'user',
            # 'url',
            # 'timestamp',
        ]

    def get_user(self, obj):
        return str(obj.user.username)
