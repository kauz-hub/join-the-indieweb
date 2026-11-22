const root = document.documentElement;
const theme = document.querySelector('[data-toggle-theme]');
function setTheme(value) {
  root.dataset.theme = value;
  document.querySelectorAll('meta[name="theme-color"]').forEach(meta => {
    meta.content = value === 'dark' ? '#17251e' : '#f7f7ed';
  });
  if (theme) {
    theme.textContent = value === 'dark' ? 'Light' : 'Dark';
    theme.setAttribute('aria-label', value === 'dark' ? 'Switch to light theme' : 'Switch to dark theme');
  }
}
// The inline head script has already set the theme; don't reset it at DOM ready.
if (root.dataset.theme !== 'dark' && root.dataset.theme !== 'light') {
  let preference;
  try { preference = localStorage.getItem('indieweb-theme'); } catch {}
  if (preference !== 'dark' && preference !== 'light') {
    try { preference = sessionStorage.getItem('indieweb-theme'); } catch {}
  }
  if (preference !== 'dark' && preference !== 'light') {
    preference = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }
  setTheme(preference);
} else {
  setTheme(root.dataset.theme);
}
theme?.addEventListener('click', () => {
  const value = root.dataset.theme === 'dark' ? 'light' : 'dark';
  setTheme(value);
  try { localStorage.setItem('indieweb-theme',value); } catch {}
  try { sessionStorage.setItem('indieweb-theme',value); } catch {}
});
document.querySelectorAll('[data-check]').forEach(input => {
  const key = 'indieweb-check-' + input.dataset.check;
  try { input.checked = localStorage.getItem(key) === 'true'; } catch {}
  input.addEventListener('change', () => {try { localStorage.setItem(key,String(input.checked)); } catch {}});
});
const search = document.querySelector('[data-filter]');
if (search) {
  const cards = [...document.querySelectorAll('[data-chapter]')];
  const groups = [...document.querySelectorAll('[data-group]')];
  const count = document.querySelector('[data-count]');
  const empty = document.querySelector('[data-empty]');
  function filter() {
    const q = search.value.trim().toLowerCase();
    let n = 0;
    cards.forEach(card => {card.hidden = !card.textContent.toLowerCase().includes(q); if (!card.hidden) n++;});
    groups.forEach(group => group.hidden = ![...group.querySelectorAll('[data-chapter]')].some(c => !c.hidden));
    count.textContent = `${n} ${n === 1 ? 'chapter' : 'chapters'}`;
    empty.hidden = n !== 0;
  }
  search.addEventListener('input',filter);
  filter();
}
