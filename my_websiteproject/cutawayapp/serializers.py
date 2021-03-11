from rest_framework import serializers
from cutawayapp.models import Blog


class BlogSerializers(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, blog):
        request = self.context.get('request')
        image_url = blog.image.url
        return request.build_absolute_uri(image_url)

    class Meta:
        model = Blog
        fields = ('id', 'name', 'text', 'image', 'date')
