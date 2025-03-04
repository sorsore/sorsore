import os
from django.apps import apps
from django.conf import settings


class _DefaultSettings:
    CRX_PROTECTED_MEDIA_URL = "/protected/"
    CRX_PROTECTED_MEDIA_ROOT = os.path.join(settings.BASE_DIR, "protected")
    CRX_PROTECTED_MEDIA_UPLOAD_WHITELIST = []
    CRX_PROTECTED_MEDIA_UPLOAD_BLACKLIST = [
        ".app",
        ".bat",
        ".exe",
        ".jar",
        ".php",
        ".pl",
        ".ps1",
        ".py",
        ".rb",
        ".sh",
    ]

    CRX_FRONTEND_BTN_SIZE_DEFAULT = ""
    CRX_FRONTEND_BTN_SIZE_CHOICES = [
        ("btn-sm", "Small"),
        ("", "Default"),
        ("btn-lg", "Large"),
    ]

    CRX_FRONTEND_BTN_STYLE_DEFAULT = "btn-primary"
    CRX_FRONTEND_BTN_STYLE_CHOICES = [
        ("btn-primary", "Primary"),
        ("btn-secondary", "Secondary"),
        ("btn-success", "Success"),
        ("btn-danger", "Danger"),
        ("btn-warning", "Warning"),
        ("btn-info", "Info"),
        ("btn-link", "Link"),
        ("btn-light", "Light"),
        ("btn-dark", "Dark"),
        ("btn-outline-primary", "Outline Primary"),
        ("btn-outline-secondary", "Outline Secondary"),
        ("btn-outline-success", "Outline Success"),
        ("btn-outline-danger", "Outline Danger"),
        ("btn-outline-warning", "Outline Warning"),
        ("btn-outline-info", "Outline Info"),
        ("btn-outline-light", "Outline Light"),
        ("btn-outline-dark", "Outline Dark"),
    ]

    CRX_FRONTEND_COL_SIZE_DEFAULT = ""
    CRX_FRONTEND_COL_SIZE_CHOICES = [
        ("", "Automatically size"),
        ("12", "Full row"),
        ("6", "Half - 1/2 column"),
        ("4", "Thirds - 1/3 column"),
        ("8", "Thirds - 2/3 column"),
        ("3", "Quarters - 1/4 column"),
        ("9", "Quarters - 3/4 column"),
        ("2", "Sixths - 1/6 column"),
        ("10", "Sixths - 5/6 column"),
        ("1", "Twelfths - 1/12 column"),
        ("5", "Twelfths - 5/12 column"),
        ("7", "Twelfths - 7/12 column"),
        ("11", "Twelfths - 11/12 column"),
    ]

    CRX_FRONTEND_COL_BREAK_DEFAULT = "md"
    CRX_FRONTEND_COL_BREAK_CHOICES = [
        ("", "Always expanded"),
        ("sm", "sm - Expand on small screens (phone, 576px) and larger"),
        ("md", "md - Expand on medium screens (tablet, 768px) and larger"),
        ("lg", "lg - Expand on large screens (laptop, 992px) and larger"),
        ("xl", "xl - Expand on extra large screens (wide monitor, 1200px)"),
    ]

    CRX_FRONTEND_NAVBAR_FORMAT_DEFAULT = ""
    CRX_FRONTEND_NAVBAR_FORMAT_CHOICES = [
        ("", "Default Bootstrap Navbar"),
        ("crx-navbar-center", "Centered logo at top"),
    ]

    CRX_FRONTEND_NAVBAR_COLOR_SCHEME_DEFAULT = "navbar-light"
    CRX_FRONTEND_NAVBAR_COLOR_SCHEME_CHOICES = [
        ("navbar-light", "Light - for use with a light-colored navbar"),
        ("navbar-dark", "Dark - for use with a dark-colored navbar"),
    ]

    CRX_FRONTEND_NAVBAR_CLASS_DEFAULT = "bg-light"

    CRX_FRONTEND_NAVBAR_COLLAPSE_MODE_DEFAULT = "navbar-expand-lg"
    CRX_FRONTEND_NAVBAR_COLLAPSE_MODE_CHOICES = [
        (
            "",
            "Never show menu - Always collapse menu behind a button",
        ),
        (
            "navbar-expand-sm",
            "sm - Show on small screens (phone size) and larger",
        ),
        (
            "navbar-expand-md",
            "md - Show on medium screens (tablet size) and larger",
        ),
        (
            "navbar-expand-lg",
            "lg - Show on large screens (laptop size) and larger",
        ),
        (
            "navbar-expand-xl",
            "xl - Show on extra large screens (desktop, wide monitor)",
        ),
    ]

    SORSORE_TEMPLATE_DEFAULT = "None"
    THEMES_LIST = os.listdir(os.getcwd() + "/patterns/templates/patterns")
    THEMES = [(i, i) for i in THEMES_LIST]
    THEMES.insert(0, ("None", "None"))
    SORSORE_TEMPLATE_CHOICES = THEMES

    CRX_FRONTEND_THEME_DEFAULT = ""
    CRX_FRONTEND_THEME_CHOICES = [
        ("", "Default - Classic Bootstrap"),
        ("cerulean", "Cerulean - A calm blue sky"),
        ("cosmo", "Cosmo - An ode to Metro"),
        ("cyborg", "Cyborg - Jet black and electric blue"),
        ("darkly", "Darkly - Flatly in night mode"),
        ("flatly", "Flatly - Flat and modern"),
        ("journal", "Journal - Crisp like a new sheet of paper"),
        ("litera", "Litera - The medium is the message"),
        ("lumen", "Lumen - Light and shadow"),
        ("lux", "Lux - A touch of class"),
        ("materia", "Materia - Material is the metaphor"),
        ("minty", "Minty - A fresh feel"),
        ("morph", "Morph - A neumorphic layer"),
        ("pulse", "Pulse - A trace of purple"),
        ("quartz", "Quartz - A glassmorphic layer"),
        ("sandstone", "Sandstone - A touch of warmth"),
        ("simplex", "Simplex - Mini and minimalist"),
        ("sketchy", "Sketchy - A hand-drawn look for mockups and mirth"),
        ("slate", "Slate - Shades of gunmetal gray"),
        ("solar", "Solar - A dark spin on Solarized"),
        ("spacelab", "Spacelab - Silvery and sleek"),
        ("superhero", "Superhero - The brave and the blue"),
        ("united", "United - Ubuntu orange and unique font"),
        ("vapor", "Vapor - A cyberpunk aesthetic"),
        ("yeti", "Yeti - A friendly foundation"),
        ("zephyr", "Zephyr - Breezy and beautiful"),
    ]

    CRX_FRONTEND_TEMPLATES_BLOCKS = {
        "cardblock": [
            (
                "sorsore/blocks/card_block.html",
                "Card",
            ),
            (
                "sorsore/blocks/card_head.html",
                "Card with header",
            ),
            (
                "sorsore/blocks/card_foot.html",
                "Card with footer",
            ),
            (
                "sorsore/blocks/card_head_foot.html",
                "Card with header and footer",
            ),
            (
                "sorsore/blocks/card_blurb.html",
                "Blurb - rounded image and no border",
            ),
            (
                "sorsore/blocks/card_img.html",
                "Cover image - use image as background",
            ),
        ],
        "cardgridblock": [
            (
                "sorsore/blocks/cardgrid_group.html",
                "Card group - attached cards of equal size",
            ),
            (
                "sorsore/blocks/cardgrid_deck.html",
                "Card deck - separate cards of equal size",
            ),
            (
                "sorsore/blocks/cardgrid_columns.html",
                "Card masonry - fluid brick pattern",
            ),
        ],
        # DEPRECATED: Remove in 3.0.
        "pagelistblock": [
            (
                "sorsore/blocks/pagelist_block.html",
                "General, simple list",
            ),
            (
                "sorsore/blocks/pagelist_list_group.html",
                "General, list group navigation panel",
            ),
            (
                "sorsore/blocks/pagelist_article_media.html",
                "Article, media format",
            ),
            (
                "sorsore/blocks/pagelist_article_card_group.html",
                "Article, card group - attached cards of equal size",
            ),
            (
                "sorsore/blocks/pagelist_article_card_deck.html",
                "Article, card deck - separate cards of equal size",
            ),
            (
                "sorsore/blocks/pagelist_article_card_columns.html",
                "Article, card masonry - fluid brick pattern",
            ),
        ],
        # DEPRECATED: Remove in 3.0
        "pagepreviewblock": [
            (
                "sorsore/blocks/pagepreview_card.html",
                "Card",
            ),
            (
                "sorsore/blocks/pagepreview_form.html",
                "Form inputs",
            ),
        ],
        # templates that are available for all block types
        "*": [
            ("", "Default"),
        ],
    }

    CRX_FRONTEND_TEMPLATES_PAGES = {
        # templates that are available for all page types
        "*": [
            (
                "",
                "Default",
            ),
            (
                "sorsore/pages/web_page.html",
                "Web page showing title and cover image",
            ),
            (
                "sorsore/pages/web_page_notitle.html",
                "Web page without title and cover image",
            ),
            (
                "sorsore/pages/home_page.html",
                "Home page without title and cover image",
            ),
            (
                "sorsore/pages/base.html",
                "Blank page - no navbar or footer",
            ),
        ],
    }

    CRX_BANNER = None
    CRX_BANNER_BACKGROUND = "#ff0"
    CRX_BANNER_TEXT_COLOR = "#000"

    def __getattribute__(self, attr: str):
        # First load from Django settings.
        # If it does not exist, load from _DefaultSettings.
        try:
            return getattr(settings, attr)
        except AttributeError:
            return super().__getattribute__(attr)


crx_settings = _DefaultSettings()


# If the older django-bootstrap4 is the only version listed in INSTALLED_APPS,
# use it for compatibility. Otherwise use django-bootstrap5 which is a
# dependency of sorsore.
if apps.is_installed("bootstrap4") and not apps.is_installed(
    "django_bootstrap5"
):
    import bootstrap4.bootstrap as bootstrap
else:
    import django_bootstrap5.core as bootstrap


get_bootstrap_setting = bootstrap.get_bootstrap_setting
