from django.forms import ModelForm
from blogging.models import Post

class MyPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title',
                  'text',
                  'author',
                  ]
        # removed publish date so you cannot publish
        # a post using the model form

