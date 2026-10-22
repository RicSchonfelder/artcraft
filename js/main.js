/* JS comum para os sites de repos — null-safe (elementos opcionais) */
(() => {
  "use strict";
  const $  = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => [...c.querySelectorAll(s)];

  /* foco de accent por repo (classe h-NN no body define --acc via CSS) */

  /* tema */
  const html = document.documentElement;
  const sys = matchMedia("(prefers-color-scheme: light)").matches ? "light" : "dark";
  const forced = new URLSearchParams(location.search).get("theme");
  html.dataset.theme = forced === "light" || forced === "dark" ? forced : (localStorage.getItem("mdv-theme") || sys);

  let toastT;
  const toast = msg => {
    const t = $("#toast"); if (!t) return;
    t.textContent = msg; t.classList.add("is-show");
    clearTimeout(toastT);
    toastT = setTimeout(() => t.classList.remove("is-show"), 2200);
  };
  window.__toast = toast;

  const themeBtn = $("#theme-toggle");
  if (themeBtn) themeBtn.addEventListener("click", () => {
    html.dataset.theme = html.dataset.theme === "dark" ? "light" : "dark";
    localStorage.setItem("mdv-theme", html.dataset.theme);
    toast(html.dataset.theme === "light" ? "Tema: claro ☀️" : "Tema: escuro 🌙");
  });

  /* nav */
  const nav = $("#nav");
  if (nav) addEventListener("scroll", () => nav.classList.toggle("is-scrolled", scrollY > 8), { passive: true });

  const menuBtn = $("#menu-btn"), mobileMenu = $("#mobile-menu");
  if (menuBtn && mobileMenu) {
    menuBtn.addEventListener("click", () => {
      const open = mobileMenu.classList.toggle("is-open");
      menuBtn.setAttribute("aria-expanded", String(open));
    });
    $$("a", mobileMenu).forEach(a => a.addEventListener("click", () => mobileMenu.classList.remove("is-open")));
  }

  /* scroll-spy */
  const navLinks = $$("#nav-links a");
  if (navLinks.length) {
    const sections = $$("main section[id]");
    addEventListener("scroll", () => {
      let cur = "";
      sections.forEach(s => { if (scrollY >= s.offsetTop - 140) cur = s.id; });
      navLinks.forEach(a => a.classList.toggle("is-active", a.getAttribute("href") === `#${cur}`));
    }, { passive: true });
  }

  /* copy */
  $$(".copy-btn").forEach(btn => btn.addEventListener("click", async () => {
    const codeEl = btn.closest(".codebox__body") && btn.closest(".codebox__body").querySelector("code");
    const text = codeEl ? codeEl.textContent : "";
    try { await navigator.clipboard.writeText(text); }
    catch (_) {
      const ta = document.createElement("textarea");
      ta.value = text; document.body.appendChild(ta);
      ta.select(); document.execCommand("copy"); ta.remove();
    }
    const label = btn.querySelector("span");
    const prev = label.textContent;
    btn.classList.add("is-copied"); label.textContent = "Copiado!";
    toast("Copiado!");
    setTimeout(() => { btn.classList.remove("is-copied"); label.textContent = prev; }, 1800);
  }));

  /* reveal + stagger */
  const io = new IntersectionObserver(entries => {
    entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add("is-in"); io.unobserve(e.target); } });
  }, { threshold: .12 });
  $$(".reveal").forEach(el => io.observe(el));
  $$(".features, .stats, .stack").forEach(grid => {
    [...grid.children].forEach((child, i) => (child.style.transitionDelay = `${i * 60}ms`));
  });

  /* card spotlight */
  $$(".card").forEach(card => card.addEventListener("pointermove", e => {
    const r = card.getBoundingClientRect();
    card.style.setProperty("--mx", `${((e.clientX - r.left) / r.width) * 100}%`);
    card.style.setProperty("--my", `${((e.clientY - r.top) / r.height) * 100}%`);
  }));

  /* counters */
  const countIO = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (!e.isIntersecting) return;
      countIO.unobserve(e.target);
      const n = e.target, target = +n.dataset.count, suffix = n.dataset.suffix || "";
      const t0 = performance.now(), dur = 1100;
      const step = t => {
        const p = Math.min((t - t0) / dur, 1);
        n.textContent = Math.round(target * (1 - Math.pow(1 - p, 3))) + suffix;
        if (p < 1) requestAnimationFrame(step);
      };
      requestAnimationFrame(step);
    });
  }, { threshold: .5 });
  $$(".stat__n[data-count]").forEach(el => countIO.observe(el));
})();
