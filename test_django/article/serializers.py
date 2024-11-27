from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
 class Meta:
  model = Article
  fields = ('id', 'title', 'description', 'body', 'author_id')
class CapitalSerializer(serializers.Serializer):
    capital_city = serializers.CharField(max_length=200)
    capital_population = serializers.IntegerField()
    author = serializers.CharField(source='author.username', max_length=200)