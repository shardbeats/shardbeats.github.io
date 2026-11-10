#!/usr/bin/env python3
"""Pull the latest release tag for each tool and push it into the site.

What it touches:
    versions.json               slug -> version, the single source of truth
    <slug>/index.html           regenerated via build_tool_pages.py
    en/<slug>/index.html        same
    index.html, en/index.html   only the version label in each card and the
                                softwareVersion inside the JSON-LD

Run locally:
    python scripts/sync_versions.py

In CI the GITHUB_TOKEN is used when present (raises the API rate limit).
Exit code is 0 whether or not anything changed, unless a fetch fails.
"""

import json
import os
import re
import sys
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))

import build_tool_pages as gen  # noqa: E402

VERSIONS_FILE = os.path.join(ROOT, 'versions.json')
OWNER = 'shardbeats'

# slug -> repository name
REPOS = {
    'trakkstudio': 'TRAKKSTUDIO',
    'trakkconverter': 'TRAKKCONVERTER',
    'trakknormalizer': 'TRAKKNORMALIZER',
    'trakkname': 'TRAKKNAME',
    'trakkout': 'TRAKKOUT',
    'trakklicense': 'TRAKKLICENSE',
}


def latest_version(repo, token=None):
    url = 'https://api.github.com/repos/%s/%s/releases/latest' % (OWNER, repo)
    req = urllib.request.Request(url, headers={
        'Accept': 'application/vnd.github+json',
        'User-Agent': 'trakk-suite-site',
    })
    if token:
        req.add_header('Authorization', 'Bearer ' + token)
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.load(resp)
    tag = (data.get('tag_name') or '').strip()
    m = re.match(r'^[vV]?(\d[\w.\-+]*)$', tag)
    return m.group(1) if m else tag.lstrip('vV')


def patch_index(path, versions):
    """Update the card label and the softwareVersion in the JSON-LD."""
    with open(path, encoding='utf-8') as f:
        html = f.read()
    original = html

    for slug, version in versions.items():
        name = REPOS[slug]

        card = re.compile(
            r'(id="%s"[\s\S]{0,2000}?<span class="tag version">v)([^<]*)(</span>)'
            % re.escape(slug)
        )
        html, n_card = card.subn(lambda m, v=version: m.group(1) + v + m.group(3), html, count=1)

        spec = re.compile(
            r'("name":\s*"%s",[\s\S]{0,2000}?"softwareVersion":\s*")([^"]*)(")'
            % re.escape(name)
        )
        html, n_spec = spec.subn(lambda m, v=version: m.group(1) + v + m.group(3), html, count=1)

        if n_card != 1:
            print('  WARN %s: card label matched %d times (%s)' % (os.path.basename(path), n_card, slug))
        if n_spec != 1:
            print('  WARN %s: softwareVersion matched %d times (%s)' % (os.path.basename(path), n_spec, slug))

    if html != original:
        with open(path, 'w', encoding='utf-8', newline='\n') as f:
            f.write(html)
        return True
    return False


def main():
    token = os.environ.get('GITHUB_TOKEN') or os.environ.get('GH_TOKEN')

    versions = {}
    failures = []
    for slug, repo in REPOS.items():
        try:
            versions[slug] = latest_version(repo, token)
            print('  %-16s %s' % (slug, versions[slug]))
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:
            failures.append((slug, str(e)))
            print('  %-16s FAILED: %s' % (slug, e))

    if failures:
        print('\nRefusing to write: %d fetch(es) failed.' % len(failures))
        return 1

    previous = {}
    if os.path.exists(VERSIONS_FILE):
        try:
            with open(VERSIONS_FILE, encoding='utf-8') as f:
                previous = json.load(f)
        except ValueError:
            previous = {}

    with open(VERSIONS_FILE, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(versions, f, indent=2, sort_keys=True)
        f.write('\n')

    changed = {k: (previous.get(k), v) for k, v in versions.items() if previous.get(k) != v}
    if changed:
        for slug, (old, new) in changed.items():
            print('  changed %-16s %s -> %s' % (slug, old or '(none)', new))
    else:
        print('  no version changes')

    gen.main()

    for rel in ('index.html', os.path.join('en', 'index.html')):
        path = os.path.join(ROOT, rel)
        if patch_index(path, versions):
            print('  patched %s' % rel)
        else:
            print('  unchanged %s' % rel)

    return 0


if __name__ == '__main__':
    sys.exit(main())
