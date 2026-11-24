# Tutoriales lote 2 (partes + bass lines) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Sumar las guías `partes-de-un-beat` (video pt1 `7LfwEb4ds4`) y `bass-lines-fl-studio` (video pt2 `1mFZIt85qLE`) ES+EN y activarlas en índice + sitemap.

**Architecture:** HTML estático con el patrón probado del lote 1 (ya mergeado en `main`): guía = hero + embed youtube-nocookie responsive + pasos + FAQ + CTA, JSON-LD HowTo + VideoObject. Índice y sitemap se extienden.

**Tech Stack:** HTML/CSS estático, youtube-nocookie embed, JSON-LD, GTM-NMVJZ8VL, Search Console.

**Spec:** `docs/superpowers/specs/2026-11-24-tutoriales-lote2-design.md` (extiende `docs/superpowers/specs/2026-11-24-tutoriales-design.md`)

## Global Constraints

- Sitio estático, sin build; copiar el patrón de `tutoriales/fl-studio-ia/index.html` (lote 1 en `main`).
- ES+EN siempre, con canonical + alternate hreflang es/en/x-default recíprocos.
- GTM `GTM-NMVJZ8VL` + consent banner `sb-consent` en cada página (default denied, uno solo de cada uno).
- Footer ES: `Shard Btmkr (Darío García) · canal y sitio ShardBeats · La Piedad, Mich. · <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" rel="license">Contenido del sitio: CC BY-NC-SA 4.0</a>`; EN: `Shard Btmkr (Dario Garcia) · ShardBeats channel & site · La Piedad, Mich. · <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" rel="license">Site content: CC BY-NC-SA 4.0</a>`.
- Apps TRAKK SUITE son `GPL-3.0-only` (NO menciones MIT).
- No romper URLs existentes. Archivos nuevos en UTF-8 (verificar con `python -c "open(f,'rb').read().decode('utf-8')"`; la consola PowerShell puede mostrar mojibake aunque el archivo esté bien).
- Videos: partes → `7LfwEb4ds4` (embed `https://www.youtube-nocookie.com/embed/7LfwEb4ds4`, thumb `https://i.ytimg.com/vi/7LfwEb4ds4/hqdefault.jpg`, watch `https://www.youtube.com/watch?v=7LfwEb4ds4`); bass → `1mFZIt85qLE` (mismo patrón con su ID).
- `uploadDate` del VideoObject: usar `2026-11-24` solo como fallback y reportarlo (fecha real desconocida sin API key).

## Review Focus

- Embed bloqueado por privacy/adblock deja página sin video visible — se espera fallback link "Ver en YouTube" / "Watch on YouTube" siempre visible bajo el video.
- hreflang/canonical cruzados mal puestos causan duplicado ES/EN — se espera alternates recíprocos exactos en las 4 páginas nuevas.
- GTM o consent duplicado/ausente rompe medición — se espera un solo GTM + un banner por página.
- Layout móvil del embed 16:9 se desborda — se espera embed responsive sin scroll horizontal a 360px.
- Ruta de links relativos mal calculada desde la profundidad correcta — se espera verificar cada `href` por profundidad (`tutoriales/X/` usa `../../`, `tutoriales/en/X/` usa `../../../` para raíz).

---

### Task 1: Guía partes-de-un-beat ES+EN

**Files:**
- Create: `tutoriales/partes-de-un-beat/index.html`
- Create: `tutoriales/en/partes-de-un-beat/index.html`
- Test: `grep`/`shell` + `python` UTF-8 decode (sin pytest en este repo)

**Interfaces:**
- Consumes: patrón `tutoriales/fl-studio-ia/index.html` (copiar estructura: nav, hero, embed, pasos, FAQ, CTA, schema, GTM, consent, footer), video `7LfwEb4ds4`.
- Produces: rutas `/tutoriales/partes-de-un-beat/` ES+EN con HowTo + VideoObject.

- [ ] **Step 1: Write the failing check**

```bash
test -f tutoriales/partes-de-un-beat/index.html -a -f tutoriales/en/partes-de-un-beat/index.html
```

- [ ] **Step 2: Run check to verify it fails**

Run: `test -f tutoriales/partes-de-un-beat/index.html -a -f tutoriales/en/partes-de-un-beat/index.html; echo $?`
Expected: `1`

- [ ] **Step 3: Implement `tutoriales/partes-de-un-beat/index.html` en ES**

Título exacto `Partes de un beat: estructura de intro, verso y hook | ShardBeats`. 400-600 palabras: pasos intro/verso/pre-hook/hook/outro con ejemplo de compases, cómo marcar secciones en el DAW, transiciones, CTA a `../../tools/trakkname/` (nombrar por sección) + `../../tools/`. Queries literales: `partes de un beat`. Embed responsive `7LfwEb4ds4` + fallback `https://www.youtube.com/watch?v=7LfwEb4ds4`. FAQ 3 (¿cuántos compases por sección? / ¿qué es el hook? / ¿cómo marco secciones en FL Studio?). HowTo 5 pasos + VideoObject. Canonical `https://shardbeats.github.io/tutoriales/partes-de-un-beat/`, hreflang recíproco, nav con `← Tutoriales` a `../`, GTM + consent + footer ES.

- [ ] **Step 4: Implement `tutoriales/en/partes-de-un-beat/index.html` en EN**

Traducción directa. Título `Beat structure: intro, verse and hook arrangement | ShardBeats`. Links raíz con `../../../` (verificar por profundidad), `../../` solo para objetivos bajo `tutoriales/`. Canonical `/tutoriales/en/partes-de-un-beat/`, footer EN, mismo schema en inglés.

- [ ] **Step 5: Run checks to verify it passes**

Run:
```bash
grep -q "youtube-nocookie.com/embed/7LfwEb4ds4" tutoriales/partes-de-un-beat/index.html && echo EMBED_OK
grep -q "watch?v=7LfwEb4ds4" tutoriales/partes-de-un-beat/index.html && echo FALLBACK_OK
grep -q '"@type": "HowTo"' tutoriales/partes-de-un-beat/index.html && grep -q '"@type": "VideoObject"' tutoriales/partes-de-un-beat/index.html && echo SCHEMA_OK
python -c "open('tutoriales/partes-de-un-beat/index.html','rb').read().decode('utf-8');open('tutoriales/en/partes-de-un-beat/index.html','rb').read().decode('utf-8');print('UTF8_OK')"
```
Repetir los 3 greps para `tutoriales/en/partes-de-un-beat/index.html`.
Expected: `EMBED_OK FALLBACK_OK SCHEMA_OK UTF8_OK` en ambas.

- [ ] **Step 6: Commit**

```bash
git add tutoriales/partes-de-un-beat/index.html tutoriales/en/partes-de-un-beat/index.html
git commit -m "feat(tutoriales): guia partes-de-un-beat ES+EN con video 7LfwEb4ds4"
```

### Task 2: Guía bass-lines-fl-studio ES+EN

**Files:**
- Create: `tutoriales/bass-lines-fl-studio/index.html`
- Create: `tutoriales/en/bass-lines-fl-studio/index.html`
- Test: `grep`/`shell` + `python` UTF-8 decode

**Interfaces:**
- Consumes: mismo patrón lote 1, video `1mFZIt85qLE`.
- Produces: rutas `/tutoriales/bass-lines-fl-studio/` ES+EN.

- [ ] **Step 1: Write the failing check**

```bash
test -f tutoriales/bass-lines-fl-studio/index.html -a -f tutoriales/en/bass-lines-fl-studio/index.html
```

- [ ] **Step 2: Run check to verify it fails**

Run: `test -f tutoriales/bass-lines-fl-studio/index.html -a -f tutoriales/en/bass-lines-fl-studio/index.html; echo $?`
Expected: `1`

- [ ] **Step 3: Implement `tutoriales/bass-lines-fl-studio/index.html` en ES**

Título exacto `Cómo hacer bass lines en FL Studio | ShardBeats`. 400-600 palabras: elegir nota raíz/key, ritmo del 808/bajo con el kick, slides/portamento, niveles y saturación leve, CTA a `../../tools/` + resto de la serie (`../fl-studio-ia/`, `../partes-de-un-beat/`). Queries literales: `bass lines fl studio`, `como hacer bass lines`. Embed `1mFZIt85qLE` + fallback watch. FAQ 3 (¿bajo en la misma key? / ¿808 o bajo eléctrico? / ¿cómo evito choques con el kick?). HowTo + VideoObject. Canonical, hreflang, GTM, consent, footer ES.

- [ ] **Step 4: Implement `tutoriales/en/bass-lines-fl-studio/index.html` en EN**

Traducción directa. Título `How to make bass lines in FL Studio | ShardBeats`. Profundidad de links igual que Task 1 (`../../../` a raíz). Footer EN.

- [ ] **Step 5: Run checks to verify it passes**

Run: mismos 3 greps + UTF-8 con ID `1mFZIt85qLE` en ambas rutas.
Expected: `EMBED_OK FALLBACK_OK SCHEMA_OK UTF8_OK` en ambas.

- [ ] **Step 6: Commit**

```bash
git add tutoriales/bass-lines-fl-studio/index.html tutoriales/en/bass-lines-fl-studio/index.html
git commit -m "feat(tutoriales): guia bass-lines-fl-studio ES+EN con video 1mFZIt85qLE"
```

### Task 3: Índice + sitemap del lote 2

**Files:**
- Modify: `tutoriales/index.html`
- Modify: `tutoriales/en/index.html`
- Modify: `sitemap.xml`
- Test: `grep` checks

**Interfaces:**
- Consumes: cards actuales del índice (2ª `Soon`→partes, 3ª → nueva card bass lines; eliminar card de cuantizar), rutas de Task 1-2.
- Produces: índice con 3 cards live (FL Studio con IA, Partes de un beat, Bass lines) + 4 loc nuevas en sitemap.

- [ ] **Step 1: Write the failing check**

```bash
grep -q "partes-de-un-beat" tutoriales/index.html && grep -q "bass-lines" sitemap.xml && echo WIRED || echo NOT_WIRED
```

- [ ] **Step 2: Run check to verify it fails**

Run: mismo comando. Expected: `NOT_WIRED`

- [ ] **Step 3: Implement cards en `tutoriales/index.html` y `en/index.html`**

Card 2: `Partes de un beat` → `partes-de-un-beat/` (tag `Disponible`, quitar `Soon`/`#`). Card 3: reemplazar card de cuantizar por `Bass lines en FL Studio` → `bass-lines-fl-studio/` (tag `Disponible`; EN `Bass lines in FL Studio`, `Available`). Textos teaser 1-2 líneas con keywords.

- [ ] **Step 4: Implement `sitemap.xml` con 4 URLs**

`tutoriales/partes-de-un-beat/` weekly 0.8, `tutoriales/bass-lines-fl-studio/` weekly 0.8, `tutoriales/en/partes-de-un-beat/` monthly 0.7, `tutoriales/en/bass-lines-fl-studio/` monthly 0.7. Formato loc/changefreq/priority sin hreflang.

- [ ] **Step 5: Run checks to verify it passes**

Run:
```bash
grep -q 'href="partes-de-un-beat/"' tutoriales/index.html && grep -q 'href="bass-lines-fl-studio/"' tutoriales/index.html && echo IDX_ES_OK
grep -q "partes-de-un-beat" tutoriales/en/index.html && grep -q "bass-lines-fl-studio" tutoriales/en/index.html && echo IDX_EN_OK
grep -c "partes-de-un-beat\|bass-lines" sitemap.xml
```
Expected: `IDX_ES_OK IDX_EN_OK` y conteo `4`. Además: `! grep -q "cuantizar" tutoriales/index.html` (card eliminada).

- [ ] **Step 6: Commit**

```bash
git add tutoriales/index.html tutoriales/en/index.html sitemap.xml
git commit -m "feat(tutoriales): activa partes + bass lines en indice y sitemap"
```

### Task 4: QA final y push

**Files:**
- Modify: ninguno (solo verificación; fix trivial permitido con commit extra reportado)
- Test: `grep` + `python` + browse visual

- [ ] **Step 1: Run link integrity check**

Run:
```bash
grep -rho 'href="[^"]*"' tutoriales/ index.html | sort -u
```
Expected: ningún href a rutas inexistentes; `sync_versions.py` NO debe correrse sobre tutoriales (si se corre por rutina, revertir sus side-effects en `tools/` antes de commitear nada).

- [ ] **Step 2: Run SEO/consent audit**

Run: para `tutoriales/partes-de-un-beat/index.html`, `tutoriales/en/partes-de-un-beat/index.html`, `tutoriales/bass-lines-fl-studio/index.html`, `tutoriales/en/bass-lines-fl-studio/index.html`, `tutoriales/index.html`, `tutoriales/en/index.html`: `GTM-NMVJZ8VL` + `id="consent-banner"` + `creativecommons.org/licenses/by-nc-sa` presentes.
Expected: 6/6 líneas OK.

- [ ] **Step 3: Visual check en Brave (browse conectado)**

Abrir las 2 guías nuevas a 360px y desktop: nav legible, embed 16:9 sin scroll horizontal, CTA + fallback visibles. Reportar lo visto.

- [ ] **Step 4: Push de la rama feature (NO main)**

Run: `git log --oneline -6` + `git push -u origin <rama>`.
Expected: push exitoso de la rama feature; `main` intacto. Si falla 2 veces, reportar concern.
