/* Lightweight navbar wiring for all pages */
(function () {
  try {
    var header = document.getElementById('site-header');
    if (!header || header.dataset.navWired === 'true') return;
    header.dataset.navWired = 'true';

    var btn = document.getElementById('mobile-menu-button');
    var menu = document.getElementById('mobile-menu');
    var bottomBanner = document.getElementById('global-top-banner');

    function updateBottomBannerOffset() {
      var height = bottomBanner ? bottomBanner.offsetHeight : 0;
      document.documentElement.style.setProperty('--bottom-banner-height', height + 'px');
    }

    if (btn && menu) {
      btn.addEventListener('click', function () {
        menu.classList.toggle('open');
        btn.setAttribute('aria-expanded', menu.classList.contains('open'));
      });

      // Close mobile menu when a link is clicked
      var links = menu.querySelectorAll('a');
      for (var i = 0; i < links.length; i++) {
        links[i].addEventListener('click', function () {
          menu.classList.remove('open');
          btn.setAttribute('aria-expanded', 'false');
        });
      }
    }

    // Optimized sticky header with throttling to prevent forced reflows
    var ticking = false;
    var lastScrollTop = 0;
    
    function updateStickyHeader() {
      var scrollTop = window.pageYOffset || document.documentElement.scrollTop;
      
      // Only update if scroll position changed significantly (prevents unnecessary reflows)
      if (Math.abs(scrollTop - lastScrollTop) > 5) {
        if (scrollTop > 10) {
          header.classList.add('sticky-nav');
        } else {
          header.classList.remove('sticky-nav');
        }
        lastScrollTop = scrollTop;
      }
      ticking = false;
    }

    function requestTick() {
      if (!ticking) {
        requestAnimationFrame(updateStickyHeader);
        ticking = true;
      }
    }

    // Use passive scroll listener for better performance
    window.addEventListener('scroll', requestTick, { passive: true });
    window.addEventListener('resize', function () {
      updateBottomBannerOffset();
    });

    // Initial check on load
    window.addEventListener('load', function() {
      updateBottomBannerOffset();
      requestAnimationFrame(updateStickyHeader);
    });

    updateBottomBannerOffset();
    requestAnimationFrame(updateStickyHeader);
    
  } catch (e) {
    // no-op: avoid breaking page if something unexpected occurs
  }
})();
