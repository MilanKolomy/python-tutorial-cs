(function () {
    "use strict";

    const THEME_KEY = "python-tutorial-cs-theme";
    const SCALE_KEY = "python-tutorial-cs-font-scale";
    const MIN_SCALE = 0.85;
    const MAX_SCALE = 1.30;
    const SCALE_STEP = 0.05;
    const MOBILE_BREAKPOINT = 800;

    function loadValue(key, fallback) {
        try {
            return window.localStorage.getItem(key) || fallback;
        } catch (_error) {
            return fallback;
        }
    }

    function saveValue(key, value) {
        try {
            window.localStorage.setItem(key, value);
        } catch (_error) {
            // Nastavení zůstane platné alespoň pro aktuální stránku.
        }
    }

    let theme = loadValue(THEME_KEY, "light");
    let scale = Number.parseFloat(loadValue(SCALE_KEY, "1"));

    if (theme !== "dark") {
        theme = "light";
    }
    if (!Number.isFinite(scale)) {
        scale = 1;
    }
    scale = Math.min(MAX_SCALE, Math.max(MIN_SCALE, scale));

    function applyPreferences() {
        document.documentElement.dataset.readerTheme = theme;
        document.documentElement.style.setProperty(
            "--reader-font-scale",
            scale.toFixed(2)
        );
    }

    applyPreferences();

    function createButton(className, label, text) {
        const button = document.createElement("button");
        button.type = "button";
        button.className = className;
        button.setAttribute("aria-label", label);
        button.title = label;
        button.textContent = text;
        return button;
    }

    function createNavigationLink(relation, label, arrow) {
        const source = document.querySelector(`head link[rel="${relation}"]`);
        const link = document.createElement("a");
        link.className = `reader-controls__nav-link reader-controls__${relation} reader-controls__mobile`;

        const arrowElement = document.createElement("span");
        arrowElement.setAttribute("aria-hidden", "true");
        arrowElement.textContent = arrow;
        const labelElement = document.createElement("span");
        labelElement.className = "reader-controls__nav-label";
        labelElement.textContent = label;
        if (relation === "next") {
            link.append(labelElement, arrowElement);
        } else {
            link.append(arrowElement, labelElement);
        }

        if (source) {
            link.href = source.href;
            const targetTitle = source.title ? `: ${source.title}` : "";
            link.setAttribute("aria-label", `${label}${targetTitle}`);
            link.title = `${label}${targetTitle}`;
        } else {
            link.setAttribute("aria-disabled", "true");
            link.setAttribute("aria-label", `${label} není k dispozici`);
        }

        return link;
    }

    function initializeControls() {
        if (document.querySelector(".reader-controls")) {
            return;
        }

        const controls = document.createElement("div");
        controls.className = "reader-controls";
        controls.setAttribute("role", "group");
        controls.setAttribute("aria-label", "Nastavení čtení");

        const themeButton = createButton(
            "reader-controls__theme",
            "Přepnout na tmavé téma",
            "☾"
        );
        const separator = document.createElement("span");
        separator.className = "reader-controls__separator";
        separator.setAttribute("aria-hidden", "true");
        const smallerButton = createButton(
            "reader-controls__smaller",
            "Zmenšit text",
            "A−"
        );
        const largerButton = createButton(
            "reader-controls__larger",
            "Zvětšit text",
            "A+"
        );
        const navigationSeparator = document.createElement("span");
        navigationSeparator.className = "reader-controls__separator reader-controls__mobile";
        navigationSeparator.setAttribute("aria-hidden", "true");
        const previousLink = createNavigationLink("prev", "Předchozí", "‹");
        const nextLink = createNavigationLink("next", "Další", "›");
        const menuSeparator = document.createElement("span");
        menuSeparator.className = "reader-controls__separator reader-controls__mobile";
        menuSeparator.setAttribute("aria-hidden", "true");
        const menuButton = createButton(
            "reader-controls__menu reader-controls__mobile",
            "Otevřít navigaci",
            "☰"
        );
        menuButton.setAttribute("aria-expanded", "false");
        const status = document.createElement("span");
        status.className = "reader-status";
        status.setAttribute("aria-live", "polite");

        function updateControls(announce) {
            const dark = theme === "dark";
            themeButton.textContent = dark ? "☀" : "☾";
            themeButton.setAttribute(
                "aria-label",
                dark ? "Přepnout na světlé téma" : "Přepnout na tmavé téma"
            );
            themeButton.title = themeButton.getAttribute("aria-label");
            themeButton.setAttribute("aria-pressed", String(dark));
            smallerButton.disabled = scale <= MIN_SCALE;
            largerButton.disabled = scale >= MAX_SCALE;
            if (announce) {
                status.textContent = `Velikost textu ${Math.round(scale * 100)} %`;
            }
        }

        themeButton.addEventListener("click", function () {
            theme = theme === "dark" ? "light" : "dark";
            saveValue(THEME_KEY, theme);
            applyPreferences();
            updateControls(false);
        });

        smallerButton.addEventListener("click", function () {
            scale = Math.max(MIN_SCALE, scale - SCALE_STEP);
            saveValue(SCALE_KEY, scale.toFixed(2));
            applyPreferences();
            updateControls(true);
        });

        largerButton.addEventListener("click", function () {
            scale = Math.min(MAX_SCALE, scale + SCALE_STEP);
            saveValue(SCALE_KEY, scale.toFixed(2));
            applyPreferences();
            updateControls(true);
        });

        const sidebar = document.querySelector("div.sphinxsidebar");
        const mobileQuery = window.matchMedia(`(max-width: ${MOBILE_BREAKPOINT}px)`);

        if (sidebar) {
            if (!sidebar.id) {
                sidebar.id = "reader-mobile-navigation";
            }
            menuButton.setAttribute("aria-controls", sidebar.id);
        } else {
            menuButton.disabled = true;
        }

        function setMenuOpen(open, returnFocus) {
            const shouldOpen = Boolean(open && sidebar && mobileQuery.matches);
            document.body.classList.toggle("mobile-menu-open", shouldOpen);
            menuButton.setAttribute("aria-expanded", String(shouldOpen));
            menuButton.setAttribute(
                "aria-label",
                shouldOpen ? "Zavřít navigaci" : "Otevřít navigaci"
            );
            menuButton.title = menuButton.getAttribute("aria-label");
            menuButton.textContent = shouldOpen ? "×" : "☰";
            controls.classList.remove("reader-controls--hidden");

            if (shouldOpen) {
                const firstLink = sidebar.querySelector("a");
                if (firstLink) {
                    firstLink.focus({ preventScroll: true });
                }
            } else if (returnFocus) {
                menuButton.focus({ preventScroll: true });
            }
        }

        menuButton.addEventListener("click", function () {
            setMenuOpen(!document.body.classList.contains("mobile-menu-open"), false);
        });

        if (sidebar) {
            sidebar.addEventListener("click", function (event) {
                if (event.target.closest("a")) {
                    setMenuOpen(false, false);
                }
            });
        }

        document.addEventListener("keydown", function (event) {
            if (event.key === "Escape" && document.body.classList.contains("mobile-menu-open")) {
                setMenuOpen(false, true);
            }
        });

        mobileQuery.addEventListener("change", function (event) {
            if (!event.matches) {
                setMenuOpen(false, false);
                controls.classList.remove("reader-controls--hidden");
            }
        });

        let lastScrollY = window.scrollY;
        let scrollTicking = false;

        function updateBarFromScroll() {
            const currentScrollY = Math.max(0, window.scrollY);
            const delta = currentScrollY - lastScrollY;
            const menuOpen = document.body.classList.contains("mobile-menu-open");

            if (mobileQuery.matches && !menuOpen) {
                if (currentScrollY < 40 || delta < -6) {
                    controls.classList.remove("reader-controls--hidden");
                } else if (currentScrollY > 90 && delta > 6) {
                    controls.classList.add("reader-controls--hidden");
                }
            }

            lastScrollY = currentScrollY;
            scrollTicking = false;
        }

        window.addEventListener("scroll", function () {
            if (!scrollTicking) {
                window.requestAnimationFrame(updateBarFromScroll);
                scrollTicking = true;
            }
        }, { passive: true });

        controls.append(
            themeButton,
            separator,
            smallerButton,
            largerButton,
            navigationSeparator,
            previousLink,
            nextLink,
            menuSeparator,
            menuButton,
            status
        );
        document.body.appendChild(controls);
        updateControls(false);
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", initializeControls, { once: true });
    } else {
        initializeControls();
    }
})();
