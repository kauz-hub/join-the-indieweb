// Run with Node after regenerating the website: node test-theme.cjs
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const docs = path.join(__dirname, 'docs');
const script = fs.readFileSync(path.join(docs, 'site.js'), 'utf8');
const pages = fs.readdirSync(docs).filter(name => name.endsWith('.html'));
const cases = [
  ['dark', null, false, 'dark'], ['light', null, true, 'light'],
  [null, 'dark', false, 'dark'], [null, null, true, 'dark'],
  [null, null, false, 'light'], ['invalid', null, true, 'dark'],
  ['blocked', 'dark', false, 'dark'], ['blocked', 'blocked', true, 'dark'],
];
let tested = 0;
for (const name of pages) {
  const page = fs.readFileSync(path.join(docs, name), 'utf8');
  const head = page.match(/<head>([\s\S]+?)<\/head>/)[1];
  const boot = head.match(/<script>([\s\S]+?)<\/script>/)[1];
  assert(head.indexOf('<script>') < head.indexOf('rel="stylesheet"'), `${name}: theme must run before stylesheets`);
  assert(head.includes(':root[data-theme="dark"]'));
  assert(head.includes('prefers-color-scheme:dark'));
  for (const [local, session, systemDark, expected] of cases) {
    const storage = value => ({getItem() { if (value === 'blocked') throw Error('storage unavailable'); return value; }, setItem() {}});
    const root = {dataset: {}, setAttribute(key, value) { this.dataset.theme = value; }};
    const meta = [{}, {}];
    const button = {setAttribute() {}, addEventListener(type, fn) { this.click = fn; }};
    const context = vm.createContext({
      document: {documentElement: root, querySelectorAll(s) { return s.startsWith('meta') ? meta : []; }, querySelector(s) { return s === '[data-toggle-theme]' ? button : null; }},
      localStorage: storage(local), sessionStorage: storage(session), window: {matchMedia() { return {matches: systemDark}; }},
    });
    vm.runInContext(boot, context);
    assert.equal(root.dataset.theme, expected, name);
    assert.equal(meta[0].content, expected === 'dark' ? '#17251e' : '#f7f7ed');
    vm.runInContext(script, context);
    assert.equal(root.dataset.theme, expected, `${name}: deferred script must not change the initial theme`);
    button.click();
    assert.equal(root.dataset.theme, expected === 'dark' ? 'light' : 'dark');
    tested++;
  }
}
console.log(`${pages.length} pages; ${tested} theme initialization and toggle checks passed.`);
