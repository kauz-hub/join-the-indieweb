const root = document.documentElement;
const theme = document.querySelector('[data-toggle-theme]');
let saved;
try { saved = localStorage.getItem('indieweb-theme'); } catch {}
function setTheme(value) {
  root.dataset.theme = value;
  if (theme) {
    theme.textContent = value === 'dark' ? '☀' : '☾';
    theme.setAttribute('aria-label', value === 'dark' ? 'Switch to light theme' : 'Switch to dark theme');
  }
}
setTheme(saved === 'dark' || saved === 'light' ? saved : (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'));
theme?.addEventListener('click', () => {const value = root.dataset.theme === 'dark' ? 'light' : 'dark'; setTheme(value);try { localStorage.setItem('indieweb-theme',value); } catch {}});
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
