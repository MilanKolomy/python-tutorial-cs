(function () {
    "use strict";

    const THEME_KEY = "python-tutorial-cs-theme";
    const SCALE_KEY = "python-tutorial-cs-font-scale";
    const MIN_SCALE = 0.85;
    const MAX_SCALE = 1.30;
    const SCALE_STEP = 0.05;

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

    function initializeControls() {
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

        controls.append(
            themeButton,
            separator,
            smallerButton,
            largerButton,
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
