const navToggle = document.querySelector('.nav-toggle');
const navMenu = document.getElementById('nav-menu');
const navItems = document.querySelectorAll('.nav-item');

// Menú hamburguesa (móvil)
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

// Cierra todos los dropdowns
function closeAllDropdowns() {
  navItems.forEach(item => {
    item.classList.remove('open');
    const btn = item.querySelector('.dropbtn');
    if (btn) btn.setAttribute('aria-expanded', 'false');
  });
}

// Muestra la sección correspondiente sin ocultar el resultado
const sections = document.querySelectorAll('main section');

function showSection(id) {
  sections.forEach(sec => {
    // Mantenemos visible la sección seleccionada Y la de resultado
    if (sec.id === id || sec.id === "resultado") {
      sec.classList.remove('hidden');
    } else {
      // Ocultamos las demás
      if (sec.id !== "resultado") {
        sec.classList.add('hidden');
      }
    }
  });

  // Cerrar menú móvil y dropdowns
  navMenu.classList.remove('open');
  navToggle.classList.remove('open');
  navToggle.setAttribute('aria-expanded', 'false');
  closeAllDropdowns();
}
