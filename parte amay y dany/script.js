const navToggle = document.querySelector('.nav-toggle');
const navMenu = document.getElementById('nav-menu');
const navItems = document.querySelectorAll('.nav-item');

navToggle.addEventListener('click', () => {
  const expanded = navToggle.getAttribute('aria-expanded') === 'true' || false;
  navToggle.setAttribute('aria-expanded', !expanded);
  navToggle.classList.toggle('open');
  navMenu.classList.toggle('open');
});

// Funcionalidad dropdown menú
navItems.forEach(item => {
  const btn = item.querySelector('.dropbtn');
  btn.addEventListener('click', e => {
    const isOpen = item.classList.contains('open');
    closeAllDropdowns();
    if (!isOpen) {
      item.classList.add('open');
      btn.setAttribute('aria-expanded', 'true');
    } else {
      item.classList.remove('open');
      btn.setAttribute('aria-expanded', 'false');
    }
  });
});

// Cerrar dropdowns cuando haces click afuera
document.addEventListener('click', e => {
  if (!e.target.closest('.nav-item')) {
    closeAllDropdowns();
  }
});

// Función para cerrar todos dropdowns
function closeAllDropdowns() {
  navItems.forEach(item => {
    item.classList.remove('open');
    const btn = item.querySelector('.dropbtn');
    if (btn) btn.setAttribute('aria-expanded', 'false');
  });
}

// Mostrar secciones y ocultar menú móvil al seleccionar opción
const sections = document.querySelectorAll('main section');

function showSection(id) {
  sections.forEach(sec => {
    if (sec.id === id) {
      sec.classList.remove('hidden');
    } else {
      sec.classList.add('hidden');
    }
  });
  // Cerrar menú y dropdowns (útil en móvil)
  navMenu.classList.remove('open');
  navToggle.classList.remove('open');
  navToggle.setAttribute('aria-expanded', 'false');
  closeAllDropdowns();
}
