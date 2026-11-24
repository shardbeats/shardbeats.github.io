# Tutoriales SEO con video base Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Crear la sección `/tutoriales/` ES+EN con índice + guía piloto `fl-studio-ia` basada en tu video de ChatGPT.

**Architecture:** HTML estático copiando el patrón `web-tools/` (nav + styles + consent + footer). Índice tipo cards, guía tipo landing (hero + embed youtube-nocookie responsive + pasos + FAQ + CTA). JSON-LD HowTo + VideoObject por guía.

**Tech Stack:** HTML/CSS estático, youtube-nocookie embed, JSON-LD, GTM-NMVJZ8VL, Search Console.

**Spec:** `docs/superpowers/specs/2026-11-24-tutoriales-design.md`

## Global Constraints

- Sitio estático, sin build; copiar patrón `web-tools/` (nav, styles, consent, footer).
- ES+EN siempre, con canonical + alternate hreflang es/en/x-default.
- GTM `GTM-NMVJZ8VL` + consent banner `sb-consent` en cada página (default denied).
- Footer: `Shard Btmkr + canal y sitio ShardBeats + CC BY-NC-SA 4.0` con link a creativecommons.
- Apps TRAKK SUITE son `GPL-3.0-only` (no decir MIT salvo nota versiones pre-2026-11-23).
- No romper URLs existentes bajo `shardbeats.github.io/`.
- Video base piloto: YouTube `wC4Sxo0tQrs` (ChatGPT progresiones), embed `https://www.youtube-nocookie.com/embed/wC4Sxo0tQrs`.
- Títulos = queries exactas: `FL Studio con IA`, `partes de un beat`, etc.

## Review Focus

- Embed bloqueado por privacy/adblock deja página sin video visible — se espera fallback link "Ver en YouTube".
- hreflang/canonical cruzados mal puestos causan duplicado ES/EN — se espera alternates recíprocos exactos.
- GTM o consent duplicado/ausente rompe medición — se espera un solo GTM + un banner por página.
- Layout móvil del embed 16:9 se desborda — se espera embed responsive sin scroll horizontal a 360px.
- Sitemap sin las 4 URLs nuevas deja guías sin descubrir — se espera root sitemap con 4 loc + alternates.

---

### Task 1: Scaffold índice /tutoriales/ ES+EN

**Files:**
- Create: `tutoriales/index.html`
- Create: `tutoriales/en/index.html`
- Create: `tutoriales/styles.css` (copia de `web-tools/styles.css`)
- Test: verificación por `grep`/`shell` (no hay pytest en este repo estático)

**Interfaces:**
- Consumes: patrón `web-tools/index.html:62-101` (nav + hero + tool-grid + footer), `web-tools/styles.css`, footer ES/EN del spec.
- Produces: rutas `/tutoriales/`, `/tutoriales/en/` con nav cruzada; cards con links a `/tutoriales/fl-studio-ia/` (placeholder 404 hasta Task 2 permitido).

- [ ] **Step 1: Write the failing check**

```bash
# debe fallar: archivos no existen aún
test -f tutoriales/index.html -a -f tutoriales/en/index.html
```

- [ ] **Step 2: Run check to verify it fails**

Run: `test -f tutoriales/index.html -a -f tutoriales/en/index.html; echo $?`
Expected: `1` (FAIL, no existen)

- [ ] **Step 3: Implement `tutoriales/index.html` + `en/index.html` + `styles.css`**

Copiar `web-tools/index.html` como base. Cambiar: `lang`, `title` = `Tutoriales para beatmakers: FL Studio, mezcla y SP-404 | ShardBeats`, `description` con `fl studio ia, partes de un beat, cuantizar`, canonical `https://shardbeats.github.io/tutoriales/` y `/en/`, hreflang recíproco, nav con `TRAKK SUITE / Pack gratis / EN|ES / Tutoriales activo`, hero eyebrow `ShardBeats · Tutoriales`, grid con 3 cards (FL Studio con IA → `fl-studio-ia/`, Partes de un beat → `#`, Cuantizar → `#`), footer spec ES/EN, GTM + consent idéntico a web-tools.

- [ ] **Step 4: Run checks to verify it passes**

Run:
```bash
test -f tutoriales/index.html -a -f tutoriales/en/index.html -a -f tutoriales/styles.css && echo FILES_OK
grep -q "GTM-NMVJZ8VL" tutoriales/index.html && grep -q "sb-consent" tutoriales/index.html && echo CONSENT_OK
grep -q "canal y sitio ShardBeats" tutoriales/index.html && grep -q "ShardBeats channel & site" tutoriales/en/index.html && echo FOOTER_OK
grep -q 'hreflang="en" href="https://shardbeats.github.io/tutoriales/en/"' tutoriales/index.html && echo HREFLANG_OK
```
Expected: `FILES_OK CONSENT_OK FOOTER_OK HREFLANG_OK`

- [ ] **Step 5: Commit**

```bash
git add tutoriales/index.html tutoriales/en/index.html tutoriales/styles.css
git commit -m "feat(tutoriales): scaffold indice ES+EN"
```

### Task 2: Guía piloto fl-studio-ia ES+EN con video base

**Files:**
- Create: `tutoriales/fl-studio-ia/index.html`
- Create: `tutoriales/en/fl-studio-ia/index.html`
- Test: `grep` checks + apertura manual en browser

**Interfaces:**
- Consumes: índice Task 1 (links), video `wC4Sxo0tQrs`, patrón embed `landing/index.html:241-243` (youtube-nocookie responsive).
- Produces: rutas `/tutoriales/fl-studio-ia/` ES+EN con HowTo + VideoObject y CTA a `/tools/`.

- [ ] **Step 1: Write the failing check**

```bash
test -f tutoriales/fl-studio-ia/index.html -a -f tutoriales/en/fl-studio-ia/index.html
```

- [ ] **Step 2: Run check to verify it fails**

Run: `test -f tutoriales/fl-studio-ia/index.html -a -f tutoriales/en/fl-studio-ia/index.html; echo $?`
Expected: `1`

- [ ] **Step 3: Implement `tutoriales/fl-studio-ia/index.html` en ES**

Título exacto `FL Studio con IA: progresiones de acordes con ChatGPT | ShardBeats`. 400-600 palabras, pasos: 1) idea en FL, 2) prompt a ChatGPT, 3) pasar a Piano Roll, 4) cuantizar/humanizar, 5) exportar y preparar con TRAKKCONVERTER. Embed `https://www.youtube-nocookie.com/embed/wC4Sxo0tQrs` responsive + fallback `<a href="https://www.youtube.com/watch?v=wC4Sxo0tQrs">`. JSON-LD `HowTo` (steps) + `VideoObject` (embedUrl, thumbnail `https://i.ytimg.com/vi/wC4Sxo0tQrs/hqdefault.jpg`). FAQ con `fl studio ia`, `ia fl studio`, `fl ia`. CTA a `/tools/trakkconverter/` y `/tools/`. GTM + consent + footer ES.

- [ ] **Step 4: Implement `tutoriales/en/fl-studio-ia/index.html` en EN**

Traducción directa del ES. Canonical `/tutoriales/en/fl-studio-ia/`, hreflang recíproco, footer EN, mismo embed y schema en inglés.

- [ ] **Step 5: Run checks to verify it passes**

Run:
```bash
grep -q "youtube-nocookie.com/embed/wC4Sxo0tQrs" tutoriales/fl-studio-ia/index.html && echo EMBED_OK
grep -q "watch?v=wC4Sxo0tQrs" tutoriales/fl-studio-ia/index.html && echo FALLBACK_OK
grep -q '"@type": "HowTo"' tutoriales/fl-studio-ia/index.html && grep -q '"@type": "VideoObject"' tutoriales/fl-studio-ia/index.html && echo SCHEMA_OK
grep -q "trakkconverter" tutoriales/fl-studio-ia/index.html && echo CTA_OK
```
Expected: `EMBED_OK FALLBACK_OK SCHEMA_OK CTA_OK` (repetir para `en/`)

- [ ] **Step 6: Commit**

```bash
git add tutoriales/fl-studio-ia/index.html tutoriales/en/fl-studio-ia/index.html
git commit -m "feat(tutoriales): guia piloto fl-studio-ia ES+EN con video wC4Sxo0tQrs"
```

### Task 3: Hub + sitemap wiring

**Files:**
- Modify: `index.html` (agregar botón Tutoriales)
- Modify: `en/index.html`
- Modify: `sitemap.xml` (4 URLs nuevas)
- Test: `grep` checks

**Interfaces:**
- Consumes: botones hub `index.html:108-112`, root `sitemap.xml:1-53` (sin hreflang, solo loc).
- Produces: hub enlaza `/tutoriales/`, sitemap incluye índice + guía ES+EN.

- [ ] **Step 1: Write the failing check**

```bash
grep -q "tutoriales/" index.html && grep -q "tutoriales/" sitemap.xml && echo WIRED || echo NOT_WIRED
```

- [ ] **Step 2: Run check to verify it fails**

Run: `grep -q "tutoriales/" index.html && grep -q "tutoriales/" sitemap.xml && echo WIRED || echo NOT_WIRED`
Expected: `NOT_WIRED`

- [ ] **Step 3: Implement hub links en `index.html` y `en/index.html`**

En `div.row` junto a TRAKK SUITE / Pack / Web tools agregar `<a class="btn ghost" href="tutoriales/">Tutoriales</a>` (ES) y `tutorials` (EN, href `../tutoriales/en/` relativo según patrón existente). No tocar GTM/consent/footer.

- [ ] **Step 4: Implement `sitemap.xml` con 4 URLs**

Agregar tras `web-tools/metronome/`: `tutoriales/` (0.9 weekly), `tutoriales/fl-studio-ia/` (0.8 monthly), `tutoriales/en/` (0.8), `tutoriales/en/fl-studio-ia/` (0.7). Formato igual al existente (loc + changefreq + priority, sin hreflang en root).

- [ ] **Step 5: Run checks to verify it passes**

Run:
```bash
grep -q 'href="tutoriales/"' index.html && echo HUB_ES_OK
grep -q "tutoriales" en/index.html && echo HUB_EN_OK
grep -c "tutoriales" sitemap.xml
```
Expected: `HUB_ES_OK HUB_EN_OK` y conteo `4`

- [ ] **Step 6: Commit**

```bash
git add index.html en/index.html sitemap.xml
git commit -m "feat(tutoriales): wiring hub + sitemap"
```

### Task 4: QA final y push

**Files:**
- Modify: ninguno (solo verificación; fix solo si falla)
- Test: suite de `grep` + inspección visual con browser

**Interfaces:**
- Consumes: todo lo de Task 1-3.
- Produces: rama lista para push, sin 404 internos.

- [ ] **Step 1: Run link integrity check (debe pasar)**

Run:
```bash
grep -rho 'href="[^"]*"' tutoriales/ index.html | sort -u
python tools/scripts/sync_versions.py 2>&1 | tail -2
```
Expected: ningún `href` a `fl-studio-ia` roto; `sync_versions.py` no toca `tutoriales/` (solo tools).

- [ ] **Step 2: Run SEO/consent audit (debe pasar)**

Run:
```bash
for f in tutoriales/index.html tutoriales/en/index.html tutoriales/fl-studio-ia/index.html tutoriales/en/fl-studio-ia/index.html; do echo "== $f"; grep -q "GTM-NMVJZ8VL" "$f" && echo -n "GTM_OK "; grep -q 'id="consent-banner"' "$f" && echo -n "BANNER_OK "; grep -q "creativecommons.org/licenses/by-nc-sa" "$f" && echo "LICENSE_OK" || echo "LICENSE_MISS"; done
```
Expected: 4 líneas con `GTM_OK BANNER_OK LICENSE_OK`

- [ ] **Step 3: Visual check en browser (manual)**

Abrir con browse `tutoriales/` y `tutoriales/fl-studio-ia/`, snapshot + screenshot a 360px y desktop. Se espera: nav legible, embed 16:9 sin scroll horizontal, CTA visible.
Test de Review Focus: con embed bloqueado debe verse el fallback "Ver en YouTube".

- [ ] **Step 4: Push (solo tras OK de pasos 1-3)**

```bash
git log --oneline -4
git push
```
Expected: push `main -> main` sin rebase pendiente.
