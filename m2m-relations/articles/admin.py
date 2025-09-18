from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope

# проверка одного основного тега
class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        super().clean()
        main_count = 0
        for form in self.forms:
            if form.cleaned_data and not form.cleaned_data.get('DELETE', False):
                if form.cleaned_data.get('is_main', False):
                    main_count += 1
        if main_count == 0:
            raise ValidationError('Укажите основной раздел')
        if main_count > 1:
            raise ValidationError('Основным может быть только один раздел')


# Inline для связи Article-Tag
class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 1  # форм для добавления нового
    formset = ScopeInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at')
    search_fields = ('title', 'text')
    inlines = [ScopeInline]  # подключаем inline для тегов


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    list_display = ('article', 'tag', 'is_main')
    list_filter = ('is_main',)
