import os

from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
logo = os.path.join(BASE_DIR, "static/images/logo.png")

JAZZMIN_SETTINGS = {
    "site_title": "FixYourPlants Admin",
    "site_header": "FixYourPlants",
    "site_brand": "FixYourPlants",
    "site_logo": logo,
    "login_logo": logo,
    "login_logo_dark": logo,
    "site_logo_classes": "img-circle",
    "site_icon": "icon-leaf",
    "welcome_sign": "Welcome to FixYourPlants",
    "copyright": "FixYourPlants Ltd",
    "search_model": ["users.User", "plants.Plant", "sickness.Sickness"],
    "user_avatar": None,
    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Support", "url": "https://github.com/FixYourPlants/fyp-api/issues", "new_window": True},
        {"name": "Api Docs (Swagger)", "url": config("BACKEND_URL", default="https://fyp-api-0yf4.onrender.com/") + "/docs/",  "new_window": True},
        {"name": "Api Docs (Redoc)", "url": config("BACKEND_URL", default="https://fyp-api-0yf4.onrender.com/") + "/redoc/",  "new_window": True},
        {"name": "Documentation", "url": config("DOCS_URL", default="https://fyp-doc.onrender.com/"), "new_window": True},
        {"model": "auth.User"},
    ],
    "usermenu_links": [
        {"name": "Support", "url": "https://github.com/FixYourPlants/fyp-api/issues", "new_window": True},
        {"model": "auth.user"},
    ],
    "show_sidebar": True,
    "navigation_expanded": False,
    "hide_apps": [],
    "hide_models": [],
    "order_with_respect_to": [
        "plants",
        "sickness",
        "diary",
        "notification",
        "users",
        "auth"
    ],
    "icons": {
        "auth": "fas fa-users-cog",
        "users.User": "fas fa-user",
        "auth.Group": "fas fa-users",
        "diary.Diary": "fas fa-book",
        "diary.Page": "fas fa-file",
        "notification.Notification": "fas fa-bell",
        "plants.Plant": "fas fa-leaf",
        "plants.Characteristic": "fas fa-cogs",
        "plants.History": "fas fa-history",
        "plants.Opinion": "fas fa-comment",
        "sickness.Sickness": "fas fa-bug",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    "related_modal_active": False,
    "use_google_fonts_cdn": True,
    "show_ui_builder": False,
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
    "language_chooser": False,

}


JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "darkly",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    }
}