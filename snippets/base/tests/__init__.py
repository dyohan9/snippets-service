import random
import string

from django.test import TransactionTestCase

import factory

from snippets.base import models


class TestCase(TransactionTestCase):
    pass


class SnippetTemplateFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: 'Test Template {0}'.format(n))
    code = factory.Sequence(lambda n: '<p>Test Snippet {0}</p>'.format(n))
    code_name = factory.Sequence(lambda n: 'test_var_{0}'.format(n))
    version = '1.0.0'

    @factory.post_generation
    def variable_set(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            self.variable_set.add(*extracted)

    class Meta:
        model = models.SnippetTemplate


class SnippetTemplateVariableFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: 'test_var_{0}'.format(n))
    template = factory.SubFactory(SnippetTemplateFactory)

    class Meta:
        model = models.SnippetTemplateVariable


class BaseSnippetFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: 'Test Snippet {0}'.format(n))
    published = True
    on_release = True

    @factory.post_generation
    def client_match_rules(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            self.client_match_rules.add(*extracted)

    @factory.post_generation
    def locales(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted is None:
            extracted = ['en-us']

        locales = [models.TargetedLocale.objects.get_or_create(code=code, name=code)[0]
                   for code in extracted]
        self.locales.add(*locales)

    @factory.post_generation
    def countries(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            countries = [
                models.TargetedCountry.objects.get_or_create(code=code, name=code)[0]
                for code in extracted]
            self.countries.add(*countries)


class SnippetFactory(BaseSnippetFactory):
    template = factory.SubFactory(SnippetTemplateFactory)
    on_startpage_5 = True

    class Meta:
        model = models.Snippet


class ClientMatchRuleFactory(factory.django.DjangoModelFactory):
    description = factory.Sequence(lambda n: 'Client Match Rule {0}'.format(n))

    class Meta:
        model = models.ClientMatchRule


class SearchProviderFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: 'Search Provider {0}'.format(n))
    identifier = factory.Sequence(lambda n: 'search-provider-{0}'.format(n))

    class Meta:
        model = models.SearchProvider


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Sequence(lambda n: 'User {0}'.format(n))

    class Meta:
        model = 'auth.User'
        django_get_or_create = ('username',)


class TargetFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: 'Target {0}'.format(n))
    creator = factory.SubFactory(UserFactory)
    on_release = True

    class Meta:
        model = models.Target


class CampaignFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: 'Campaign {0}'.format(n))
    slug = factory.Sequence(lambda n: 'campaign_{0}'.format(n))
    creator = factory.SubFactory(UserFactory)

    class Meta:
        model = models.Campaign


class CategoryFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: 'Campaign {0}'.format(n))
    creator = factory.SubFactory(UserFactory)

    class Meta:
        model = models.Category


class ProductFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: 'Campaign {0}'.format(n))
    creator = factory.SubFactory(UserFactory)

    class Meta:
        model = models.Product


class IconFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: 'Icon {0}'.format(n))
    creator = factory.SubFactory(UserFactory)
    image = factory.django.ImageField(width=192, height=192,
                                      format='PNG', filename='example.png')

    class Meta:
        model = models.Icon


class SimpleTemplateFactory(factory.django.DjangoModelFactory):
    text = 'This is the main text with a <a href="https://example.com">link</a>.'
    icon = factory.SubFactory(IconFactory)

    class Meta:
        model = models.SimpleTemplate


class ASRSnippetFactory(factory.django.DjangoModelFactory):
    creator = factory.SubFactory(UserFactory)
    name = factory.Sequence(lambda n: 'ASRSnippet {0}'.format(n))
    category = factory.SubFactory(CategoryFactory, creator=factory.SelfAttribute('..creator'))
    product = factory.SubFactory(ProductFactory, creator=factory.SelfAttribute('..creator'))
    template_relation = factory.RelatedFactory(SimpleTemplateFactory, 'snippet')
    status = models.STATUS_CHOICES['Approved']

    class Meta:
        model = models.ASRSnippet

    @factory.post_generation
    def set_template_relation_to_template_model(self, *args, **kwargs):
        """By default this Factory creates and relates a SimpleTemplate to this
        new ASRSnippet object. The Django Admin on the other hand, relates a
        Template obj when saving a ASRSnippet object. We use this method to
        make the Factory behave like Django Admin.
        """
        self.template_relation = self.template_relation.template_ptr

    @factory.post_generation
    def locale(self, create, extracted, **kwargs):
        if not create:
            return

        code = extracted or 'en-us'
        if code[0] != ',':
            code = ',' + code
        if code[-1] != ',':
            code = code + ','
        locale = models.Locale.objects.get_or_create(code=code, name=code)[0]
        self.locale = locale

    @factory.post_generation
    def add_tags(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            self.tags.add(*extracted)


class AddonFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: 'Addon {}'.format(n))
    guid = factory.Sequence(lambda n: 'addon_{}'.format(n))
    url = factory.Sequence(lambda n: 'https://example.com/{}'.format(n))

    class Meta:
        model = models.Addon


class LocaleFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: 'Locale {}'.format(n))
    code = factory.LazyAttribute(lambda o: ''.join(random.choices(string.ascii_lowercase, k=4)))

    class Meta:
        model = models.Locale


class DistributionFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: 'Distribution {}'.format(n))

    class Meta:
        model = models.Distribution
        django_get_or_create = ('name',)


class DistributionBundleFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: 'Distribution Bundle {}'.format(n))
    code_name = factory.Sequence(lambda n: 'distribution_bundle_{}'.format(n))

    class Meta:
        model = models.DistributionBundle
        django_get_or_create = ('name', 'code_name')


class JobFactory(factory.django.DjangoModelFactory):
    creator = factory.SubFactory(UserFactory)
    campaign = factory.SubFactory(CampaignFactory, creator=factory.SelfAttribute('..creator'))
    status = models.Job.PUBLISHED
    snippet = factory.SubFactory(ASRSnippetFactory, creator=factory.SelfAttribute('..creator'))
    distribution = factory.SubFactory(DistributionFactory, name='Default')

    class Meta:
        model = models.Job

    @factory.post_generation
    def targets(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted is None:
            extracted = [TargetFactory(creator=self.creator)]

        for target in extracted:
            self.targets.add(target)
