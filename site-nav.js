/* Lightweight navbar wiring for all pages */
(function () {
  try {
    var header = document.getElementById('site-header');
    if (!header || header.dataset.navWired === 'true') return;
    header.dataset.navWired = 'true';

    var btn = document.getElementById('mobile-menu-button');
    var menu = document.getElementById('mobile-menu');

    if (btn && menu) {
      btn.addEventListener('click', function () {
        menu.classList.toggle('open');
      });

      // Close mobile menu when a link is clicked
      var links = menu.querySelectorAll('a');
      for (var i = 0; i < links.length; i++) {
        links[i].addEventListener('click', function () {
          menu.classList.remove('open');
        });
      }
    }

    function updateStickyHeader() {
      if (window.pageYOffset > 10) {
        header.classList.add('sticky-nav');
      } else {
        header.classList.remove('sticky-nav');
      }
    }

    window.addEventListener('scroll', updateStickyHeader);
    window.addEventListener('load', updateStickyHeader);
  } catch (e) {
    // no-op: avoid breaking page if something unexpected occurs
  }
})();


