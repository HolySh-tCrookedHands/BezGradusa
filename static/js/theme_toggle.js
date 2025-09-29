document.addEventListener('DOMContentLoaded', function () {
  const themeToggle = document.getElementById('theme-toggle');
  if (!themeToggle) return;

  function applyTheme(name) {
    if (name === 'light') {
      document.body.classList.add('light-theme');
      document.body.classList.add('neon-mode');
      // @ts-ignore
      themeToggle.textContent = '☀️';
      // @ts-ignore
      themeToggle.setAttribute('aria-pressed', 'true');
    } else {
      document.body.classList.remove('light-theme');
      document.body.classList.add('neon-mode');
      // @ts-ignore
      themeToggle.textContent = '🌙';
      // @ts-ignore
      themeToggle.setAttribute('aria-pressed', 'false');
    }
    localStorage.setItem('theme', name);
  }

  const saved = localStorage.getItem('theme');
  if (saved === 'light') applyTheme('light');
  else applyTheme('dark');

  themeToggle.addEventListener('click', () => {
    const isLight = document.body.classList.contains('light-theme');
    applyTheme(isLight ? 'dark' : 'light');
    themeToggle.style.transform = 'scale(0.96)';
    setTimeout(() => themeToggle.style.transform = '', 140);
  });
});
