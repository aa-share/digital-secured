import unittest
import os
import re
from pathlib import Path

class TestDigitalSecured(unittest.TestCase):

    def setUp(self):
        self.root_dir = Path(__file__).parent
        self.index_html = self.root_dir / "index.html"
        self.index_dev_html = self.root_dir / "index.dev.html"
        self.robots_txt = self.root_dir / "robots.txt"
        self.static_dir = self.root_dir / "static"

    def test_required_files_exist(self):
        """Verify core files exist in repository root."""
        self.assertTrue(self.index_html.exists(), "index.html is missing")
        self.assertTrue(self.index_dev_html.exists(), "index.dev.html is missing")
        self.assertTrue(self.robots_txt.exists(), "robots.txt is missing")
        self.assertTrue(self.static_dir.is_dir(), "static/ directory is missing")

    def test_robots_txt_disallows_static(self):
        """Verify robots.txt blocks web crawlers from /static/."""
        content = self.robots_txt.read_text(encoding="utf-8")
        self.assertIn("Disallow: /static/", content)

    def test_pdf_asset_exists_and_not_empty(self):
        """Ensure at least one valid non-empty PDF exists in static/."""
        pdf_files = list(self.static_dir.glob("*.pdf"))
        self.assertGreater(len(pdf_files), 0, "No PDF file found in static/")

        for pdf in pdf_files:
            self.assertGreater(pdf.stat().st_size, 0, f"PDF file {pdf.name} is empty")

    def test_html_references_existing_pdf(self):
        """Verify that index.html and index.dev.html reference an existing PDF file."""
        pdf_pattern = re.compile(r'static/doc_[a-f0-9]{32}\.pdf')

        for html_file in [self.index_html, self.index_dev_html]:
            content = html_file.read_text(encoding="utf-8")
            matches = pdf_pattern.findall(content)
            self.assertGreater(len(matches), 0, f"No valid PDF path match found in {html_file.name}")

            referenced_pdf = self.root_dir / matches[0]
            self.assertTrue(
                referenced_pdf.exists(),
                f"Referenced PDF '{matches[0]}' in {html_file.name} does not exist on disk"
            )

if __name__ == "__main__":
    unittest.main()