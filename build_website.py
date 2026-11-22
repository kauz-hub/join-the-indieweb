"""Regenerate the static companion website from the Markdown guide (requires Pandoc)."""
from pathlib import Path
import html
import re
import subprocess

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / 'docs'
DOCS.mkdir(exist_ok=True)
CHAPTERS = [
    ('01-what-is-the-indieweb', 'What is the IndieWeb?', 'Own your identity, content and little corner of the internet.'),
    ('02-choose-a-platform', 'Choose your platform', 'Compare handmade sites, hosted blogs, static generators and CMSs.'),
    ('03-domains-and-hosting', 'Domains & hosting', 'Register an address, understand DNS and publish a site.'),
    ('04-learn-the-web', 'Learn the web', 'A practical roadmap for HTML, CSS, accessibility and Git.'),
    ('05-build-your-site', 'Build your personal site', 'Ideas for pages, navigation, design and your first post.'),
    ('06-publishing-and-feeds', 'Publishing & RSS feeds', 'Share your writing, follow blogs and syndicate on your own terms.'),
    ('07-indieweb-standards', 'IndieWeb standards', 'Microformats, Webmentions, IndieAuth and other optional tools.'),
    ('08-community', 'Community & connections', 'Find meetups, blogrolls, webrings and other people.'),
    ('09-care-for-your-site', 'Care for your site', 'Privacy, accessibility, backups and keeping your site alive.'),
    ('10-blogging-and-microblogging', 'Blogging & microblogging', 'Discover blogs, short notes, digital gardens and more.'),
    ('11-three-ways-to-start', 'Three ways to start', 'Compare Neocities, Nekoweb and Bear Blog.'),
    ('12-decentralized-social', 'Decentralized social media', 'Explore Mastodon, Pixelfed, Bluesky, Lemmy and open protocols.'),
    ('13-discovery', 'Discover the small web', 'Marginalia, Wiby, directories and the joy of browsing.'),
    ('14-personal-web-toolkit', 'Personal web toolkit', 'Guestbooks, web buttons, image galleries, contact forms and more.'),
]

def esc(text):
    return html.escape(text, quote=True)

def frame(title, desc, page, content, section=''):
    nav = [('index.html','Home'),('guide.html','Guide'),('resources.html','Resources'),('inspiration.html','Inspiration')]
    links = ''.join(f'<a href="{url}"'+(' aria-current="page"' if page == url or section == url else '')+f'>{label}</a>' for url,label in nav)
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{esc(title)} | Join the IndieWeb</title><meta name="description" content="{esc(desc)}"><link rel="icon" href="favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="style.css"><script src="site.js" defer></script></head>
<body><a class="skip" href="#main">Skip to content</a><header class="masthead"><div class="wrap"><a class="brand" href="index.html"><img src="favicon.svg" alt="">Join the IndieWeb</a><nav aria-label="Main navigation">{links}<button class="theme" type="button" data-toggle-theme aria-label="Switch color theme">☾</button></nav></div></header>
<main id="main">{content}</main><footer class="foot"><div class="wrap"><p>Made for people who make the web. <br>Independent guide • CC BY 4.0</p><p><a href="https://github.com/kauz-hub/join-the-indieweb">GitHub repository</a><a href="contributing.html">Contribute</a><a href="license.html">License</a><a href="https://indieweb.org/">IndieWeb wiki</a></p></div></footer></body></html>'''

def card(i):
    slug,title,desc=CHAPTERS[i-1]
    return f'<article class="card" data-chapter><span class="num">CHAPTER {i:02}</span><h3>{esc(title)}</h3><p>{esc(desc)}</p><a href="{slug}.html">Read chapter</a></article>'

def save(name, title, desc, body, section=''):
    (DOCS/name).write_text(frame(title, desc, name, body, section), encoding='utf-8')

home = '''<div class="wrap"><section class="hero"><div><p class="eyebrow">✳ A field guide to the independent web</p><h1>The web is yours<br>to make.</h1><p>Create a little corner of the internet you can call your own. Write, share, explore and connect, without having to build an audience or learn everything at once.</p><div class="actions"><a class="pill" href="01-what-is-the-indieweb.html">Start here</a><a class="pill secondary" href="guide.html">Browse the guide</a></div><p class="mono" style="font-size:.85rem">Free to read. No accounts. No tracking.</p></div>
<div class="browser" aria-label="Illustration of a personal homepage"><div class="browserhead"><b>my little website</b><span aria-hidden="true">− □ ×</span></div><div class="browserbody"><div class="address">https://example.com/</div><div class="minihero"><div><strong>hello, web!</strong><p>Welcome to my little corner of cyberspace.</p></div><svg viewBox="0 0 100 100" role="presentation"><rect x="4" y="4" width="92" height="92" rx="3" fill="#e4eddb"/><path d="M50 80V47C50 28 72 18 90 18 85 39 72 53 50 53M50 63C23 63 11 43 14 21 38 23 50 40 50 63" fill="#89b97e" stroke="#276345" stroke-width="2.5" stroke-linejoin="round"/><path d="M50 60 25 35m25 15 27-22" stroke="#276345" stroke-width="2" fill="none"/><circle cx="76" cy="76" r="8" fill="#f2d775"/></svg></div><div class="minirow"><span class="minilink">about</span><span class="minilink">journal</span><span class="minilink">blogroll</span><span class="minilink">guestbook</span></div><div class="minipost"><small>MY FIRST POST</small>I finally made a website. It's a work in progress, and that's okay.</div><small class="mono" style="color:var(--muted)">✿ handmade with HTML · illustration</small></div></div></section>
<section class="section"><div class="sectionhead"><div><p class="eyebrow">Find your starting point</p><h2>There's more than one way in.</h2></div><p>Pick what you want to do today.</p></div><div class="cards">'''+card(1)+card(11)+card(10)+card(4)+card(12)+card(13)+'''</div></section>
<section class="banner"><div><p class="eyebrow">A little progress is enough</p><h2>Your first hour</h2><p>You don't need a perfect website. You just need somewhere to begin. This little checklist stays on your device.</p><a href="05-build-your-site.html">More ideas for your personal site</a></div><div class="checklist"><label><input type="checkbox" data-check="1">Choose a blog or website host.</label><label><input type="checkbox" data-check="2">Publish a short introduction.</label><label><input type="checkbox" data-check="3">Write something or share a favorite link.</label><label><input type="checkbox" data-check="4">Visit another personal website.</label><label><input type="checkbox" data-check="5">Save a backup of your work.</label></div></section>
<section class="section"><div class="sectionhead"><div><p class="eyebrow">Keep exploring</p><h2>Meet the people behind the web.</h2></div></div><div class="cards"><article class="card"><h3>Resource directory</h3><p>Tools, reading, learning resources, services and standards in one place.</p><a href="resources.html">Explore resources</a></article><article class="card"><h3>Real personal websites</h3><p>Discover creative homepages, diaries, galleries and blogs.</p><a href="inspiration.html">Find inspiration</a></article><article class="card"><h3>Follow a few blogs</h3><p>Learn how RSS, blogrolls and syndication help build a connected web.</p><a href="06-publishing-and-feeds.html">Try reading feeds</a></article></div></section></div>'''
save('index.html','A field guide','A practical guide to making your own corner of the independent web.',home)

groups = [('Start small',[1,2,11,3]),('Make and publish',[4,5,10,6]),('Connect & explore',[7,8,12,13]),('Keep it going',[9,14])]
guide = '<div class="wrap"><header class="subhero"><p class="eyebrow">The handbook</p><h1>Explore the guide.</h1><p>Fourteen chapters, from your first homepage to feeds, decentralized networks, and the standards that connect independent sites. Read in any order.</p></header><div class="filterbox"><label for="filter">Find a chapter</label><input id="filter" type="search" data-filter placeholder="Try RSS or Bear Blog"><output data-count aria-live="polite">14 chapters</output></div><p class="no-results" data-empty hidden>No matching chapters. Try a shorter search.</p>'
for title, inds in groups:
    guide += f'<section class="group" data-group><h2>{esc(title)}</h2><div class="cards">'+''.join(card(i) for i in inds)+'</div></section>'
guide += '</div>'
save('guide.html','Guide','Browse all fourteen chapters of the IndieWeb handbook.',guide)

def convert(md):
    text = md.read_text(encoding='utf-8')
    # The shared site navigation replaces the original Markdown navigation line.
    text = re.sub(r'^\[(?:Home|Back to the guide)\]\([^\n]+\n', '', text, flags=re.M)
    markup = subprocess.run(['pandoc','--from=gfm','--to=html5','--wrap=none','--no-highlight'],input=text,text=True,check=True,capture_output=True).stdout
    def replace_link(m):
        href=m[1]
        if href.startswith(('http:', 'https:', 'mailto:','#')): return m[0]
        path, _, fragment = href.partition('#')
        name=Path(path).name
        names={'README.md':'index.html','RESOURCES.md':'resources.html','INSPIRATION.md':'inspiration.html','CONTRIBUTING.md':'contributing.html','LICENSE.md':'license.html'}
        if name.endswith('.md'):
            href=names.get(name,Path(name).stem+'.html')+('#'+fragment if fragment else '')
        return f'href="{href}"'
    markup = re.sub(r'href="([^"]+)"',replace_link,markup)
    markup = markup.replace('<table>', '<div class="table-wrap"><table>').replace('</table>', '</table></div>')
    return markup

def sidebar(current):
    out='<aside class="sidebar" aria-label="Chapter navigation"><h2>In the guide</h2><a href="guide.html">All chapters</a>'
    for i,(slug,title,_) in enumerate(CHAPTERS,1):
        out += f'<a href="{slug}.html"'+(' aria-current="page"' if current==slug+'.html' else '')+f'>{i:02} · {esc(title)}</a>'
    return out+'</aside>'

for idx,(slug,title,desc) in enumerate(CHAPTERS):
    name=slug+'.html'
    article=convert(ROOT/'guides'/(slug+'.md'))
    prev = f'<a href="{CHAPTERS[idx-1][0]}.html">Previous chapter</a>' if idx else '<a href="guide.html">All chapters</a>'
    nxt = f'<a href="{CHAPTERS[idx+1][0]}.html">Next chapter</a>' if idx+1<len(CHAPTERS) else '<a href="resources.html">Resource directory</a>'
    body=f'<div class="wrap reading">{sidebar(name)}<article class="article"><p class="eyebrow">Chapter {idx+1:02} · Field guide</p>{article}<nav class="chapter-nav" aria-label="Chapter navigation">{prev}{nxt}</nav></article></div>'
    save(name,title,desc,body,'guide.html')

for md,name,title in [('RESOURCES.md','resources.html','Resource directory'),('INSPIRATION.md','inspiration.html','Personal website inspiration'),('CONTRIBUTING.md','contributing.html','Contribute'),('LICENSE.md','license.html','License')]:
    body='<div class="wrap reading">'+sidebar(name)+'<article class="article">'+convert(ROOT/md)+'</article></div>'
    save(name,title,title+' for the independent web.',body)
