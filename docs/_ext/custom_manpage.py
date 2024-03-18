"""Custom sphinx extension to include manpage."""


def setup(app):
    """Setup connect events to the man builder."""
    app.connect("builder-inited", include_manpage)


def include_manpage(app):
    """Update the excluded patterns to include the manpage."""
    if app.builder.name != "man":
        return

    for pattern in app.config.exclude_patterns:
        if "manpage" in pattern:
            app.config.exclude_patterns.remove(pattern)
