"""Custom sphinx extension to generate text file sitemap"""

from pathlib import Path


def setup(app):
    """Setup connect events to the sitemap builder"""
    app.add_config_value("sitemap_excluded_pages", default=[], rebuild="")
    app.connect("html-page-context", add_links)
    app.connect("build-finished", create_sitemap)
    app.sitemap_pages = []


def add_links(app, pagename, *args):
    """As each page is built, collect page names for the sitemap"""
    excluded_pages = app.config.sitemap_excluded_pages
    excluded_pages = list(set(excluded_pages + ["404", "search", "genindex"]))
    if pagename not in excluded_pages and not pagename.startswith("_"):
        app.sitemap_pages.append(f"{pagename}")


def create_sitemap(app, exception):
    """Generates the sitemap.txt from the collected pages"""
    site_url = app.builder.config.html_baseurl.rstrip("/") + "/"

    if not site_url or exception is not None or not app.sitemap_pages:
        print("error while generating sitemap")
        return

    output_path = Path(app.outdir)

    # write sitemap
    sitemap_links = [f"{site_url}{page}.html" for page in app.sitemap_pages]
    sitemap_file = output_path.joinpath("sitemap.txt")
    sitemap_file.write_text("\n".join(sitemap_links))

    # update robots with sitemap url
    sitemap_url = site_url + sitemap_file.name
    robots_file = output_path.joinpath("robots.txt")
    robots_file.write_text(robots_file.read_text().replace("sitemap_url", sitemap_url))
