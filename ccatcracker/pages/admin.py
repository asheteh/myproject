from django.contrib import admin


from .models import Center

from .models import Ranks,question,Aptitude,CCAT_Question,DS
    

admin.site.register(Center)
admin.site.register(Ranks)
admin.site.register(question)
admin.site.register(Aptitude)
admin.site.register(CCAT_Question)
admin.site.register(DS)


