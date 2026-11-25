# Tutoriales lote 3 (sp-404 mk2) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Sumar la guía `sp-404-mk2-preparar-samples` ES+EN (video `UAMboy8mtro`) y activarla en índice + sitemap para capturar `roland fl studio` + `sp 404 mk2`.

**Architecture:** HTML estático con el patrón de `tutoriales/fl-studio-ia` y lotes 1-2 ya en `main`: guía = hero + embed youtube-nocookie responsive + pasos + FAQ + CTA, JSON-LD HowTo + VideoObject. Índice y sitemap se extienden.

**Tech Stack:** HTML/CSS estático, youtube-nocookie embed, JSON-LD, GTM-NMVJZ8VL.

**Spec:** `docs/superpowers/specs/2026-11-24-tutoriales-lote3-design.md` (extiende specs lote 1 y 2)

## Global Constraints

- Sitio estático, sin build; copiar estructura de `tutoriales/fl-studio-ia/index.html` (lote 1 en `main`).
- ES+EN siempre, canonical + alternate hreflang es/en/x-default recíprocos.
- GTM `GTM-NMVJZ8VL` + consent banner `sb-consent` en cada página (default denied, uno solo de cada uno).
- Footer ES: `Shard Btmkr (Darío García) · canal y sitio ShardBeats · La Piedad, Mich. · <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" rel="license">Contenido del sitio: CC BY-NC-SA 4.0</a>`; EN: `Shard Btmkr (Dario Garcia) · ShardBeats channel & site · La Piedad, Mich. · <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" rel="license">Site content: CC BY-NC-SA 4.0</a>`.
- Apps TRAKK SUITE son `GPL-3.0-only` (cero menciones MIT).
- No romper URLs existentes. Archivos nuevos en UTF-8 estricto (verificar con `python -c "open(F,'rb').read().decode('utf-8')"`; mojibake de consola PowerShell es artefacto de display).
- Video: `UAMboy8mtro`; embed `https://www.youtube-nocookie.com/embed/UAMboy8mtro`; thumb `https://i.ytimg.com/vi/UAMboy8mtro/hqdefault.jpg`; watch `https://www.youtube.com/watch?v=UAMboy8mtro`.
- `uploadDate` del VideoObject: usar `2026-11-24` solo como fallback y reportarlo.

## Review Focus

- Embed bloqueado por privacy/adblock deja página sin video — se espera fallback "Ver en YouTube" / "Watch on YouTube" siempre visible bajo el video.
- hreflang/canonical cruzados mal puestos causan duplicado ES/EN — se espera alternates recíprocos exactos.
- GTM o consent duplicado/ausente rompe medición — se espera un solo GTM + un banner por página.
- Layout móvil del embed 16:9 se desborda — se espera embed responsive sin scroll horizontal a 360px.
- Ruta de links relativos mal calculada — se espera verificar cada `href` por profundidad (`tutoriales/X/` usa `../../`, `tutoriales/en/X/` usa `../../../` para raíz).

---

### Task 1: Guía sp-404-mk2-preparar-samples ES+EN

**Files:**
- Create: `tutoriales/sp-404-mk2-preparar-samples/index.html`
- Create: `tutoriales/en/sp-404-mk2-preparar-samples/index.html`
- Test: `grep`/`shell` + `python` UTF-8 decode

**Interfaces:**
- Consumes: patrón `tutoriales/fl-studio-ia/index.html`, video `UAMboy8mtro`.
- Produces: rutas `/tutoriales/sp-404-mk2-preparar-samples/` ES+EN con HowTo + VideoObject.

- [ ] **Step 1: Write the failing check**

```bash
test -f tutoriales/sp-404-mk2-preparar-samples/index.html -a -f tutoriales/en/sp-404-mk2-preparar-samples/index.html
```

- [ ] **Step 2: Run check to verify it fails**

Run: `test -f tutoriales/sp-404-mk2-preparar-samples/index.html -a -f tutoriales/en/sp-404-mk2-preparar-samples/index.html; echo $?`
Expected: `1`

- [ ] **Step 3: Implement `tutoriales/sp-404-mk2-preparar-samples/index.html` en ES**

Título exacto `SP-404 MK2: prepara tus samples en la SD rápido | ShardBeats`. 400-600 palabras: pasos SD / carpetas ROLAND/SP404 / WAV con TRAKKCONVERTER / copiar+importar / pitfalls. Queries literales: `roland fl studio`, `sp 404 mk2`, `preparar samples sp 404`. Embed responsive `UAMboy8mtro` + fallback `https://www.youtube.com/watch?v=UAMboy8mtro`. FAQ 3 (¿qué formato WAV necesita la SP-404MK2? / ¿qué estructura de carpetas? / ¿puedo convertir librerías completas?). CTA `../../tools/trakkconverter/` + `../../tools/`. HowTo 5 pasos + VideoObject (uploadDate `2026-11-24` fallback). Canonical `https://shardbeats.github.io/tutoriales/sp-404-mk2-preparar-samples/`, hreflang recíproco, nav `← Tutoriales` a `../`, GTM + consent + footer ES.

- [ ] **Step 4: Implement `tutoriales/en/sp-404-mk2-preparar-samples/index.html` en EN**

Traducción directa. Título `SP-404 MK2: prepare your samples on the SD card fast | ShardBeats`. Links raíz `../../../`, `../../` solo bajo `tutoriales/`. Canonical EN, footer EN, schema en inglés.

- [ ] **Step 5: Run checks to verify it passes**

Run:
```bash
grep -q "youtube-nocookie.com/embed/UAMboy8mtro" tutoriales/sp-404-mk2-preparar-samples/index.html && echo EMBED_OK
grep -q "watch?v=UAMboy8mtro" tutoriales/sp-404-mk2-preparar-samples/index.html && echo FALLBACK_OK
grep -q '"@type": "HowTo"' tutoriales/sp-404-mk2-preparar-samples/index.html && grep -q '"@type": "VideoObject"' tutoriales/sp-404-mk2-preparar-samples/index.html && echo SCHEMA_OK
python -c "open('tutoriales/sp-404-mk2-preparar-samples/index.html','rb').read().decode('utf-8');open('tutoriales/en/sp-404-mk2-preparar-samples/index.html','rb').read().decode('utf-8');print('UTF8_OK')"
```
Repetir greps para la ruta EN.
Expected: `EMBED_OK FALLBACK_OK SCHEMA_OK UTF8_OK` en ambas.

- [ ] **Step 6: Commit**

```bash
git add tutoriales/sp-404-mk2-preparar-samples/index.html tutoriales/en/sp-404-mk2-preparar-samples/index.html
git commit -m "feat(tutoriales): guia sp-404-mk2-preparar-samples ES+EN con video UAMboy8mtro"
```

### Task 2: Índice + sitemap del lote 3

**Files:**
- Modify: `tutoriales/index.html`
- Modify: `tutoriales/en/index.html`
- Modify: `sitemap.xml`
- Test: `grep` checks

**Interfaces:**
- Consumes: 3 cards live (fl-studio-ia, partes, bass lines) + rutas nuevas de Task 1.
- Produces: índice con 4 cards live + 2 loc nuevas en sitemap.

- [ ] **Step 1: Write the failing check**

```bash
grep -q "sp-404-mk2-preparar-samples" tutoriales/index.html && grep -q "sp-404-mk2-preparar-samples" sitemap.xml && echo WIRED || echo NOT_WIRED
```

- [ ] **Step 2: Run check to verify it fails**

Run: mismo comando. Expected: `NOT_WIRED`

- [ ] **Step 3: Implement cards en `tutoriales/index.html` y `en/index.html`**

Agregar 4ª card: `SP-404 MK2: prepara tus samples` → `sp-404-mk2-preparar-samples/` (tag `Disponible`; EN `SP-404 MK2: prepare your samples`, `Available`). Teaser con `roland` / `sp 404 mk2` / `samples sd`.

- [ ] **Step 4: Implement `sitemap.xml` con 2 URLs**

`tutoriales/sp-404-mk2-preparar-samples/` weekly 0.8, `tutoriales/en/sp-404-mk2-preparar-samples/` monthly 0.7. Formato loc/changefreq/priority sin hreflang.

- [ ] **Step 5: Run checks to verify it passes**

Run:
```bash
grep -q 'href="sp-404-mk2-preparar-samples/"' tutoriales/index.html && echo IDX_ES_OK
grep -q "sp-404-mk2-preparar-samples" tutoriales/en/index.html && echo IDX_EN_OK
grep -c "sp-404-mk2-preparar-samples" sitemap.xml
```
Expected: `IDX_ES_OK IDX_EN_OK` y conteo `2`.

- [ ] **Step 6: Commit**

```bash
git add tutoriales/index.html tutoriales/en/index.html sitemap.xml
git commit -m "feat(tutoriales): activa sp-404 mk2 en indice y sitemap"
```

### Task 3: QA final y push

**Files:**
- Modify: ninguno (solo verificación; fix trivial permitido con commit extra reportado)
- Test: `grep` + `python` + browse visual

- [ ] **Step 1: Run link integrity check**

Run: `grep -rho 'href="[^"]*"' tutoriales/ index.html | sort -u`
Expected: 0 rotos; revertir side-effects de `sync_versions.py` si ensució `tools/` (no commitear).

- [ ] **Step 2: Run SEO/consent audit**

Run: para las 2 guías nuevas + índice ES+EN: `GTM-NMVJZ8VL` + `id="consent-banner"` + `creativecommons.org/licenses/by-nc-sa` presentes.
Expected: 4/4 OK (2 índices + 2 ES+EN de la guía).

- [ ] **Step 3: Visual check en Brave (browse conectado)**

Abrir la guía nueva a 360px y desktop: nav legible, embed 16:9 sin scroll-H, fallback + CTA visibles.

- [ ] **Step 4: Push de la rama feature (NO main)**

Run: `git log --oneline -5` + `git push -u origin <rama>`.
Expected: push OK de la rama feature; `main` intacto.
